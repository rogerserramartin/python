nombre = "Pepe"
edad = 34
# aunque no hace falta especificar el tipo, se puede
edad: int = 36
PI = 3.1415
# podemos asignar varias variables a la vez
nombre, edad, PI = "Maria", 24, 3.14
print(nombre, edad, PI)
print(type(nombre))
print(type(edad))
print(type(PI))

def saludar():
    return "hola"
# de esta manera sabemos que saludar retorna un string si o si
def saludar2()->str:
    return "hola, string100%"

saludo_1 = saludar()
saludo_2 = saludar2()
print(saludo_1)
print(saludo_2)

#comentario de una linea
'''
Muchos comentarios
'''
""""
Muchos comentarios
"""
#! alerta de bettercomments
#? Pregunta
#* Remarcar
#TODO pendiente de hacer

string_muy_largo = """"
fwggwhwhwhwhhthhhet
jrjrjgnlkwgnwñklnwñhnwñhnwñhw
whnhkwhnwkñhnwh
hwrknhwrhpwnhwñhnñwhwh
"""
print(string_muy_largo)
# Ejemplo de tratamiento de strings mejorado, con {}
nombre = "mario"
email = "{}@dominio.com"
print(email.format(nombre))
# Ejemplo de tratamiento de strings mejorado, con f al principio
email2 = f"{nombre}@dominio.com"
print(email2)

#* Convenciones
#! variables: x, var, my_variable
#! Clases: Model, MiClase
#! Funcion: funcion, una_funcion
#! Constante: CONSTANTE, MI_CONSTANTE
#! Package: package, mypackage

import keyword
print(keyword.kwlist)

#!
#! iniciar venv Linux: source .\entorno_virtual\bin\activate
#! iniciar venv Windows: .\venv\Scripts\activate
#! desactivar venv Linux: Deactivate
#! desactivar venv Windows: Deactivate
numero = 10
positivo = "si" if numero >= 0 else "no"





