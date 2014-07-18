#!/bin/sh

docker run -d -p 8080:8080 -p 30303:30303 --name="eth-json-rpc" cpp-ethereum-headless eth --json-rpc --mining on
