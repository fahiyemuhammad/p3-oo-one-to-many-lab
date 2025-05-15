class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return Pet.all     
    
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else :
            raise Exception("Invalid pet. Must be a Pet instance.")
    

    def get_sorted_pets(self):
        return sorted(
            [pet for pet in Pet.all if pet.owner == self],
            key = lambda pet : pet.name
        )




class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner = ""):
        self.name = name 
        self.owner = owner

        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
            Pet.all.append(self)
        else :
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
    

    








          




    






        