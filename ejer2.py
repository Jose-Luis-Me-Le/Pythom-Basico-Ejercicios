#Constantes
d1 = 0.10
d2 = 0.20
igv = 0.19

#variables
c = None
m_d = None
m_igv = None
pt = None

#Entrada por teclado
c = float(input("Ingrese el consumo que hizo: "))

#Proceso
if c <= 100:
   m_d = c * d1
elif c > 100:
    m_d = c * d2

m_igv = (c - m_d) * igv
p = c - m_d + m_igv

#Salida
print("Monto del descuento es: ", m_d)
print("Monto del IGV es: ", m_igv)
print("Cantidad a pagar es: ", p)