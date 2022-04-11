import hashlib

class Node(object):
    def __init__(self, left, right, value, content):
        self.left = left
        self.right = right
        self.value = value
        self.content = content

    def hash(self, value):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def __str__(self):
        return str(self.value)

class MerkleTree:
    pass
#link koji sam naso 
#neke stvari mi nisu jasne jos pa ce nastavim kasnije
#https://onuratakan.medium.com/what-is-the-merkle-tree-with-python-example-cbb4513b8ad0