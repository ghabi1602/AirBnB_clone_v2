#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
from op.path import isdir

def do_pack():
    """fabric function that generates a tgz archive"""
    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir(versions) is False:
            local('mkdir versions')

        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_server".format(file_name))
        return file_name
    except:
        return None
