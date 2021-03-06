import mysql.connector
import hashlib
import json

class Connector(object):
    def __init__(self, user, password, dbname, host="localhost"):
        self.mydb = mysql.connector.connect(
          host=host,
          user=user,
          passwd=password,
          database=dbname
        )
        self.mycursor = self.mydb.cursor()

    # create blockchain table statement
    def create_blockchain_table(self):
        sql = "CREATE TABLE IF NOT EXISTS blockchainsystem.blockchain (\
            id INT,\
            nonce INT,\
            hash VARCHAR(255),\
            last_hash VARCHAR(255),\
            transactions VARCHAR(10000),\
            merkle_root VARCHAR(1000),\
            timestamp DOUBLE)"
        self.mycursor.execute(sql)
        print("Created blockchain table")

    def drop_blockchain_table(self):
        sql = "DROP TABLE IF EXISTS blockchainsystem.blockchain"
        self.mycursor.execute(sql)
        print("Dropped blockchain table")

    # create txn table to store unmined txn
    def create_transactions_table(self):
        sql = "CREATE TABLE IF NOT EXISTS blockchainsystem.transactions (\
            id INT,\
            sender_address VARCHAR(255),\
            receiver_address VARCHAR(255),\
            amount DOUBLE,\
            transactions_data VARCHAR(255),\
            transactions_data_hash VARCHAR(10000))"
        self.mycursor.execute(sql)
        print("Created transactions table")

    def drop_transactions_table(self):
        sql = "DROP TABLE IF EXISTS blockchainsystem.transactions"
        self.mycursor.execute(sql)
        print("Dropped transactions table")

    # insert blockchain statement(insert new block data into the table)
    def insert_into_blockchain(self, id, nonce, hash, transactions, merkle_root, timestamp):
        sql = "INSERT INTO blockchainsystem.blockchain (\
            id,\
            nonce,\
            hash,\
            transactions,\
            merkle_root,\
            timestamp\
            ) VALUES (%s, %s, %s, %s, %s, %s)"

        val = (id,nonce,hash,transactions,merkle_root,timestamp)

        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Inserted into blockchain table")

    # insert blockchain statement(insert new block data into the table)
    def savetodb(self, block):
        print(block)
        sql = "INSERT INTO blockchainsystem.blockchain (\
            id,\
            nonce,\
            hash,\
            last_hash,\
            transactions,\
            merkle_root,\
            timestamp\
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)"


        val = (block['index'],block['nonce'],block['hash'],block['last_hash'],\
            json.dumps(block['transactions']), block['merkleRoot'],block['timestamp'])

        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Inserted into blockchain table")


    # insert transactions statement(insert new,unmined txn data into the table)
    def insert_into_transactions(self, id, sender_address, receiver_address,\
    amount):
        sql = "INSERT INTO blockchainsystem.transactions (\
            id,\
            sender_address,\
            receiver_address,\
            amount,\
            transactions_data,\
            transactions_data_hash\
            ) VALUES (%s, %s, %s, %s, %s, %s)"

        transactions_data = "{} sends {} BTC to {}".format(sender_address,\
        amount, receiver_address)
        transactions_data_hash = hashlib.sha256(transactions_data.encode()).hexdigest()

        val = (id,sender_address,receiver_address, amount, transactions_data,\
        transactions_data_hash)

        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Inserted into transactions table")

    # query blockchain statement (get the latest block)
    def query_last_block(self):
        sql = "SELECT * FROM blockchainsystem.blockchain ORDER BY timestamp \
            DESC LIMIT 1"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        myresult = myresult[0]
        myresult_dict = {'id':myresult[0],'nonce':myresult[1],'hash':myresult[2],\
            'last_hash':myresult[3],'transactions':myresult[4], 'merkle_root':myresult[5],
            'timestamp':myresult[6]}
        return myresult_dict

    # query transactions statement (get all txn)
    def query_all_transactions(self):
        sql = "SELECT * FROM transactions"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        return myresult


# NodeA = Node("root", "password", "blockchainsystem")
# NodeB = Node("root", "password", "blockchainsystem2")
# NodeA.drop_blockchain_table()
# NodeA.drop_transactions_table()
# NodeA.create_blockchain_table()
# NodeA.create_transactions_table()
# block1={'id':3,'nonce':231,'hash':'dsfsdfa','last_hash':'sdfsdf',\
#     'transactions':'sdgdgs', 'merkle_root':'dsfdsg','timestamp':23}
# block2={'id':4,'nonce':231,'hash':'hash','last_hash':'lasthash',\
#     'transactions':'txn', 'merkle_root':'root','timestamp':32896}
# NodeA.savetodb(block1)
# NodeA.savetodb(block2)
# # NodeA.savetodb(1,3241,"0000dsf","[\"A sends B\",\"B send C\"]", '1ba3d50eb4ab68eda730d8c22f7fdef3706d5149c82e3d36b01e290ae15325b9','sfsf',1.753797)
# # NodeA.savetodb(1,3241,"0000dsf","[\"A sends B\",\"B send C\"]", '1ba3d50eb4ab68eda730d8c22f7fdef3706d5149c82e3d36b01e290ae15325b9','sdfsf',123.753797)
# # NodeA.insert_into_blockchain(1,3241,"0000670a9094720ea02dff0ac7d7cab3ae0f50c0c684d2c86beb6e647b2bb110","[\"A sends B\",\"B send C\"]", "1ba3d50eb4ab68eda730d8c22f7fdef3706d5149c82e3d36b01e290ae15325b9",1543672366.753797)
# # NodeA.insert_into_transactions(1, "add_A", "add_B", 20.123)
# # NodeA.insert_into_transactions(1, "add_A", "add_B", 1.123)
# myresult = NodeA.query_last_block()
# # NodeA.query_all_transactions()
# print(myresult)
