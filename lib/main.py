#!/usr/bin/env python
#coding:utf-8

import os
from lib.utils import cc_chdir
from lib.client_tml import app_init_file, router_init_file
from lib.client_tml import html_doc

from lib.utils import make_dir, make_dir_soft, make_py_model_dir, touch_file_soft
from lib.server_tml import api_init_py, config_file_mysql, run_py_file

def js_init(big):
    if make_dir_soft("js"):
        with cc_chdir("js"):
            with open("app.js", 'w') as app, open("router.js", 'w') as router:
                app.write(app_init_file)
                router.write(router_init_file)
            make_dir_soft("controllers")
            with cc_chdir("controllers"):
                touch_file_soft("Controllers.js", text="var ctr = angular.module('app.controllers',[]);\n")
            make_dir_soft("services")
            with cc_chdir("services"):
                touch_file_soft("Services.js", text="var ser = angular.module('app.services',[]);\n")

            make_dir_soft("directives")
            with cc_chdir("directives"):
                touch_file_soft("Directives.js", text="var dir = angular.module('app.directives', []);\n")
            make_dir_soft("filters")
            with cc_chdir("filters"):
                touch_file_soft("Filters.js", text="var appFilters = angular.module('app.filters', []);\n")

    else:
        return

def static_dir_init():
    if make_dir_soft("css"):
        with cc_chdir("css"):
            with open("main.css", 'w') as fd:
                pass
    if make_dir_soft("partials"):
        with cc_chdir("partials"):
            with open("main.html", 'w') as fd:
                fd.write("welcome !\n")
    return


def static_file_init():
    touch_file_soft("index.html", text=html_doc)

def config_init(db="mysql"):
    touch_file_soft("config.py", text=config_file_mysql)

def client_init(dir_name, force=None, big=False):
    if make_dir(dir_name, force):
        with cc_chdir(dir_name):
            js_init(big)
            static_dir_init()
            static_file_init()
            # with open("index.html")

def server_init(dir_name, force=None, big=False):
    if make_py_model_dir(dir_name, init=None, flag=force):
        with cc_chdir(dir_name):
            make_py_model_dir("api", init=api_init_py)
            config_init()
            touch_file_soft("run.py", text=run_py_file)
