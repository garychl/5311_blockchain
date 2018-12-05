import hashlib
#the node class of binary merkle hash tree
class MerkleNode(object):
    def __init__(self,left=None,right=None,data=None,up = None):
        self.left = left
        self.right = right
        #data stores the hash value
        self.data = data
        self.up = up

class MerkleTree():
    def __init__(self,transactions):
        nodes = []

        for e in transactions:
            md5 = hashlib.md5()
            md5.update(e.encode())
            d = md5.hexdigest()
            nodes.append(MerkleNode(data=d))

        self.leaves = nodes
        self.root = createTree(self.leaves)

    def get_spv_root(self,transaction):
        md5 = hashlib.md5()
        md5.update(transaction.encode())
        d = md5.hexdigest()

        idx = -1
        for index,leaf in enumerate(self.leaves):
            if leaf.data == d:
                idx = index
                break

        # transaction is not in the tree
        if idx == -1:
            return {}

        leaf = self.leaves[idx]
        spv_start = leaf.data
        spv_route = []
        spv_index = []
        spv_root = self.root.data

        while not leaf.up == None:
            # if leaf is in the left of up leaf find and append right
            if leaf.up.left.data == leaf.data:
                spv_route.append(leaf.up.right.data)
                spv_index.append(0) # you are in left
            # if leaf is iin the right of up leaf find and append left
            elif leaf.up.right.data == leaf.data:
                spv_route.append(leaf.up.left.data)
                spv_index.append(1)  # you are in right

            leaf = leaf.up
        return {'root':spv_root,'spv_index':spv_index,'start':spv_start,'spv_route':spv_route}


def do_spv(route,transaction):
    try:


        root = route['root']
        spv_index = route['spv_index']
        spv_route = route['spv_route']
        start = route['start']

        md5 =hashlib.md5()
        md5.update(transaction)
        if not start == md5.hexdigest():
            return False

        for i,d in enumerate(spv_route):
            if(spv_index[i] == 0):
                md5 = hashlib.md5()
                md5.update(start+d)
            else:
                md5 = hashlib.md5()
                md5.update(d + start)
            start =  md5.hexdigest()

        if start == root:
            return True
        else:
            return False
    except:
        return False












#build the tree recursively
def createTree(nodes):
    list_len = len(nodes)
    if list_len == 0:
        return 0
    else:
        while list_len %2 != 0:
            nodes.extend(nodes[-1:])
            list_len = len(nodes)
        secondary = []
        #combine two nodes in pair
        for k in [nodes[x:x+2] for x in range(0,list_len,2)]:
            d1 = k[0].data.encode()
            d2 = k[1].data.encode()
            md5 = hashlib.md5()
            md5.update(d1+d2)
            newdata = md5.hexdigest()
            #print("nodehash:",newdata)
            node = MerkleNode(left=k[0],right=k[1],data=newdata)
            k[0].up = node
            k[1].up = node
            secondary.append(node)
        if len(secondary) == 1:
            return secondary[0]
        else:
            return createTree(secondary)




def get_merkle_data(transactions):
    nodes = []
    for i in transactions:
        md5 = hashlib.md5()
        md5.update(i.encode())
        d=md5.hexdigest()
        nodes.append(MerkleNode(data=d))

    root = createTree(nodes)
    root_hash = root.data
    return root_hash, nodes

if __name__ == "__main__":
    transactions = ['AB']
    tree = MerkleTree(transactions)

    spv_route = tree.get_spv_root('AB')
    print(do_spv(spv_route,'AB'))

