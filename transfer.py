from web3 import Web3, HTTPProvider 
from web3.middleware import construct_sign_and_send_raw_middleware
from dotenv import load_dotenv 
import os 

load_dotenv()

RPC = os.getenv("SEPOLIA_RPC_URL")
PK = os.getenv("PK")

w3 = Web3(Web3.HTTPProvider(RPC))

account = w3.eth.account.from_key(PK)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
w3.eth.default_account = account.address 

# Recipient address
to_address = "0xEDEeBD1899FBae1593b001d4bD04F56428074968"  # Replace with the actual recipient address

# Amount of ETH to send (in Wei)
amount = w3.to_wei(0.01, 'ether')  # Sending 0.1 ETH

# Prepare the transaction
tx = {
    'to': to_address,
    'value': amount,
    'gasPrice': w3.eth.gas_price,
    'nonce': w3.eth.get_transaction_count(account.address),
}

# Estimate the gas cost of the transaction
estimated_gas = w3.eth.estimate_gas(tx)
tx['gas'] = int(estimated_gas * 1.2)

# Sign and send the transaction
signed_tx = account.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Wait for the transaction to be mined
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction sent: {tx_hash.hex()}")
print(f"Transaction mined in block: {tx_receipt['blockNumber']}")


