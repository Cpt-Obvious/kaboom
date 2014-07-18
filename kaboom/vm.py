#!/usr/bin/env python

import os

import docker

import constants

# boot2docker support
if 'DOCKER_HOST' in os.environ:
    docker_host = os.environ['DOCKER_HOST']
else:
    docker_host = 'unix://var/run/docker.sock'

c = docker.Client(base_url=docker_host,
                  version='1.13',
                  timeout=10)


def ensure_running():
    running = False

    containers = c.containers(quiet=False, all=False, trunc=True, latest=False, since=None, before=None, limit=-1)
    for container in containers:
        for name in container['Names']:
            if name == '/' + constants.VM_NAME:
                running = True
                break

    print "VM running: %s" % running

    if not running:
        start_docker()


def start_docker():
    container = c.create_container(constants.VM_IMAGE, constants.VM_CMD, name=constants.VM_NAME,
                                   detach=True, ports=[8080, 30303])
    c.start(container, port_bindings={8080: 8080, 30303: 30303})
    print "Starting VM in container %s" % container['Id']
