from persona import Persona
from factura_detalle import FacturaDetalle

#--------------------------------------------------------------
class Factura:
    """clase que implementa factura"""

    def __init__(self, numero: int, cliente: Persona):
        self.serie: str = 'F001'
        self.numero: int = numero
        self.cliente: Persona = cliente
        self.base_imponible: float = 0.00
        self.igv: float = 0.00
        self.total: float = 0.00
        self.detalle: FacturaDetalle = []
        pass
    
#--------------------------------------------------------------
    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} | {} | {} |".format(self.serie, self.numero, self.cliente.dni, self.cliente.nombres, self.base_imponible, self.igv, self.total))

#--------------------------------------------------------------
    def calcular_totales(self):
        for detalle in self.detalle:
            self.base_imponible = self.base_imponible+detalle.base_imponible
            self.igv = self.igv+detalle.igv
            self.total = self.total+detalle.total
