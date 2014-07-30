#!/usr/bin/env python

import sys

import kaboom.api
import kaboom.constants
import kaboom.vm


def balance(api, address):
    balance = api.balance_at(address)
    print "%s %.4e" % (address, balance)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        address = sys.argv[1]
    else:
        address = kaboom.constants.DEFAULT_ADDRESS

    kaboom.vm.ensure_running()
    api = kaboom.api.Api()
    api.wait_for_startup(verbose=True)

    balance(api, address)
