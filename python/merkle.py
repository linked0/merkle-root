from hashlib import sha256
import sys
import binascii


class MerkleTree(object):
    def __init__(self, values):
        self.leaf_data = values
        
        if len(self.leaf_data) > 0:
            leaf_count = 1
            while leaf_count < len(self.leaf_data):
                leaf_count *= 2

            for i in range(len(values), leaf_count):
                self.leaf_data.append(self.leaf_data[-1])

    def makeTree(self):
        current_level = []
        for data in self.leaf_data:
            hash_value = self.get_double_sha256(data.encode('ascii'), None)
            node = dict({'hash': hash_value, 'data': data, 'child': None})
            # print(str(hash_value).upper())
            current_level.append(node)

        non_leaf_node = None
        iter_count = 0
        while len(current_level) != 1:
            parent_level = []
            for i in range(0, len(current_level), 2):
                node1 = current_level[i]
                node2 = current_level[i+1]
                hash_value = self.get_double_sha256(node1['hash'], node2['hash'])
                non_leaf_node = dict({'hash': hash_value, 'data': None, 'child': [node1, node2]})
                parent_level.append(non_leaf_node)

            iter_count += 1
            current_level = parent_level

        self.root_node = non_leaf_node

    def get_double_sha256(self, value1, value2):
        m = sha256()
        m.update(value1)
        if value2 != None:
            m.update(value2)
        one_hash = m.digest()
        double_hash = sha256(one_hash).digest()
        return double_hash

    def printTree(self, nodes, level=0):
        if nodes == None:
            nodes = [self.root_node]

        print('Level {0}:'.format(level))
        next_print_nodes = []
        for node in nodes:
            print(self.convert_ascii_str(node['hash']))
            if node['child'] != None:
                next_print_nodes = next_print_nodes + node['child']

        if len(next_print_nodes) != 0:
            self.printTree(next_print_nodes, level+1)

    def convert_ascii_str(self, hash):
       return str(binascii.hexlify(hash), encoding='ascii').upper()

def merkle(argv):
    mt = MerkleTree(argv)
    mt.makeTree()
    mt.printTree(None)


if __name__ == "__main__":
    # print(sys.argv[1:])
    merkle(sys.argv[1:])

