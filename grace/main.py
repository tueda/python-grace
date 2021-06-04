"""Main program."""

import shutil
from pathlib import Path

import click

from . import GRACE_ROOT, __version__, commands
from .click_ext import OrderedGroup


@click.group(
    cls=OrderedGroup,
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.pass_context
@click.option("--version", is_flag=True, help="Show the version.")
def main(  # noqa: D103  # to suppress the help message
    ctx: click.Context, version: bool
) -> None:
    if ctx.invoked_subcommand is None:
        if version:
            click.echo(f"python-grace {__version__}")
        else:
            click.echo(main.get_help(ctx))


@main.command(no_args_is_help=True)
@click.argument("name")
def template(name: str) -> None:
    """Copy a template in.prc to the current directory."""
    src = GRACE_ROOT / "lib" / "templates" / name / "in.prc"
    dest = Path("in.prc")
    shutil.copy(src, dest)


def _add_template_help() -> None:
    if not template.help:
        return

    template_dir = GRACE_ROOT / "lib" / "templates"
    names = [str(f.relative_to(template_dir)) for f in template_dir.glob("*/*")]

    if names:
        s = ", ".join(names)
        template.help += f"\n\nNAME must be one of: {s}."


_add_template_help()


def _add_raw_commands() -> None:
    args = click.Argument(["args"], required=False, nargs=-1)
    context_settings = {"ignore_unknown_options": True, "help_option_names": []}

    for c in commands.raw_commands.values():
        if not c.available:
            continue
        name = c.name
        cmd = click.Command(
            name,
            context_settings=context_settings,
            callback=c,
            params=[args],
            help=f"Run {name}.",
        )
        main.add_command(cmd)


_add_raw_commands()
