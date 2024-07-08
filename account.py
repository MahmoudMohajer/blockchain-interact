from web3 import Web3
from eth_account import Account

# Generate a new account
new_account = Account.create()

# Get the private key
private_key = new_account._private_key.hex()

# Get the public address
address = new_account.address

print(f"Private Key: {private_key}")
print(f"Address: {address}")