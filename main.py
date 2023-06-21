#luis llerena
#yuletsy fong
#leandro urbina
#gregorio rosales


from docente import Docente
from estudiante import Estudiante
from libro import Libro
from revista import Revista
from pedido import Pedido

d1 = Docente(cedula='0985685496', nombre='ANA', apellido='RUIZ', email='anaru@gmail.com',
             telefono='0954895962', direccion='PORTETE', numero_libros=0, activo=True, carrera='GIG',
             titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
d2 = Docente(cedula='0986985478', nombre='PATRICIO', apellido='DELGADO', email='patriciodel@gmail.com',
             telefono='0985412365', direccion='sauces', numero_libros=0, activo=True, carrera='GIG',
             titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')

print(d1)
print(d2)

# Estudiantes
e1 = Estudiante(cedula='0950643973', nombre='gregorio', apellido='rosales', email='gregoriorosales42@gmail.com',
                telefono='0961228092', direccion='sauces', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e2 = Estudiante(cedula='0951249390', nombre='yuletsy', apellido='fong', email='yulyfong@gmail.com',
                telefono='0995182475', direccion='pascuales', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e3 = Estudiante(cedula='0952822294', nombre='Leandro', apellido='Urbina', email='leandrour@gmail.com',
                telefono='0986179963', direccion='Trinitaria', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e4 = Estudiante(cedula='0989547152', nombre='Luis', apellido='Llerena', email='luisllerena@gmail.com',
                telefono='0993062825', direccion='Suburbio', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)

print(e1)
print(e2)
print(e3)
print(e4)


libro7 = Libro(codigo='19', autor='Jane Austen ', titulo='Orgullo y prejuicio', anio=2008, editorial='Editorial Alma', disponible=True, cantidad_disponible=85,tipo_pasta='NORMAL')
print(libro7)

revista78 = Revista(codigo='235', autor='JUAN', titulo='arte del sable', anio=2014, editorial='ISSU', disponible=True, cantidad_disponible=75,tipo='DIGITAL')
print(revista78)

pedido1 = Pedido(id='0950643973', solicitante='Gregorio Rosales', lista_material='Compra apartamento',
                 fecha_prestamo='12/Junio/2023', fecha_devolucion='22/Junio/2023')
print(pedido1)