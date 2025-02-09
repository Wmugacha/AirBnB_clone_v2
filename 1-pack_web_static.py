#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """Function that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo."""

    archive_name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(archive_name))

        return "versions/web_static_{}.tgz".format(archive_name)

    except Exception as e:
        return None
