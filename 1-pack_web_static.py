#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric import task
from datetime import datetime

now = datetime.now().strftime('%Y%m%d%H%M%S')


@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    dir_name = f'web_static_{now}.tgz'
    c.local('mkdir -p versions')
    result = c.local(f'tar -cvzf versions/{dir_name} web_static', warn=True)
    if result.failed:
        return None
    return f'versions/{dir_name}'
