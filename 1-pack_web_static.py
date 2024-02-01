#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric import task
from datetime import datetime


@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        dir_name = f'web_static_{now}.tgz'
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{dir_name} web_static')
        return f'versions/{dir_name}'
    except Exception:
        return None
