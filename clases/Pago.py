

class Pago :
    def __init__(self,factura):
        self._monto = factura._total

    def get_monto(self):
        return self._monto
    
    def set_monto(self, monto):
        self._monto = monto

 

class PagoDebito(Pago):

    def __init__(self, factura,tarjetaDebito):
        super().__init__(factura)
        self._tarjetaDebito = tarjetaDebito

    def get_TD(self):
        return self._tarjetaDebito

    def set_TD(self,tarjetaDebito):
        self._tarjetaDebito = tarjetaDebito

    def mostrarPago(self):
        return f" Tipo de pago: Pago en Debito \n Numero Tarjeta de Debito: {self._tarjetaDebito} \n  Total: {self._monto}"

class PagoCredito(Pago):

    def __init__(self, factura,numeroCredito,numCuotas,codigoV):
        super().__init__(factura)
        self._numeroCredito = numeroCredito
        self._numCuotas = numCuotas
        self._codigoV = codigoV
    
    def get_NC (self):
        return self._numeroCredito

    def get_NumCuotas (self):
        return self._numCuotas

    def get_CodigoV (self):
        return self._codigoV

    def set_NC (self,numCredito):
        self._numeroCredito = numCredito

    def set_NumCuotas (self,numCuotas):
        self._numCuotas = numCuotas            

    def set_CodigoV (self,codigoV):
        self._codigoV = codigoV

    def generarCuota(self):
        cuota = self._monto/self._numCuotas 
        return cuota

    def mostrarPago(self):
        return f" Tipo de pago: Pago en Credito \n Numero de tarjeta: {self._numeroCredito} \n Codigo de Verificación: {self._codigoV} \n Numero de Cuotas {self._numCuotas} \n Valor de Cuota: {self.generarCuota()}"      

class PagoEfectivo(Pago):
    def __init__(self, factura):
        super().__init__(factura)

    def mostrarPago(self):
        return f" Tipo de pago: Pago en efectivo \n  Total: {self._monto}"
    
