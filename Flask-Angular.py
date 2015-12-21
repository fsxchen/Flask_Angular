#!/usr/bin/env python
#coding:utf-8

__auth__ = "fsxchen"

version = [0, 0, 1]

import os, sys
from optparse import OptionParser

from lib.main import client_init, server_init
from lib.utils import cc_chdir

SERVER_DIR_NAME = "server"
CLIENT_DIR_NAME = "client"
API_NAME = "api"
CONFIG_FILE_NAME = "config"


def touch_config_py():
    if os.path.isfile("config.py"):
        print "config.py file is exist"
        return
    else:
        with open("config.py", 'w') as f:
            f.write(config_file)

def flask_start(options):
    project_path = options.dirname if options.dirname else "."
    WORK_DIR_ROOT = os.path.abspath(project_path)
    project_name = options.project_name if options.project_name else "flask_project"
    PROJECT_ROOT = os.path.join(WORK_DIR_ROOT, project_name)
    if not os.path.exists(WORK_DIR_ROOT):
        raise Exception("路径不存在，您可以先创建")
    if os.path.exists(PROJECT_ROOT):
        if options.force==False:
            raise Exception("项目%s已经存在！" % project_name)
    else:
        os.mkdir(PROJECT_ROOT)
    with cc_chdir(PROJECT_ROOT):
        client_init(CLIENT_DIR_NAME, options.force)
        server_init(SERVER_DIR_NAME, options.force)


def flask_guide():
    welcome_msg = "\
    欢迎使用生成向导,继续请选择<Y/N>?\
    "
    welcome = raw_input(welcome_msg).strip()
    if welcome.lower() == "y":
        while 1:
            choice = raw_input().strip()
            print choice

if __name__ == "__main__":
    USAGE="%prog <options>"
    parser = OptionParser(usage=USAGE)
    parser.add_option('-v', "--version",
        action="store_true",
        dest="version",
        default=False,
        help=u"当前版本")
    parser.add_option('-D', "--dirname",
        action="store",
        dest="dirname",
        help=u"项目存放路径")

    parser.add_option('-B', "--big-project",
        action="store_true",
        dest="big_project",
        help=u"一个完整大项目")

    parser.add_option('-N', "--project-name",
        action="store",
        dest="project_name",
        help=u"项目名词")
    parser.add_option('-F', "--force",
        action="store_true",
        dest="force",
        default=False,
        help=u"强制执行")

    (options, args) = parser.parse_args()
    if len(sys.argv) == 1:
        flask_guide()
        exit()

    if options.version:
        print "version: %s" % ".".join([str(v) for v in version])
        exit(0)

    else:
        flask_start(options)
