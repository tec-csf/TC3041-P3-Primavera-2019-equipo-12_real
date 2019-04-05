# Ejecurar una instancia de neo4j en docker, con un volumen fisico
sudo docker run --name=neo4j -m=4g --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --env=NEO4J_AUTH=none neo4j

# Importar los csv dentro del contenedor de docker
docker cp nodes.csv neo4j:/var/lib/neo4j/import/
docker cp web-Google.csv neo4j:/var/lib/neo4j/import/

# El archivo txt (web-Google.txt) no tiene el formato csv para impoartar a neo4j, por lo que fue necesario
# primero obtener todos los nodos, haciendo una sola columna de las 2 del archivo. 
# Despues quitando los todas las rows repetidas (sort -u web-Google.txt -o web-Google.txt) 
# Finalmente simplemente se reenombra el archivo a nodos.csv

# Importar el grafo completo (demora mucho tiempo)

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/nodes.csv" AS row
CREATE (:node {nodeID: row.FromNodeId});

# Crear un index en nodeID

CREATE INDEX ON :node(nodeID);

# Crear las relaciones

USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:/web-Google.csv" AS row
MATCH (start:node {nodeID: row.FromNodeId})
MATCH (end:node {nodeID: row.ToNodeId})
MERGE (start)-[:HYPERLINKS_TO]->(end);
