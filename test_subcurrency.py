import pytest
import re

import kaboom.api
import kaboom.compiler
import kaboom.vm

@pytest.fixture
def api():
    kaboom.vm.ensure_running()
    api = kaboom.api.Api()
    api.wait_for_startup(min_balance=True, verbose=True)
    return api

def test_subcurrency_serpent(api):
    code = kaboom.compiler.compile("examples/subcurrency.se")
    assert re.match(r'^0x[0-9a-f]+$', code)
    assert len(code) > 100

    owner_key = api.key()
    owner = api.coinbase()

    contract = api.create(code, owner_key)
    api.wait_for_next_block(verbose=True)
    assert api.is_contract_at(contract)
    assert int(api.storage_at(contract, owner), 16) == 1000000

    dest_secret = "cow"
    dest = api.secret_to_address(dest_secret)

    api.transact(contract, owner_key, data=[dest[2:], 1000])
    api.wait_for_next_block(verbose=True)
    assert int(api.storage_at(contract, owner), 16) == 999000
    assert int(api.storage_at(contract, dest), 16) == 1000







