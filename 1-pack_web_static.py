#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric.api import local, task
from datetime import datetime

now = datetime.now().strftime('%Y%m%d%H%M%S')


@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    dir_name = f'web_static_{now}.tgz'
    local('mkdir -p versions')
    result = local(f'tar -cvzf versions/{dir_name} web_static', warn=True)
    if result.failed:
        return None
    return f'versions/{dir_name}'
