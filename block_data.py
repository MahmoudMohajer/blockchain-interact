from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

RPC = os.getenv("SEPOLIA_RPC_URL")

w3 = Web3(Web3.HTTPProvider(RPC))

latest_block = w3.eth.block_number
block_details = w3.eth.get_block(latest_block) 

print(f"Latest block number: {latest_block}")
print(f"Latest block details: {block_details}")