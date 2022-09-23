""" Import the required libraries   """



"""
    Definition for our blockchain class
    
"""

class Blockchain():
    
    """
        default constructor for blockchain instantiation
        chain : whole blockchain 
        pending_transactions : transactions to be added in blockchain by block mining
        create_genesis_block : function to initialize the genesis block in the blockchain
    """
    def __init__(self) -> None:
        self.chain=[] 
        self.pending_transactions=[]
        self.create_genesis_block()
    
    def create_genesis_block():
        genesis_block= Block(0,)