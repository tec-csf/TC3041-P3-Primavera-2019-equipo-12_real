# Regresa el numero de hyperlinks a los que apunta el nodo 0

match (n) -[r:HYPERLINKS_TO]->() with n, count(r) as num_hyperlinks where n.nodeID = "0" return n, num_hyperlinks

# Regresa todos los nodos que apuntan al nodo 1

match (n) <-[r:HYPERLINKS_TO]-(f) where n.nodeID = "1" return n, r, f

# Regresa todos los nodos que tienen mas de 200 hyperlinks 

match (n)-[r:HYPERLINKS_TO]->() with n, count(r) as num_hyperlinks where num_hyperlinks > 200 return n, num_hyperlinks
