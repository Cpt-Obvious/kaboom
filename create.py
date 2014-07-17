#!/usr/bin/env python

import argparse
import time

import kaboom.api
import kaboom.compiler
from kaboom.constants import MIN_MINING_BALANCE, MINING_POLL_SLEEP


def wait_for_startup(api, coinbase):
    while True:
        balance = api.balance_at(coinbase)
        print "Balance:", balance
        if balance < MIN_MINING_BALANCE:
            print "Insufficient balance, sleeping %d seconds" % MINING_POLL_SLEEP
            time.sleep(MINING_POLL_SLEEP)
        else:
            break
    print "Listening:", api.is_listening()
    print "Mining: ", api.is_mining()
    print "Ready!"


def create(args):
    api = kaboom.api.Api()
    key = api.key()
    coinbase = api.secret_to_address(key)
    print "Coinbase address is:", coinbase
    wait_for_startup(api, coinbase)

    bytecode = kaboom.compiler.compile(args.infile)
    print bytecode

    contract = api.create(bytecode, key)
    print "Contract \"%s\" is at address %s" % (args.infile, contract)
    api.wait_for_next_block(verbose=True)

    assert api.is_contract_at(contract), "contract not present at address"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()
    create(args)
