from clases.Factura import Factura
from clases.Producto import Producto
from clases.Persona import Persona
from clases.Pago import PagoEfectivo
from clases.Pago import PagoCredito
from clases.Pago import PagoDebito



#Crear objeto persona
x = Persona("Juan Camilo Martinez","Cra21B#27B-27","3015217812","Natural")

#Detalle de productos a llevar
e = Producto("WSWC1","Arroz",3,1000)
r = Producto("WSWC2","Aceite",3,1000)
f = Producto("WSWC2","Aceite",3,1000)

#Crear Objeto factura
factura = Factura("xxxxx","Tienda el porvenir", x)


#Agregar Objetos a factura
factura.AgregarProductos(e)
factura.AgregarProductos(r)
factura.AgregarProductos(f)

#Calcular Total de factura
factura.CalcularTotal()


#Metodo de Pago
pagE = PagoEfectivo (factura)
pagC = PagoCredito(factura,"012121254",5,"CASD545")
pagD = PagoDebito (factura,1235456)

#Mostar factura y pago realizado
print(factura.MostrarFactura())
print(pagE.mostrarPago())

print(factura.MostrarFactura())
print(pagC.mostrarPago())

print(factura.MostrarFactura())
print(pagD.mostrarPago())





