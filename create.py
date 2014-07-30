#!/usr/bin/env python

import argparse

import kaboom.api
import kaboom.compiler
import kaboom.constants
import kaboom.vm


def create(api, infile):
    bytecode = kaboom.compiler.compile(infile)
    print "Contract bytecode:", bytecode

    contract = api.create(bytecode, kaboom.constants.DEFAULT_KEY)
    print "Contract \"%s\" is at address %s" % (infile, contract)
    api.wait_for_next_block(verbose=True)

    assert api.is_contract_at(contract), "contract not present at address"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    kaboom.vm.ensure_running()
    api = kaboom.api.Api()
    api.wait_for_startup(verbose=True)

    create(api, args.infile)
