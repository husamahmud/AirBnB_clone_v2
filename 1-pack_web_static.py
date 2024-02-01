#!/usr/bin/python3
"""Compress before sending"""
from fabric import task
from datetime import date
from time import strftime

date = date.today()


@task()
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    name = f"{date.year}{date.month}{date.day}{strftime('%I%M%S')}"
    result = c.local(f"tar cvf web_static_{name}.rgz ./web_static", warn=True)
    if result.failed:
        return None
    return result
