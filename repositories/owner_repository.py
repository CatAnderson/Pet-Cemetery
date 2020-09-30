from db.run_sql import run_sql

from models.owner import Owner
from models.pet import Pet

def save(owner):
    sql = " INSERT INTO owners (name) VALUES (%s) RETURNING *"
    values = [owner.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    owner.id = id
    return owner

def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['name'], row['id'])
        owners.append(owner)
    return owners
    
def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result["name"], result["id"])
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (name) = (%s) WHERE id= %s"
    values = [owner.name, owner.id]
    run_sql(sql,values)

def pets(owner):
    pets = []

    sql = "SELECT * FROM pets WHERE owner_id = %s"
    values = [owner_id]
    results = run_sql(sql, values)

    for row in results:
        pet = Pet(row['name], row['user_id], row['species']
