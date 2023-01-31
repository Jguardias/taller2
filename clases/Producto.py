class Producto:
    #Constructor
    def __init__(self,codigo,nombre,valorUnitario,unidad):
        self._codigo = codigo
        self._nombre = nombre
        self._valorUnitario = valorUnitario
        self._unidad = unidad
        self._subTotal = self.calcularSubTotal()
    #Getters
    def get_Codigo(self):
        return self._codigo      

    def get_Nombre(self):
        return self._nombre 

    def get_ValorUnitario(self):
        return self._valorUnitario

    def get_Unidad(self):
        return self._unidad

    def get_subTotal(self):
        return self._subTotal    
    #Setters
    def set_Codigo(self, codigo):
        self._codigo = codigo

    def set_Nombre(self, nombre):
        self._nombre = nombre     

    def set_ValorUnitario(self, valorUnitario):
        self._valorUnitario = valorUnitario

    def set_Unidad(self, unidad):
        self._unidad = unidad 
    #Metodos
    def calcularSubTotal(self):
        return self._unidad * self._valorUnitario
  