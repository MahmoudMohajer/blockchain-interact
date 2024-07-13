from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

RPC = os.getenv("SEPOLIA_RPC_URL")
PK = os.getenv("PK")

w3 = Web3(Web3.HTTPProvider(RPC))
account = w3.eth.account.from_key(PK)
w3.eth.default_account = account.address 

public_address = account.address 
eth_balance = w3.eth.get_balance(public_address)
print(f"{public_address} has {w3.from_wei(eth_balance, 'ether')} ETH balance")