import uuid

class Cliente:
    #this(java) = self(python)
    def __init__(self, nombre, direccion, telefono):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    #decorator that makes usage of getter and setters much easier in Object-Oriented Programming.
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_direccion(self):
        return self.direccion
    
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def get_telefono(self):
        return self.telefono
    
    def set_telefono(self, telefono):
        self.telefono = telefono
