# python
# Consideraciones
1. Tkinter es una libreria incluida en Python
2. Crear entorno virtual: python3 -m venv /path/to/new/virtual/environment
3. Instalar TODAS las librerías con el VENV activado, y por si acaso, hacer un cd al VENV antes de instalar
4. Librerías: pandas, sklearn(modelos ML), tensorflow(redes neuronales), tkdesigner(crear ventanas sin necesidad de codigo), psycopg2(conexion Python con Postgres), pyinstaller(crear ejecutables)


# Pasos desarrollo ventana Figma
0. Por si acaso, activar el Venv
1. Descargar archivo desde https://github.com/ParthJadhav/Tkinter-Designer/releases/tag/v1.0.4 y ejecutar el archivo designer.py con
python3 install -r requirements.txt
2. Login figma, crear la ventana, seguir las convenciones de: https://github.com/ParthJadhav/Tkinter-Designer/blob/master/docs/instructions.md#Using-Tkinter-Designer
3. Instalar Tkinter Designer usando pip3 install tkdesigner
4. comando con venv activado: tkdesigner.exe URL_figma(url obtenida con el copy en el share del proyecto) TOKEN_figma(main menu, settings token). quedaria asi: tkdesigner.exe URL TOKEN

# Pasos a seguir para programar
1. Crear una entidad Cliente en python, con sus atributos
2. Seleccion de fichero en la ventana y obtencion del ppath absoluto para abrirlo
3. Leer el fichero y convertir cada registro en un objeto de tipo cliente, y meterlo en una List
4. Conectar con la BBDD de Postgres
5. Hacer un for de la lista y hacer un insert a la BBDD PostgreSQL

server: localhost <br />
port: 5432 <br />
user: postgres <br />
password: amigous <br />
dbname: python_test <br />
table: cliente <br />
CREATE DATABASE python_test; <br />
\c python_test <br />
CREATE TABLE cliente (id_cliente int, nombre varchar(24), direccion varchar(56), telefono varchar(9)); <br />
SELECT * FROM cliente; <br />
DELETE FROM cliente; <br />

#### Proximo paso: recibir resultados de SQL en un DataFrame, esto abre la puerta a ML usando Sklearn