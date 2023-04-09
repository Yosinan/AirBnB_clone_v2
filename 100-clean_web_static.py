#!/usr/bin/python3

import os
from fabric import *

from os import path

# my servers ip
env.hosts = ['18.235.248.166', '100.26.226.17']

# user
env.user = 'ubuntu'

# private key of my rsa
env.key = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep. Defaults to 0.
            If number is 0 or 1, keeps only the most recent archive. If
            number is 2, keeps the most and second-most recent archives,
            etc.
    """
    number = int(number)
    if number < 1:
        raise ValueError("Number of archives can not be less than 1.")

    with lcd("versions"):
        arcs = sorted(os.listdir("."))
        if number >= len(arcs):
            return
        to_del = archs[:-number]
        for archive in to_del:
            local("rm ./versions/{}".format(archive))

    with Connection(HOSTS[0]) as con:
        with con.cd("/data/web_static/releases"):
            archs = con.run("ls -tr").stdout.split()
            archs = [a for a in archs if "web_static_" in a]
            if number >= len(archives):
                return
            to_del = archs[:-number]
            for archive in to_del:
                con.run("rm -rf ./web_static/releases/{}".format(archive))
