#!/usr/bin/python3

from fabric.api import *
env.hosts = ['100.27.3.58', '54.174.20.166', '100.25.132.139']

def deploy():
    path = execute("do_pack")
    if path is None:
        return False
    return execute("do_deploy(path)")
