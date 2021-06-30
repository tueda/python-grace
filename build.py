"""Build script."""

import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict

import skbuild

import grace.utils

PREFIX_DIR = Path(".") / "grace"
SRC_DIR = PREFIX_DIR / "extern"
PATCH_DIR = PREFIX_DIR / "patch"

GRACE_URL = "https://minami-home.kek.jp/grace221/grace.221.2006.0116.tgz"
GRACE_SHA256 = "a4971eddf65126a796c788661cdfa8c7cf738d91200d09a36999cc92baa943cf"
GRACE_SRC_DIR = SRC_DIR / "grace"
GRACE_PATCH_DIR = PATCH_DIR / "grace"


def build(setup_kwargs: Dict[str, Any]) -> None:
    """Build the extensions."""
    # Check the main CMake file.
    cmake_lists = SRC_DIR / "CMakeLists.txt"
    if not cmake_lists.is_file():
        raise RuntimeError(f"{cmake_lists.absolute()} not found")

    # Prepare the Grace source files.
    if not GRACE_SRC_DIR.exists():
        reset()

    # Back up the default parameters.
    old_sys_argv = sys.argv
    old_skbuild_plat_name = skbuild.constants._SKBUILD_PLAT_NAME

    try:
        # Build (Release).
        sys.argv = old_sys_argv.copy()
        sys.argv.append("--build-type")
        sys.argv.append("Release")
        skbuild.constants._SKBUILD_PLAT_NAME = "Release" / Path(old_skbuild_plat_name)

        skbuild.setup(
            **setup_kwargs,
            script_args=["build_ext"],
            cmake_languages=("C", "Fortran"),
            cmake_source_dir=str(SRC_DIR),
        )

        release_install_dir = Path(skbuild.constants.CMAKE_INSTALL_DIR())

        # Build (Debug).
        sys.argv = old_sys_argv.copy()
        sys.argv.append("--build-type")
        sys.argv.append("Debug")
        skbuild.constants._SKBUILD_PLAT_NAME = "Debug" / Path(old_skbuild_plat_name)

        skbuild.setup(
            **setup_kwargs,
            script_args=["build_ext"],
            cmake_languages=("C", "Fortran"),
            cmake_source_dir=str(SRC_DIR),
        )

        debug_install_dir = Path(skbuild.constants.CMAKE_INSTALL_DIR())

        # Destination.
        grace_dest_dir = Path("grace")

        # Delete the build artifacts copied in previous runs, just in case.
        grace.utils.remove_files(grace_dest_dir, "bin")
        grace.utils.remove_files(grace_dest_dir, "lib")

        # Copy the build artifacts.
        grace.utils.copy_files(release_install_dir, grace_dest_dir, "bin")
        grace.utils.copy_files(release_install_dir, grace_dest_dir, "lib")

        # For the debug version.
        dest_dir = grace_dest_dir / "bin" / "debug"
        dest_dir.mkdir(parents=True, exist_ok=True)
        for src in (debug_install_dir / "bin").glob("*"):
            shutil.copy2(src, dest_dir / src.name)

        dest_dir = grace_dest_dir / "lib" / "debug"
        dest_dir.mkdir(parents=True, exist_ok=True)
        for src in (debug_install_dir / "lib").glob("*"):
            if src.is_file():
                shutil.copy2(src, dest_dir / src.name)

    finally:
        sys.argv = old_sys_argv
        skbuild.constants._SKBUILD_PLAT_NAME = old_skbuild_plat_name


def reset() -> None:
    """Reset the GRACE source tree."""
    if GRACE_SRC_DIR.exists():
        shutil.rmtree(GRACE_SRC_DIR)
    grace.utils.download_archive(
        GRACE_URL,
        GRACE_SHA256,
        GRACE_SRC_DIR,
        normalize_newlines=True,
        patch_dir=GRACE_PATCH_DIR,
    )


def diff() -> None:
    """Update the patch set."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        temp_path = Path(tmp_dir)
        grace.utils.download_archive(
            GRACE_URL, GRACE_SHA256, temp_path, normalize_newlines=True
        )
        grace.utils.make_patch(
            temp_path, GRACE_SRC_DIR, GRACE_PATCH_DIR, normalize_newlines=True
        )


if __name__ == "__main__":
    build({})
