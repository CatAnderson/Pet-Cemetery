import pdb
from models.owner import Owner
from models.pet import Pet

import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository

owner_repository.delete_all()
pet_repository.delete_all()

owner1 = Owner("Paul")
owner_repository.save(owner1)
owner2 = Owner("Cat")
owner_repository.save(owner2)
owner3 = Owner("Jenken")
owner_repository.save(owner3)

owner_repository.select_all()

pet1 = Pet("Little Mo", owner1, "cat", 3)
pet_repository.save(pet1)
pet2 = Pet("Frank", owner2, "dog", 5)
pet_repository.save(pet2)
pet3 = Pet("Fluffy", owner3, "dog", 1)
pet_repository.save(pet3)

pdb.set_trace()