from db.run_sql import run_sql

from models.pet import Pet
from models.owner import Owner

def save(pet):
    sql = "INSERT INTO pets (name, owner_id, species, age) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.owner.id, pet.species, pet.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet



def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)
    
