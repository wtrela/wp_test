import os
from time import sleep

from fabric.api import *

env['output_prefix'] = False


@task(name='backend')
def build_backend():
    local('docker build -f ./Dockerfile -t wptest_backend ./'.format(**os.environ))


@task(name='all')
def build_all():
    build_backend()


@task(name='net')
def net():
    local('docker network create -d bridge wptest_backend')
    local('docker network create -d bridge wptest_redis')
    local('docker network create -d bridge wptest_db')


@task(name='cleanup')
def cleanup():
    local('docker rmi $(docker images -aq --filter dangling=true)')


@task(name='bootstrap')
def bootstrap():
    build_all()
    local('docker-compose up -d')
    sleep(4)
    local('docker-compose run --rm backend makemigrations')
    sleep(1)
    local('docker-compose run --rm backend migrate')
    sleep(1)
    local('echo "from django.contrib.auth.models import User; User.objects.create_superuser(\'admin\', '
          '\'admin@admin.com\', \'admin\')" | docker-compose run --rm backend shell')
    sleep(4)
    local('docker-compose restart backend')
