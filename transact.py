#!/usr/bin/env python

import kaboom.api
from kaboom.constants import FINNEY


def transact(api):
    coinbase_key = api.key()

    dest_key = "xyzzy"
    dest = api.secret_to_address(dest_key)

    start_balance = api.balance_at(dest)
    print "Start balance", start_balance
    api.transact(dest, coinbase_key, value=100 * FINNEY)
    api.wait_for_next_block(verbose=True)
    end_balance = api.balance_at(dest)
    print "End balance", end_balance


if __name__ == '__main__':
    api = kaboom.api.Api()
    transact(api)
