"""CLI interface."""

import click_completion

from . import cli

import pbcmd.hello

if __name__ == "__main__":
    click_completion.init()
    cli(prog_name="pb")
