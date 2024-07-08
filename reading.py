from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os
import json

def read_json(filename):
    with open(filename) as f:
        json_file = json.load(f)
    return json_file

load_dotenv()

RPC = os.getenv("SEPOLIA_RPC_URL")
PK = os.getenv("PK")

w3 = Web3(Web3.HTTPProvider(RPC))

USDC_ADDRESS = "0xd98B590ebE0a3eD8C144170bA4122D402182976f"
abi = read_json("./abi/usdc.json")

usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=abi)

# Reading data 
name = usdc_contract.functions.name().call()
decimals = usdc_contract.functions.decimals().call()
symbol = usdc_contract.functions.symbol().call()
totalSupply = usdc_contract.functions.totalSupply().call() 

print(f"Name: {name}")
print(f"Decimals: {decimals}")
print(f"Symbol: {symbol}")
print(f"Total Supply: {totalSupply}")