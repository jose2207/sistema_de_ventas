class Producto:
    """Clase que implementa producto"""

#--------------------------------------------------------------
    def __init__(self, codigo: str, nombre: str, precio: float, marca: str):
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.precio: float = precio
        self.marca: str = marca
        print(self.convertir_a_string())
        pass

#--------------------------------------------------------------
    def convertir_a_string(self):
        return print("| {} | {} | {} | {} |".format(self.codigo, self.nombre, self.precio, self.marca))
