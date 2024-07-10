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
account = w3.eth.account.from_key(PK)
w3.eth.default_account = account.address 


FAUCET_ADDRESS = "0xC959483DBa39aa9E78757139af0e9a2EDEb3f42D"
faucet_abi = read_json("./abi/faucet.json")
USDC_ADDRESS = "0x94a9D9AC8a22534E3FaCa9F4e7F2E2cf85d5E4C8"
usdc_abi = read_json("./abi/usdc.json")

faucet_contract = w3.eth.contract(address=FAUCET_ADDRESS, abi=faucet_abi) 
usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=usdc_abi)

# Minting USDC
mintable = faucet_contract.functions.isMintable(USDC_ADDRESS).call()

if mintable:
    print("USDC is mintable")
    print("Minting USDC...")
    amount = w3.to_wei(10000, 'mwei')
    tx = faucet_contract.functions.mint(USDC_ADDRESS, account.address, amount).build_transaction({
        "from": account.address,
        "nonce": w3.eth.get_transaction_count(account.address)
    })

    signed_tx = w3.eth.account.sign_transaction(tx, PK)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("USDC minted!")
    print("Transaction hash:", tx_receipt["transactionHash"].hex())
    usdc_balance = usdc_contract.functions.balanceOf(account.address).call()
    print("USDC balance:", w3.from_wei(usdc_balance, 'mwei'))
else:
    print("USDC is not mintable")
