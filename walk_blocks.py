#!/usr/bin/env python

from pprint import pprint

import kaboom.api
import kaboom.vm


def walk_blocks(api):
    block = api.last_block()
    parent_hash = block['hash']
    nr = int(block['number'])
    while parent_hash != "0000000000000000000000000000000000000000000000000000000000000000":
        block = api.block(parent_hash)
        print "Block #%d:" % nr
        pprint(block)
        parent_hash = block['parentHash']
        nr -= 1

if __name__ == '__main__':
    kaboom.vm.ensure_running()
    api = kaboom.api.Api()
    walk_blocks(api)
