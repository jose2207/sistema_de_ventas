class FacturaDetalle:
    """Clase que implementa el detalle una factuta"""
    
#--------------------------------------------------------------
    def __init__(self, codigo:str, nombre:str, cantidad:float, precio:float):
        self.codigo:str=codigo
        self.nombre:str=nombre
        self.cantidad:float=cantidad
        self.precio:float=precio
        self.base_imponible:float=(self.precio*self.cantidad)/1.18
        self.igv:float=(self.precio*self.cantidad)-self.base_imponible
        self.total:float=self.precio*self.cantidad
        print(self.convertir_a_string())
        pass

#--------------------------------------------------------------
    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} | {} | {} |".format(self.codigo, self.nombre, self.cantidad, self.precio, self.base_imponible, self.igv,self.total))