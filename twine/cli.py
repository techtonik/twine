# Copyright 2013 Donald Stufft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse
import subprocess

from twine import __version__
from twine.commands import subcommands


def dispatch(argv):
    parser = argparse.ArgumentParser(prog="twine")
    subparse = parser.add_subparsers(dest="command", title="commands",
                                     metavar='')
    for command in subcommands:
        subparse.add_parser(command, help='')
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s version {0}".format(__version__),
    )
    parser.add_argument(
        "args",
        help=argparse.SUPPRESS,
        nargs=argparse.REMAINDER,
    )

    args = parser.parse_args(argv)

    # Dispatch to the real command
    p = subprocess.Popen(["twine-{0}".format(args.command)] + args.args)
    p.wait()

    # Return whatever exit code the sub command used
    return p.returncode
