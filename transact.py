#!/usr/bin/env python

import kaboom.api
import kaboom.vm
from kaboom.constants import DEFAULT_KEY, FINNEY


def transact(api):
    dest_key = "xyzzy"
    dest = api.secret_to_address(dest_key)

    start_balance = api.balance_at(dest)
    print "Start balance", start_balance
    api.transact(dest, DEFAULT_KEY, value=1 * FINNEY)
    api.wait_for_next_block(verbose=True)
    end_balance = api.balance_at(dest)
    print "End balance", end_balance


if __name__ == '__main__':
    kaboom.vm.ensure_running()
    api = kaboom.api.Api()
    api.wait_for_startup()

    transact(api)
