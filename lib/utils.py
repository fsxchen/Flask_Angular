#!/usr/bin/env python
#coding:utf-8

import os
class cc_chdir:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.current_dir = os.getcwd()
    def __enter__(self):
        os.chdir(self.dir_name)
    def __exit__(self, exc_type, exc_value, exc_tb):
        os.chdir(self.current_dir)


def make_py_model_dir(model_name, init=None, flag=None):
    if make_dir_soft(model_name):
        with cc_chdir(model_name):
            md_id_filename = "__init__.py"
            with open(md_id_filename, 'w') as f:
                if not init == None:
                    f.write(init)
                else:
                    pass
        return True
    else:
        return False

def touch_file_soft(filename, text=""):
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            return False
    else:
        with open(filename, "w") as f:
            if text:
                f.write(text)

def make_dir(dir_name, flag=False):
    if os.path.exists(dir_name):
        if flag==False:
            raise Exception("%s目录与存在" % dir_name)
        else:
            return True
    else:
        os.mkdir(dir_name)
        return True

def make_dir_soft(dir_name):
    if os.path.exists(dir_name):
        if os.listdir(dir_name):
            return False
        return True
    else:
        os.mkdir(dir_name)
        return True
