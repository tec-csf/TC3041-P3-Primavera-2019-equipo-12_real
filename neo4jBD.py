    
#Daniel Pelagio
#Luis Carrasco
#Code to connect to a database at port bolt://localhost:7687 and queue a query
#compile and run with python3 <filename.py>
from neo4j import GraphDatabase #pip3 install neo4j

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)

def print_num_hyperlinks(tx, id):
    for record in tx.run("MATCH (n)-[:HYPERLINKS_TO]->() "
    					 "with n, count(r) as num_hyperlinks"
                         "WHERE n.nodeID = {id} "
                         "RETURN n, num_hyperlinks", id=id):
        print(record["m.name"])

with driver.session() as session:
    session.read_transaction(print_num_hyperlinks, "0")
