import re

import kaboom.api
import kaboom.compiler
import kaboom.vm

def _test_subcurrency(infile, market_cap):
    kaboom.vm.ensure_running()
    api = kaboom.api.Api()
    api.wait_for_startup(min_balance=True, verbose=True)

    code = kaboom.compiler.compile(infile)
    assert re.match(r'^0x[0-9a-f]+$', code)
    assert len(code) > 100

    owner_key = api.key()
    owner = api.coinbase()

    contract = api.create(code, owner_key)
    api.wait_for_next_block(verbose=True)
    assert api.is_contract_at(contract)
    assert int(api.storage_at(contract, owner), 16) == market_cap

    dest_secret = "cow"
    dest = api.secret_to_address(dest_secret)
    amount = 1000

    api.transact(contract, owner_key, data=[dest[2:], amount])
    api.wait_for_next_block(verbose=True)
    assert int(api.storage_at(contract, owner), 16) == market_cap - amount
    assert int(api.storage_at(contract, dest), 16) == amount

def test_subcurrency_serpent():
    _test_subcurrency("examples/subcurrency.se", 1000000)

def test_subcurrency_lll():
    _test_subcurrency("examples/currency.lll", int('0x1000000000000000000000000', 16))






