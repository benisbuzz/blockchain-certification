from __future__ import annotations
from dataclasses import dataclass
import json
import time
from hashlib import sha256
from ecdsa import SigningKey, VerifyingKey
from typing import Any, Literal

def get_hashed_dict(data_dict: dict) -> bytes:
    return sha256(json.dumps(data_dict, sort_keys= True).encode()).hexdigest()

def get_signed_hash(data_hash: str, private_key: str) -> bytes:
    private_key = SigningKey.from_string(bytes.fromhex(private_key))
    return private_key.sign(bytes.fromhex(data_hash)).hex()

def get_request_block(request_chain: list, account_key: str, quantity: int) -> dict:
    return {
        "previous_hash": request_chain[-1]["hash"],
        "index": request_chain[-1]["data"]["index"] + 1,
        "account_key": account_key,
        "quantity": quantity,
        "timestamp": time.time()
    }

def get_verification_block(request_hash: str, decision: Literal[0, 1]):
    return {
        "request_hash": request_hash,
        "decision": decision,
        "timestamp": time.time()
    }

class Block:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.hash = get_hashed_dict(self.data)

    def sign_request(self, private_key: str) -> None:
        self.signature = get_signed_hash(self.hash, private_key)
        print(f"added signature to block:\n{self.signature}")
    
    
class Blockchain:
    def __init__(self, request_chain: list, verify_chain: list, mint_chain: list) -> None:
        for chain in [request_chain, verify_chain, mint_chain]:
            if len(chain) == 0:
                chain.append(self.get_genesis_block)
        self.request_chain = request_chain
        self.verify_chain = verify_chain
        self.mint_chain = mint_chain

    def get_genesis_block(self) -> Block:
        return Block({"hash": "0"*64, "index": 0})

    @property
    def last_block(self) -> dict[str, dict[str, Any]]:
        return self.chain[-1]
    
    def verify_block_signature(self, public_key: str, block_hash: str, signature: str) -> bool:
        public_key = VerifyingKey.from_string(bytes.fromhex(public_key))
        assert public_key.verify(bytes.fromhex(signature), bytes.fromhex(block_hash))
    
    def verify_block_hash()
    
    def add_block(self, block: Block) -> None:
        self.verify_block_signature(block.data["account_key"], block.hash, block.signature)
        self.chain.append(block.__dict__)

        
class VerifyBlockchain:
    def __init__(self, request_chain: list) -> None:
        self.request_chain = request_chain
    
    def verify_block():
        pass


@dataclass
class CarbonCoinApplication:
    public_key: str
    application_number: int
    carbon_coin_quantity: int
    timestamp: pd.Timestamp

class AirlineAccount:
    def init(self) -> None:
        self.public_key = "airline_public_key"
        self.private_key = "airline_private_key"
        self.balance = 0
        self.historical_applications = {}
        self.current_applications = {}

    def send_application(self, verifier_account: VerifierAccount, **kwargs) -> None:
        application = CarbonCoinApplication(**kwargs)
        key = sha256(json.dumps(application.__dict__, sort_keys=True).encode('utf8')).hexdigest()
        verifier_account.unreviewed_applications.update({key: application})
        self.current_applications.update({key: application})

class VerifierAccount:
    def init(self) -> None:
        self.public_key = "verifier_public_key"
        self.private_key = "verifier_private_key"
        self.reviewed_applications= {"succesful": {}, "unsuccesful": {}}
        self.unreviewed_applications: dict[str, CarbonCoinApplication] = {}

    def review_application(self, mint: MintAccount, application_key: str, success: bool) -> None:
        if success:
            account = self.unreviewed_applications[application_key]["public_key"]
            quantity = self.unreviewed_applications[application_key]["carbon_coin_quantity"]
            self.reviewed_applications["succesful"].update({application_key: self.unreviewed_applications[application_key]})
            del self.unreviewed_applications[application_key]
            mint.coins_to_mint.update({application_key: (account, quantity)})
        else:
            print("failed")
            pass

class MintAccount:
    def init(self) -> None:
        self.public_key = "mint_public_key"
        self.private_key = "mint_private_key"
        self.coins_to_mint = {}
        self.minted_coins = []
    
    def mint_coin(application_key: str) -> None:
        pass

