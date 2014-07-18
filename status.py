#!/usr/bin/env python

from pprint import pprint

import kaboom.api
import kaboom.vm


def status(api):
    print "Coinbase: %s" % api.coinbase()
    print "Listening? %s" % api.is_listening()
    print "Mining? %s" % api.is_mining()
    print "Peer count: %d" % api.peer_count()

    last_block = api.last_block()
    print "Last Block:"
    pprint(last_block)

    keys = api.keys()
    print "Keys:"
    for key in keys:
        address = api.secret_to_address(key)
        balance = api.balance_at(address)
        print "- %s %.4e" % (address, balance)

if __name__ == '__main__':
    kaboom.vm.ensure_running()
    api = kaboom.api.Api()
    api.wait_for_startup(verbose=True)

    status(api)
