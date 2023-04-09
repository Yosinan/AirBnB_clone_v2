#!/usr/bin/python3
'''
Deploy archive

Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to web servers (web-01 & web-02)
'''
from datetime import datetime
from fabric.api import *
from os import path

# my servers ip
env.hosts = ['18.235.248.166', '100.26.226.17']

# user
env.user = 'ubuntu'

# private key of my rsa
env.key = '~/.ssh/school'


def do_deploy(archive_path):
    ''' deploy archive '''
    try:
        if not (path.exists(archive_path)):
            return False

        put(archive_path, '/tmp/')

        tar_dir = archive_path[-18:-4]

        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(tar_dir))
        # uncompress
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'.foramt(tar_dir, tar_dir))
        # Delete the archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(tar_dir))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(tar_dir))
        # Delete the symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create a new the symbolic link
        run('sudo ln -s /data/web_static/releases/\
            web_static_{}/ /data/web_static/current'.format(tar_dir))
    except BaseException:
        return False

    return True
