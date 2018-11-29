"""
help function to write and query data using python mysql
tutorial:https://www.w3schools.com/python/python_mysql_create_table.asp
"""
import mysql.connector


# create db statement
def create_db():
    sql = "CREATE DATABASE blockchainsystem"

# delete db statement
def del_db():
    sql = "DROP DATABASE IF EXISTS blockchainsystem"

# create blockchain table statement
def create_blockchain_table():
		sql = ""

# create transactions table statement (sender address, recipient address, amount)
def create_transactions_table():
		sql = ""

# insert blockchain statement(insert new block data into the table)
def insert_into_blockchain():
		sql = ""

# insert transactions statement(insert new txn data into the table)
def insert_into_transactions():
		sql = ""

# query blockchain statement (get the latest block)
def query_last_block():
		sql = ""

# query transactions statement (get the latest block)
def query_all_transactions():
		sql = ""





def write_to_json():
    pass
