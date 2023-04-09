#!/usr/bin/python3
"""
Deploy archive
Fabric script (based on 2-do_deploy_web_static.py) that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import path

# my servers ip
env.hosts = ['18.235.248.166', '100.26.226.17']

# user
env.user = 'ubuntu'

# private key of my rsa
env.key = '~/.ssh/id_rsa'


def do_pack():
    """generates a tgz archive"""
    try:
        ''' Fabric script that generates a .tgz archive '''

        arc_name = datetime.now().strftime("%Y%m%d%H%M%S")

        try:
            local("mkdir -p versions")
            arc_path = "versions/web_static_{}.tgz".format(arc_name)
            local("tar -czvf {} web_static/".format(arc_path))

            return 'arc_path'
        except Exception:
            return None


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
        run('sudo tar -xvzf /tmp/web_static_{}.tgz -C \
    /data/web_static/releases/web_static_{}/'.foramt(tar_dir, tar_dir))
        # Delete the archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(tar_dir))

        run('sudo mv \
    /data/web_static/releases/web_static_{}/web_static/* \
    /data/web_static/releases/web_static_{}/'.format(tar_dir))
        # Delete the symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create a new the symbolic link
        run('sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current'.format(tar_dir))
    except BaseException:
        return False

    return True

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
