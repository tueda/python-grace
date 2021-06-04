import contextlib
import math
import os
import re
import subprocess
from pathlib import Path
from typing import Iterator, Sequence, Tuple

import pytest
from click.testing import CliRunner

import grace.commands
import grace.main


@contextlib.contextmanager
def chdir(path: Path) -> Iterator[Path]:
    """Context manager to temporarily change the current working directory."""
    old_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(old_cwd)


def run_grace(runner: CliRunner, args: Sequence[str]) -> None:
    """Run the "grace" command."""
    result = runner.invoke(grace.main.main, args)
    assert result.exit_code == 0


def run_make(args: Sequence[str]) -> None:
    """Run the Make utility."""
    env = os.environ.copy()
    cpu_count = os.cpu_count()
    if cpu_count is not None and cpu_count >= 1:
        # GNU Make accepts -j n for parallel build.
        env["GNUMAKEFLAGS"] = "-j cpu_count"
    result = subprocess.run(["make"] + list(args), env=env)
    assert result.returncode == 0


def run_executable(cmd: str, args: Sequence[str]) -> str:
    """Run a built executable in the current working directory."""
    result = subprocess.run(
        [f"./{cmd}"] + list(args), stdout=subprocess.PIPE, encoding="utf-8"
    )
    print(result.stdout)
    assert result.returncode == 0
    return result.stdout


def extract_gauge_result(result: str) -> Tuple[float, float, float]:
    """Extract the result of the "gauge" program (ans1, ans2, rel_err)."""
    lines = result.splitlines()

    def extract_value(key: str) -> float:
        for line in reversed(lines):
            m = re.match(r"^\s*" + key + r"\s*=(.*)$", line)
            if m:
                return float(m.group(1))
        else:
            return float("nan")

    return (
        extract_value("ans1"),
        extract_value("ans2"),
        abs(extract_value(r"ans1\s*/\s*ans2\s*-\s*1")),
    )


def extract_integ_result(result: str) -> Tuple[float, float]:
    """Extract the result of the "integ" program (result, abs_err)."""
    lines = result.splitlines()

    for line in reversed(lines):
        m = re.match(
            r"^\s*\d+\s+\d+\s+[\d.]+\s+[\d.]+E[+-]\d+\s+[\d.]+\s+"
            r"([\d.]+)\s*\(\s*\+-\s*([\d.]+)\s*\)\s*E([ +-]\d+)"
            r".*$",
            line,
        )
        if m:
            estimate = float(m.group(1))
            error = float(m.group(2))
            order = 10 ** int(m.group(3))
            return estimate * order, error * order
    else:
        return float("nan"), float("nan")


@pytest.mark.test_install()
def test_sm_eewwa(tmp_path: Path) -> None:
    with chdir(tmp_path):
        runner = CliRunner()

        run_grace(runner, ["template", "sm/eewwa"])
        run_grace(runner, ["grc"])
        if grace.commands.gracefig.available:
            run_grace(runner, ["gracefig", "-p"])
        run_grace(runner, ["grcfort"])
        run_make(["all"])
        gauge_result = extract_gauge_result(run_executable("gauge", []))
        integ_result = extract_integ_result(run_executable("integ", []))
        run_executable("spring", [])

        gauge_answer = 0.210130857
        integ_answer = 4.8883  # (+-0.0005)

        assert math.isclose(gauge_result[0], gauge_answer)
        assert math.isclose(gauge_result[1], gauge_answer)
        assert gauge_result[2] < 1e-9

        assert (
            integ_result[0] - integ_result[1] * 10
            < integ_answer
            < integ_result[0] + integ_result[1] * 10
        )


@pytest.mark.test_install()
def test_mssm_asw1sw1(tmp_path: Path) -> None:
    with chdir(tmp_path):
        runner = CliRunner()

        run_grace(runner, ["template", "mssm/asw1SW1"])
        run_grace(runner, ["grc"])
        if grace.commands.gracefig.available:
            run_grace(runner, ["gracefig", "-p"])
        run_grace(runner, ["grcfort"])
        run_make(["all"])
        gauge_result = extract_gauge_result(run_executable("gauge", []))
        integ_result = extract_integ_result(run_executable("integ", []))
        run_executable("spring", [])

        gauge_answer = 0.00435036634
        integ_answer = 0.10648  # (+-0.00002)

        assert math.isclose(gauge_result[0], gauge_answer)
        assert math.isclose(gauge_result[1], gauge_answer)
        assert gauge_result[2] < 1e-9

        assert (
            integ_result[0] - integ_result[1] * 10
            < integ_answer
            < integ_result[0] + integ_result[1] * 10
        )
