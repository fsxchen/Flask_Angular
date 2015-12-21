#!/usr/bin/env python
#coding:utf-8

__auth__ = "fsxchen"

version = [0, 0, 1]


import os, sys
from optparse import OptionParser

SERVER_DIR_NAME = "server"
CLIENT_DIR_NAME = "client"
API_NAME = "api"
CONFIG_FILE_NAME = "config"


api_init_py = \
'''
from flask import Flask

from flask.ext.mongoengine import MongoEngine
from config import config


app = Flask(__name__)
#app.config.from_object(config['production'])
app.config.from_object(config['testing'])
db = MongoEngine(app)

from scan import scan as scan_blueprint

# to register model to blueprint
app.register_blueprint(scan_blueprint, url_prefix='/v1/scan')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
'''

config_file_mysql = \
'''
import os
from datetime import timedelta

class Config:
    CSRF_ENABLED = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = 'you never now'
    REMEMBER_COOKIE_SECURE = "never now"
    REMEMBER_COOKIE_DURATION = timedelta(days=14)
    # STATIC_URL_ROOT = os.path.join(basedir, "app/static")

    FLASKY_MAIL_SUBJECT_PREFIX = '[XXXX]'
    FLASKY_MAIL_SENDER = 'Admin <admin@example.com>'
    FLASKY_ADMIN = "admin@smtzs.com"

    MAIL_SERVER = "smtp.example.com"
    MAIL_USERNAME = "admin@example.com"
    MAIL_PASSWORD = "******"

    # OTHER config
    OSS_HOST="oss-cn-qingdao.aliyuncs.com"
    OSS_ACCESS_ID = "**********"
    OSS_SECRET_ACCESS_KEY = "********************"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://host:port/db?charset=utf8"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_POOL_SIZE=10

class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://host:port/db?charset=utf8'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///home/fsxchen/SMTZSV2.1/server/db/smtzs.db'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://host:port/db?charset=utf8'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

'''

run_py_file = \
'''
from api import app
if __name__ == "__main__":
    app.run("0.0.0.0", 9001, debug=True)

'''
