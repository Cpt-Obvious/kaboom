# Kaboom: Integration testing for Ethereum

> Rocket booster reentry, landing burn &amp; leg deploy were good, but lost hull integrity right after splashdown (aka kaboom)
>
> -- <cite>Elon Musk</cite>

Kaboom is a set of integration tests tools for Ethereum. It uses [Docker](https://www.docker.com/) for virtualization of the Ethereum client and the JSONRPC API for communication with the Ethereum client(s).

## Installation

Install Docker: https://docs.docker.com/installation/

Download the latest docker VM, these are frequently updated:
`docker pull cptobvious/cpp-ethereum-headless`

Install the required Python libraries with `pip`, it is suggested to do this within a [virtualenv](http://virtualenv.readthedocs.org/).

`pip install -r requirements.txt`

Serpent support is available by default.

To use LLL, the `lllc` compiler binary needs to be installed and available on the PATH; install it from https://github.com/ethereum/cpp-ethereum/

To use Mutan, the `mutan` compiler binary needs to be installed and available on the PATH; install it from https://github.com/obscuren/mutan/

## Usage: CLI

`./create.py examples/namecoin.se`

Compiles and creates a contract, waits for it to be mined and returns the contract address. Serpent, LLL and Mutan is supported (determined by the file extension).

`./transact.py`

Send a transaction to another address, waits for it to be mined and checks the resulting balance.

`./status.py`

Displays various client status metrics.

`./walk_blocks.py`

Walks through the blockchain and displays the result.

## Usage: Tests

`py.test test_subcurrency.py`

Compiles and creates the subcurrency contract with Serpent, LLL and Mutan. Sends a transaction and verifies the result.

`py.test test_subcurrency.py -k mutan -s`

Specifically run the mutan test (`-k` filters on keyword) and stream the output (`-s` disable test capturing of stdout/stderr).

## Usage: Docker

`./stop_eth.sh`

Stops the Docker process.

`docker ps`

Display running Docker processes.

`docker logs -f eth-json-rpc`

Tail the docker logs of the `eth-json-rpc` image.

## Debugging HTTP

To capture the HTTP trafic, install [mitmproxy](http://mitmproxy.org/) and run `mitmproxy` or `mitmdump`. Then ensure that the environment variable `HTTP_PROXY` is set when calling one of the above command line tools. Example:

`HTTP_PROXY="http://127.0.0.1:8080" ./transact.py`

If you run `mitmdump -w dumpfile`, the `dumpfile` will be written do disk and can be inspected with `mitmproxy -r dumpfile`
