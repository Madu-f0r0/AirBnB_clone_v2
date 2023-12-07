#!/usr/bin/python3
""" This script generates a `.tgz` archive """

from datetime import datetime
from os import mkdir


def do_pack():
    """Creates a `.tgz` archive from every file in `webstatic` directory"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        mkdir("versions")
    except FileExistsError:
        pass
    except Exception:
        print("Directory could not be created")

    archive_path = "versions/web_static_{}.tgz".format(now)
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None
