import json
import requests
import sys
import time
from uuid import uuid4

import constants


class ApiException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return "code=%d, message=\"%s\"" % (self.code, self.message)


class Api(object):

    def __init__(self, jsonrpc_url=constants.JSONRPC_URL):
        self.jsonrpc_url = jsonrpc_url

    def _rpc_post(self, method, params):
        payload = {
            "jsonrpc": "2.0",
            "id": str(uuid4()),
            "method": method,
            "params": params}
        headers = {'content-type': 'application/json'}

        r = requests.post(self.jsonrpc_url, data=json.dumps(payload), headers=headers)
        response = r.json()

        if 'error' in response:
            raise ApiException(response['error']['code'], response['error']['message'])

        return response.get('result')

    def balance_at(self, address):
        params = {
            'a': address
        }
        balance = self._rpc_post('balanceAt', params)
        if balance == "0x":
            return 0
        else:
            return int(balance, 16)

    def block(self, nr):
        params = {
            'a': nr
        }
        return self._rpc_post('block', params)

    def check(self, addresses):
        params = {
            'a': addresses
        }
        return self._rpc_post('check', params)

    def coinbase(self):
        return self._rpc_post('coinbase', None)

    def create(self, code, secret, gas=constants.DEFAULT_GAS, gas_price=constants.GAS_PRICE, endowment=0):
        params = {
            'bCode': code,
            'sec': secret,
            'xEndowment': hex(endowment),
            'xGas': hex(gas),
            'xGasPrice': hex(gas_price)}
        return self._rpc_post('create', params)

    def is_listening(self):
        return self._rpc_post('isListening', None)

    def is_mining(self):
        return self._rpc_post('isMining', None)

    def key(self):
        return self._rpc_post('key', None)

    def keys(self):
        return self._rpc_post('keys', None)

    def last_block(self):
        return self._rpc_post('lastBlock', None)

    def lll(self, contract):
        params = {
            's': contract
        }
        return self._rpc_post('lll', params)

    def peer_count(self):
        return self._rpc_post('peerCount', None)

    def secret_to_address(self, key):
        params = {
            'a': key
        }
        return self._rpc_post('secretToAddress', params)

    def storage_at(self, address, index):
        params = {
            'a': address,
            'x': index}
        return self._rpc_post('storageAt', params)

    def transact(self, dest, secret, data="", gas=constants.DEFAULT_GAS, gas_price=constants.GAS_PRICE, value=0):
        params = {
            'aDest': dest,
            'bData': data,
            'sec': secret,
            'xGas': hex(gas),
            'xGasPrice': hex(gas_price),
            'xValue': hex(value)}
        return self._rpc_post('transact', params)

    def wait_for_next_block(self, verbose=False):
        if verbose:
            sys.stdout.write('Waiting for next block to be mined')
            start_time = time.time()

        last_block = self.last_block()
        while True:
            if verbose:
                sys.stdout.write('.')
                sys.stdout.flush()
            time.sleep(constants.MINING_POLL_SLEEP)
            block = self.last_block()
            if block != last_block:
                break

        if verbose:
            print
            delta = time.time() - start_time
            print "Duration: %ds" % delta
