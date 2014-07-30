from pyethereum import utils

SZABO = 10**12
FINNEY = 10**15
ETHER = 10**18

DEFAULT_GAS = 10000
GAS_PRICE = 10 * SZABO

JSONRPC_URL = "http://192.168.59.103:8080"

MIN_MINING_BALANCE = 3 * ETHER
POLL_SLEEP = 5  # seconds

GENESIS_HASH = "0000000000000000000000000000000000000000000000000000000000000000"

DEFAULT_KEY = '0x' + utils.sha3("cow").encode('hex')  # part of the Genesis block
DEFAULT_ADDRESS = '0x' + utils.privtoaddr(DEFAULT_KEY[2:])  # cd2a3d9f938e13cd947ec05abc7fe734df8dd826

VM_NAME = "eth-json-rpc"
VM_CMD = "eth --json-rpc --mining on -v 4"
VM_IMAGE = "cptobvious/cpp-ethereum-develop"
