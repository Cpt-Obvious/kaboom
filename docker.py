#!/usr/bin/env python

import os

import docker

# boot2docker support
if 'DOCKER_HOST' in os.environ:
    docker_host = os.environ['DOCKER_HOST']
else:
    docker_host = 'unix://var/run/docker.sock'

c = docker.Client(base_url=docker_host,
                  version='1.13',
                  timeout=10)

container = c.create_container('busybox', 'ls')
print container
c.start(container)
c.wait(container)
print c.logs(container)
