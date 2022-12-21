class Persona:
    "Clase que construye persona"

#--------------------------------------------------------------
    def __init__(self, dni, nombres, apellidos, direccion, telefono):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        print(self.convertir_a_string())

#--------------------------------------------------------------
    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} |".format(self.dni, self.nombres, self.apellidos, self.direccion, self.telefono))
