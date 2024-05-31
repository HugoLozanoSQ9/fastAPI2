# user entity recibe un item y lo va a retornar en diccionario
def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "password":item["password"],
        "age":item["age"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]