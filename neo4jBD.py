#Daniel Pelagio
#Luis Carrasco
#Code to connect to a database at port bolt://localhost:7687 and queue a query
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=None)

def print_friends(tx, name):
    for record in tx.run("MATCH (n:Person)-[:KNOWS]->(m) "
                         "WHERE n.name = {name} "
                         "RETURN m.name", name=name):
        print(record["m.name"])

with driver.session() as session:
    session.read_transaction(print_friends, "Jose")