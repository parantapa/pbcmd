"""Start a ssh based socks proxy using autossh."""

import click
from subprocess import run

from . import cli

@cli.command()
@click.option("-p", "--port", default=12001, help="Local port to listen on")
@click.option("-v", "--verbose", count=True, help="Verbosity level")
@click.argument("host", type=str, nargs=1)
def proxy(port, verbose, host):
    """Start a ssh proxy on local port to remove host."""
    click.secho(f"Starting proxy to {host} on port {port}", fg="green")

    options = [
        "-M", "0",
        "-o", "ServerAliveInterval 10",
        "-o", "ServerAliveCountMax 3",
        "-o", "ExitOnForwardFailure=yes",
        "-N",
        "-S", "none",
        "-D", f"127.0.0.1:{port}",
    ]

    for _ in range(verbose):
        options.append("-v")

    cmd = ["autossh"] + options + [host]
    run(cmd, check=True)
