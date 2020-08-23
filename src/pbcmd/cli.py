"""CLI interface."""

import click_completion

from . import cli

import pbcmd.hello
import pbcmd.calc
import pbcmd.proxy

if __name__ == "__main__":
    click_completion.init()
    cli(prog_name="pb")
