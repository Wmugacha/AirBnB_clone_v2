#!/usr/bin/python3
"""a script to send an archive file to a remote server
and decompress it"""

from fabric.api import run, env, put
import os.path

env.hosts = ['34.239.107.192', '100.25.46.128']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Function to deploy code archive and decompress it """

    """ Check archive_path """
    if not os.path.isfile(archive_path):
        return False

    """ Variables for filenames """
    compressed_file = archive_path.split("/")[-1]

    no_extension = compressed_file.split(".")[0]

    try:
        remote_path = "/data/web_static/releases/{}/".format(no_extension)

        sym_link = "/data/web_static/current"

        """ Upload archive to /tmp/ on webservers 1 & 2 """
        put(archive_path, "/tmp/")

        run("sudo mkdir -p {}".format(remote_path))

        """ Decompress archive """
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_file,
                                                  remote_path))

        run("sudo rm /tmp/{}".format(compressed_file))

        run("sudo mv {}/web_static/* {}".format(remote_path, remote_path))

        run("sudo rm -rf {}/web_static".format(remote_path))

        """ Delete symbolic link file from webserver """
        run("sudo rm -rf /data/web_static/current")

        """ Create new symbolic link linked to new code version """
        run("sudo ln -sf {} {}".format(remote_path, sym_link))

        return True
    except Exception as e:
        return False
