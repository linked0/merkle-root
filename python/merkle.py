import sys, struct
from hashlib import sha256
# import binascii

class MerkleTree(object):
    def __init__(self, values):
        self.leaf_data = values
        self.root_node = None
        
        # to make full balanced tree, find nearest multiples of 2 above the length
        leaf_count = 0
        if len(self.leaf_data) > 1:
            leaf_count = 1
            while leaf_count < len(self.leaf_data):
                leaf_count *= 2
        elif len(self.leaf_data) == 1:
            leaf_count = 1
        
        # the last value is copied to empty slots in list
        for i in range(len(values), leaf_count):
            self.leaf_data.append(self.leaf_data[-1])

    def make_tree(self):
        current_level = []
        current_node = None
        
        # get hash value for data and save the value to node structure
        for data in self.leaf_data:
            hash_value = self.get_double_sha256(data.encode('ascii'), None)
            current_node = dict({'hash': hash_value, 'data': data, 'child': None})
#             print(self.convert_binary_to_ascii(current_node['hash']))
            current_level.append(current_node)

        # making non-leaf nodes continues until only one node exists
        iter_count = 0
        while len(current_level) != 1:
            parent_level = []
            for i in range(0, len(current_level), 2):
                node1 = current_level[i]
                node2 = current_level[i+1]
                hash_value = self.get_double_sha256(node1['hash'], node2['hash'])
                current_node = dict({'hash': hash_value, 'data': None, 'child': [node1, node2]})
                parent_level.append(current_node)

            iter_count += 1
            current_level = parent_level

        self.root_node = current_node

    def get_double_sha256(self, value1, value2):\
        # this function uses sha256 functions of the hashlib package
        m = sha256()
        m.update(value1)
        if value2 != None:
            m.update(value2)
        one_hash = m.digest()
        
        # date is double-sha256 hashed
        double_hash = sha256(one_hash).digest()
        return double_hash

    def print_tree(self, nodes, level=0):
        if nodes == None:
            nodes = [self.root_node]

        print('Level {0}:'.format(level))
        next_print_nodes = []
        for node in nodes:
            print(self.convert_binary_to_ascii(node['hash']))
            if node['child'] != None:
                next_print_nodes = next_print_nodes + node['child']

        if len(next_print_nodes) != 0:
            self.print_tree(next_print_nodes, level+1)
        
    def convert_binary_to_ascii(self, hash_str):
        # this function converts a binary string to ascii string
        ascii_str = ''
        chunk_size = 8
        for i in range(0, len(hash_str), chunk_size):
            bin_str = hash_str[i:i+chunk_size]
            res = struct.unpack('<BBBBBBBB', bin_str)
            hex_str = ''.join('%02X%02X%02X%02X%02X%02X%02X%02X'%(res))
            ascii_str += hex_str
        return ascii_str
    
#     def convert_binary_to_ascii_with_binascii(self, hash):
#         if sys.version_info < (3,0,0):
#             hash_str = str(binascii.hexlify(hash))
#             return hash_str.encode(encoding='ascii').upper()
#         else:
#             return str(binascii.hexlify(hash), 'ascii').upper()


def merkle(argv):
    mt = MerkleTree(argv)
    mt.make_tree()
    mt.print_tree(None)


if __name__ == "__main__":
    # Error check
    if (len(sys.argv) < 2):
        print("Error: Missing data parameters")
        exit(1)

    # Start making merkle tree
    merkle(sys.argv[1:])

