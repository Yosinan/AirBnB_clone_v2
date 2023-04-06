#!/usr/bin/python3
'''
Compress before sending --
Fabric script that generates a .tgz archive from the contents of the web_static folder

'''
from time import strftime
from datetime import datetime
from fabric.api import local

# do_pack function 
def do_pack():
    ''' Fabric script that generates a .tgz archive '''

    arc_name = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        arc_path = "versions/web_static_{}.tgz".format(arc_name)
        local("tar -cfzv {} web_static/".format(arc_path))

        return arc_path
    except Exception:
        return None
