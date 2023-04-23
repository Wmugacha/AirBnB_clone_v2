#!/usr/bin/python3
"""a script to send an archive file to a remote server
and decompress it"""

from fabric.api import run, env, put
import os.path

env.hosts = ['34.239.107.192', '100.25.46.128']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers
    """
    """ Checking for archive_path """
    if not exists(archive_path):
        return False

    """ File names with and without extension """
    arch_name = os.path.basename(archive_path)
    arch_name_minus = os.path.splitext(arch_name)[0]

    try:
        """ Saving archive to tmp on the web servers """
        put(archive_path, "/tmp/")

        """ Creating a directory for the deployed files"""
        run("sudo mkdir -p /data/web_static/releases/{}/"
            .format(arch_name_minus))

        """ Decompressing the archive into the we_static folder """
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(arch_name, arch_name_minus))

        """ Deleting the archive from the server """
        run("sudo rm /tmp/{}".format(arch_name))

        """ Moving files to new folder and deleting the old symbolic link """
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"
            .format(arch_name_minus, arch_name_minus))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(arch_name_minus))

        """ Deleting the old symbolic link and creating a new one """
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(arch_name_minus))

        return True

    except Exception as e:
        return False
