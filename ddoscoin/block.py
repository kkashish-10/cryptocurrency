"""import required libraries """

from datetime import datetime
import json
from hashlib import sha3_256


class Block():
    
    """
        A Block composed of a header and a body.
        Header in our definition are the attributes index,hash of previous block, a timestamp, nonce and the genesis block.
        Body is the transactions data
    """
    
    def __init__(self, index:"int", data: "json", previous_hash: "str", nonce=0) -> None:
        """_summary_

        Args:
            index (int): index of the block in chain
            data (json): pending transactions to be mined in the block
            previous_hash (str): hash of the previous node
            nonce (int, optional): one time use cryptographic value. Defaults to 0.
        """
        self.index = index
        self.timestamp = int(datetime.now().timestamp())
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        """
        computing hash for each block ensuring the security of each block individually, making it difficult to tamper the data

        Returns:
            str: hash string for the block using secure hashing algorithm family 3 sha3_256
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha3_256(block_string.encode()).hexdigest()
