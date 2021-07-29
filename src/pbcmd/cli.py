"""CLI interface."""
# pylint: disable=import-self,unused-import,unexpected-keyword-arg

from . import cli

import pbcmd.hello
import pbcmd.calc
import pbcmd.proxy
import pbcmd.timefmt
import pbcmd.git
import pbcmd.pyon2json
import pbcmd.csplit
# import pbcmd.rm_timestamped
import pbcmd.obscure
import pbcmd.mail

if __name__ == "__main__":
    cli(prog_name="pb")
