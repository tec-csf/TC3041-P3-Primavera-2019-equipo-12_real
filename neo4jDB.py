#Daniel Pelagio
#Luis Carrasco
#Code to connect to a database at port bolt://localhost:7687 and queue a query
#compile and run with python3 <filename.py>
from neo4j import GraphDatabase #pip3 install neo4j

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)

def print_num_hyperlinks(tx, id):
    for record in tx.run("MATCH (n)-[r:HYPERLINKS_TO]->() "
    					 "with n, count(r) as num_hyperlinks "
                         "WHERE n.nodeID = {id} "
                         "RETURN n.nodeID, num_hyperlinks", id=id):
        print("Hyperlinks from node " + str(id) + ": " + str(record["num_hyperlinks"]))

def print_directed_to(tx, id):
    for record in tx.run("MATCH (n)<-[r:HYPERLINKS_TO]-(f) "
                         "WHERE n.nodeID = {id} "
                         "RETURN n.nodeID, r, f.nodeID", id=id):
        print("Node to " + str(id) + " from: " + str(record["f.nodeID"]))

def print_node_gtr_than_n_hyperlinks(tx, id):
    for record in tx.run("MATCH (n)-[r:HYPERLINKS_TO]->() "
    					 "with n, count(r) as num_hyperlinks "
                         "WHERE num_hyperlinks > " + str(id) +
                         " RETURN n.nodeID, num_hyperlinks", id=id):
        print("Node with more than " + str(id) + " hyperlinks: " + str(record["n.nodeID"]) + " with " + str(record["num_hyperlinks"]))

with driver.session() as session:
    session.read_transaction(print_num_hyperlinks, "0")
    session.read_transaction(print_directed_to, "1")
    session.read_transaction(print_node_gtr_than_n_hyperlinks, "300")
