### Dzień dobry

- docker run \ --name testneo4j \ -p7474:7474 -p7687:7687 \ -d \ -v $HOME/neo4j/data:/data \ -v $HOME/neo4j/logs:/logs \ -v $HOME/neo4j/import:/var/lib/neo4j/import \ -v $HOME/neo4j/plugins:/plugins \ --env NEO4J_AUTH=neo4j/test1234 \ neo4j:latest
- pip install -r requirements.txt
- ~~.env~~: USERNAME="neo4j"
PASSWORD="test1234"
URI="bolt://localhost:7687"


>CREATE (:Employee {name:"Jim Halpert", role:"Salesman"})
CREATE (:Employee {name:"Pam Beesly", role:"Receptionist"})
CREATE (:Employee {name:"Dwight Schrute", role:"Assistant to the Regional Manager"})
CREATE (:Employee {name:"Michael Scott", role:"Regional Manager"})
CREATE (:Department {name:"Dunder Mifflin Paper Company"})

>CREATE (:Employee {name:"Leslie Knope", role:"Deputy Director"})
CREATE (:Employee {name:"Ron Swanson", role:"Director"})
CREATE (:Employee {name:"Tom Haverford", role:"Assistant City Manager"})
CREATE (:Employee {name:"April Ludgate", role:"Assistant to the Director"})
CREATE (:Department {name:"Parks and Recreation Department"})

>MERGE (e:Employee {name:"Jim Halpert"})
MERGE (d: Department {name:"Dunder Mifflin Paper Company"})
CREATE (e)-[:WORKS_IN]->(d)

>MERGE (e:Employee {name:"Pam Beesly"})
MERGE (d: Department {name:"Dunder Mifflin Paper Company"})
CREATE (e)-[:WORKS_IN]->(d)

>MERGE (e:Employee {name:"Dwight Schrute"})
MERGE (d: Department {name:"Dunder Mifflin Paper Company"})
CREATE (e)-[:WORKS_IN]->(d)

>MERGE (e:Employee {name:"Michael Scott"})
MERGE (d: Department {name:"Dunder Mifflin Paper Company"})
CREATE (e)-[:MANAGES]->(d)

>MERGE (e:Employee {name:"Leslie Knope"})
MERGE (d:Department {name:"Parks and Recreation Department"})
CREATE (e)-[:WORKS_IN]->(d)

>MERGE (e:Employee {name:"Ron Swanson"})
MERGE (d:Department {name:"Parks and Recreation Department"})
CREATE (e)-[:WORKS_IN]->(d)

>MERGE (e:Employee {name:"Ron Swanson"})
MERGE (d:Department {name:"Parks and Recreation Department"})
CREATE (e)-[:MANAGES]->(d)

>MERGE (e:Employee {name:"April Ludgate"})
MERGE (d:Department {name:"Parks and Recreation Department"})
CREATE (e)-[:WORKS_IN]->(d)

>MERGE (e:Employee {name:"Tom Haverford"})
MERGE (d:Department {name:"Parks and Recreation Department"})
CREATE (e)-[:WORKS_IN]->(d)
