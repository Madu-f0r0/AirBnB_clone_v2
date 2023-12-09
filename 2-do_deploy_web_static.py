#!/usr/bin/python3
""" This script generates a `.tgz` archive """

from datetime import datetime
from fabric.api import *
from os.path import exists

env.hosts = ["100.24.72.83", "100.25.162.168"]


def do_pack():
    """Creates a `.tgz` archive from every file in `webstatic` directory"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")

    archive_path = "versions/web_static_{}.tgz".format(now)
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not exists(archive_path):
        return False
    try:
        # Archive filename with extension
        archive_file_ext = archive_path.split("/")[-1]

        # Archive filename without extension
        archive_file_no_ext = archive_file_ext.split(".")[0]

        # Archive full path in remote machine
        arc_dir = "/tmp/{}".format(archive_file_ext)

        # Archive will be uncompressed and stored in this path
        new_arc_dir = "/data/web_static/releases/{}" \
                      .format(archive_file_no_ext)

        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(new_arc_dir))
        run("tar -xzf {} -C {}".format(arc_dir, new_arc_dir))
        run("rm {}".format(arc_dir))
        run("mv {0}/webstatic/* {0}".format(new_arc_dir))
        run("rm -rf {}/web_static".format(new_arc_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_arc_dir))
        return True
    except Exception:
        return False
