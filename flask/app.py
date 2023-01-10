from flask import Flask, jsonify, request
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
uri = os.getenv('URI')
user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
driver = GraphDatabase.driver(uri, auth=(user, password),database="neo4j")


def get_employees(tx, name=None, role=None, sort=None):
    query = "MATCH (e: Employee)"
    conditions = []
    if name is not None:
        conditions.append("toLower(e.name) CONTAINS toLower($name)")
    if role is not None:
        conditions.append("toLower(e.role) CONTAINS toLower($role)")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " RETURN e"
    if sort == "name_asc":
        query += " ORDER BY e.name"
    elif sort == "name_desc":
        query += " ORDER BY e.name DESC"
    results = tx.run(query, name=name, role=role).data()
    employees = [{"name": result['e']['name'],
                  "role": result['e']['role']} for result in results]
    return employees


@app.route('/employees', methods=['GET'])
def get_employees_route():
    name = request.args.get('name')
    role = request.args.get('role')
    sort = request.args.get('sort')
    with driver.session() as session:
        employees = session.read_transaction(get_employees, name, role, sort)
    response = {'employees': employees}
    return jsonify(response)


def add_employee(tx, name, role, department):
    query = "MERGE (e:Employee {name:$name, role:$role})" \
            "MERGE (d:Department {name:$department}) " \
            "MERGE (e)-[:WORKS_IN]->(d)"
    tx.run(query, name=name, role=role, department=department)


@app.route('/employees', methods=['POST'])
def add_employee_route():
    if request.json is None:
        return jsonify({"error": "Request body is empty"}), 400
    name = request.json.get("name")
    role = request.json.get("role")
    department = request.json.get("department")
    if name is None or role is None or department is None:
        return jsonify({"error": "Not all required fields have been provided"}), 400
    with driver.session() as session:
        result = session.run("MATCH (e:Employee) WHERE e.name = $name RETURN COUNT(e) as count", name=name).single()
        if result['count'] > 0:
            return jsonify({"error": "Employee already exists."}), 400
        session.write_transaction(add_employee, name, role, department)
        return jsonify({"message": "Employee added successfully."}), 201


if __name__ == '__main__':
    app.run()
