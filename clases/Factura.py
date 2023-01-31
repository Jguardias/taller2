class Factura:
    codigo = "00"    
    cont = 0
    def __init__(self,nit,razonSocial,persona):
        self.cont += 1
        self.codigo += str(self.cont)
        self.__nit = nit
        self.__razonSocial = razonSocial
        self.__persona = persona
        self._productos = []
        self._total = 0

    #Getter
    def get_Nit(self):
        return self.__nit

    def get_RazonSocial(self):
        return self.__razonSocial

    def get_Persona(self):
        return self.__persona

    def get_Total(self):
        return self._total

    def get_Productos(self):
        return self._productos
    #Setters

    def set_Nit(self,nit):
        self.__nit = nit

    def set_RazonSocial(self,razonSocial):
        self.__razonSocial = razonSocial    

    def set_Persona(self,persona):
        self.__persona = persona

    def set_Total(self,total):
        self._total = total

    def set_Productos(self,productos):
        self._productos = productos

    def AgregarProductos(self,producto):
        self._productos.append(producto)

    def CalcularTotal(self):
        
        for elementos in self._productos:
           self._total += elementos._subTotal

    def Detalle(self):
        for elementos in self._productos:
                print (f"codigo: {elementos._codigo} nombre: {elementos._nombre} unidades: {elementos._unidad} valor Unitario: {elementos._valorUnitario} subtotal: {elementos._subTotal}")

    

    def MostrarFactura(self):
         print("======    Información factura    ======\n")
         print(f"Codigo:{self.codigo}  Nit: {self.get_Nit()} Razon Social: {self.get_RazonSocial()} \n")
         print("======    Información Persona    ======\n")
         print(f"Nombre: {self.__persona.get_Nombre()}")
         print(f"Dirección: {self.__persona.get_Dire()}")
         print(f"Telefono: {self.__persona.get_Tele()}")
         print(f"Tipo de persona: {self.__persona.get_Tp()}\n")      
         print("======    Detalle    ======")
         print(f"{self.Detalle()}\n")
         print(f"Total a pagar: {self.get_Total()}\n")      

