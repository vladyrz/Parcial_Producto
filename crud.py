from parameters import collection

def mostrar_producto(id = None):
    if id is None:
        documents = collection.find()
        for document in documents:
            print(document)
    else:
        query = {"_id": id}
        document = collection.find_one(query)
        print(document)

def buscar_producto_categoria(categoria = None):
    if categoria is None:
        documents = collection.find()
        for document in documents:
            print(document)
    else:
        query = {"categoria" : categoria}
        document = collection.find_one(query)
        print(document)

def buscar_producto_nombre(nombre = None):
    if nombre is None:
        documents = collection.find()
        for document in documents:
            print(document)
    else:
        query = {"nombreProducto" : nombre}
        document = collection.find_one(query)
        print(document)

def create_producto(producto):
    result = collection.insert_one(producto)
    print(result.inserted_id)

def update_producto(id, json_update):
    query = {"_id" : id}
    new_values = {"$set" : json_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)

def delete_producto(id = None):
    if id is None:
        documents = collection.find()
        for document in documents:
            print(document)
    else:
        query = {"_id": id}
        document = collection.delete_one(query)
        print(document)