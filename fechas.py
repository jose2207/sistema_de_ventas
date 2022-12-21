class fecha:
    "Clase que construye fecha"

#--------------------------------------------------------------
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
        print(self.convertir_a_string())

#--------------------------------------------------------------
    def convertir_a_string(self):
        return print("| {} | {} | {} |".format(self.dia, self.mes, self.año))