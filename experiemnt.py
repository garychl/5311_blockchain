from sql import Node
import merkle_tree
import argparse

################################################################################################
# parser = argparse.ArgumentParser(description='model the blockchain env')
# #init: address, port number, db user, db pw, dbname,
# parser.add_argument("address", help="address of the node")
# parser.add_argument("port", help="port number of the node")
# parser.add_argument("DBuser", help="username of database login")
# parser.add_argument("DBpw", help="password of database login")
# parser.add_argument("DBname", help="name of database")
#
# args = parser.parse_args()
#
# print(args.address)
# print(args.port)
# print(args.DBname)


################################################################################################
# print("creating NodeA and insert txn")
# NodeA = Node("root", "password", "blockchainsystem")
# NodeA.drop_blockchain_table()
# NodeA.drop_transactions_table()
# NodeA.create_blockchain_table()
# NodeA.create_transactions_table()
# NodeA.insert_into_blockchain(1,3241,"0000dsf","[\"A sends B\",\"B send C\"]", '1ba3d50eb4ab68eda730d8c22f7fdef3706d5149c82e3d36b01e290ae15325b9',152366.753797)
# NodeA.insert_into_blockchain(1,3241,"0000dsf","[\"A sends B\",\"B send C\"]", '1ba3d50eb4ab68eda730d8c22f7fdef3706d5149c82e3d36b01e290ae15325b9',123.753797)
# NodeA.insert_into_blockchain(1,3241,"0000670a9094720ea02dff0ac7d7cab3ae0f50c0c684d2c86beb6e647b2bb110","[\"A sends B\",\"B send C\"]", "1ba3d50eb4ab68eda730d8c22f7fdef3706d5149c82e3d36b01e290ae15325b9",1543672366.753797)
# NodeA.insert_into_transactions(1, "add_A", "add_B", 20.123)
# NodeA.insert_into_transactions(1, "add_A", "add_B", 41.12)
# NodeA.insert_into_transactions(1, "add_C", "add_D", 19.123)
# NodeA.insert_into_transactions(1, "add_E", "add_B", 10.123)
# NodeA.insert_into_transactions(1, "add_F", "add_B", 130.123)
#
#
# last_block = NodeA.query_last_block()
# txn = NodeA.query_all_transactions()
#
# l = []
# for i in txn:
#     l.append(i[4])
# print(l)
#
# root_hash, nodes = merkle_tree.get_merkle_data(l)
# print(root_hash)
# for i in nodes:
#     print(i.data)
