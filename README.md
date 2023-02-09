# Laboratorio_1-Estructura_de_datos_II
LABORATORIO #1

Implementación de módulo para la gestión de data maestra


Contexto

¿Qué es la información de clientes?
El número de canales con el que interactúan los clientes se ha incrementado de manera exponencial. La información de los clientes cambia y crece contantemente, es consumida por múltiples departamentos, y es un gran reto mantener una alta calidad de datos, evitar duplicados y que esté siempre actualizada.

Los datos de los clientes son el activo más importante para el éxito de su estrategia omnicanal, experiencia de clientes y transformación digital. Es importante ofrecer un trato consistente y personalizado sin importar el canal, así como optimizar los procesos de inteligencia de negocio.

 


Contenido estructurado de datos personales:
⦁	Identificación
⦁	Nombre y apellido
⦁	Edad y fecha de nacimiento
⦁	Genero y estado civil
⦁	Telefono y/o celular
⦁	Email personal/oficina
⦁	Nivel educativo
⦁	Rango de ingresos
⦁	Direcciones

Información Laboral
⦁	Nombre de la empresa
⦁	Profesión
⦁	Dirección

Redes sociales
⦁	Facebook
⦁	Instagram

Contenido no estructurado
⦁	Fotos
⦁	Contrato
Privacidad
⦁	No contacto por email
⦁	No contacto por teléfono
⦁	No contacto por SMS
⦁	No contacto por correo físico

Información personal
⦁	Esposa
⦁	Hijos
⦁	Hermano

¿Qué es un CMDM?

Customer Master Data Managment es un Sistema end-to-end utilizado para centralizar, organizar, gestionar, sincronizar, y enriquecer la información relativa a los clientes de acuerdo a las reglas del negocio, estrategias de mercado, servicios y ventas de la empresa.

¿Cuál es el valor de un CMDM?

Crea una única fuente fiable de información de clientes al integrar el conocimiento de cada uno de los departamentos de la empresa en un activo transversal a la organización.

¿Qué es un PMDM?

Product Master Data Managment es un Sistema end-to-end utilizado para centralizar, organizar, clasificar, sincronizar, y enriquecer la información relativa a los productos de acuerdo a las regla de negocio, estrategias de marketing y ventas de la empresa.

¿Cuál es el valor de un PMDM?

Crea una única fuente fiable de información de clientes al integrar el conocimiento de cada uno de los departamentos de la empresa en un activo transversal a la organización.



Proyecto

Usted ha sido contratado por una organización dedicada a la gestión de datos maestros.  La gestión de datos maestros, también conocida como MDM por sus siglas en inglés, es la disciplina que proporciona una visión confiable de los datos de cualquier organización y hace que dichos datos estén disponibles con facilidad para otras funciones empresariales.

Existen diferentes tipos de datos maestros, la organización que lo ha contratado desea implementar 2 módulos, un  módulo que permita gestionar los datos maestros de los productos, y un modulo que permita gestionar los datos maestros de los clientes. 

Para el desarrollo del módulo de gestión de productos solicitado se han levantado los siguientes requerimientos:

⦁	Desarrollo de una estructura jerárquica módular que permita agrupar los productos de acuerdo a una categoría. Existe un estándar global para categorizar productos llamado GS1 global product classification, el cual clasifica los productos de la siguiente por niveles.

Ejemplo:
 
  - Imagen: (Link)

La clasificación GS1 es un estándar que garantiza que cualquier producto sea clasificado con máximo 5 niveles, sin embargo, no todas las organizaciones siguen dicho estándar, algunos han diseñado su propia clasificación, es por esto que se requiere que la construcción de esta jerarquía sea parametrizada por el usuario.

Para más información consultar: https://gpc-browser.gs1.org/

Cada nodo de la jerarquía debe tener los siguientes datos:
⦁	Identificador
⦁	Nombre
⦁	Lista de nodos que contiene


⦁	Graficar la jerarquía desarrollada.

⦁	Desarrollar una interfaz de usuario que permita la creación de productos. Cada producto debe tener la siguiente información:
⦁	Identificador
⦁	Nombre (máximo 100 caracteres)
⦁	Descripción corta (máximo 500 caracteres)
⦁	Descripción larga (sin límite)
⦁	Imagen

Para el desarrollo del módulo de gestión de clientes solicitado se han levantado los siguientes requerimientos:

⦁	Desarrollo de una estructura jerárquica modular que permita agrupar los clientes de acuerdo a una categoría. 

⦁	Graficar la jerarquía desarrollada.

⦁	Desarrollar una interfaz de usuario que permita la creación de clientes. Cada cliente debe tener la siguiente información:

⦁	Identificación
⦁	Nombre 
⦁	Apellido
⦁	Edad 
⦁	Fecha de nacimiento
⦁	Genero
⦁	Eestado civil
⦁	Telefono
⦁	Celular
⦁	Email personal
⦁	Nivel educativo
⦁	Rango de ingresos
⦁	Direcciones
⦁	No contacto por email
⦁	No contacto por teléfono
⦁	No contacto por SMS
⦁	No contacto por correo físico

El sistema deberá constar de las siguientes opciones:
⦁	Buscar un producto/cliente
⦁	Visualizar ruta de producto/cliente
⦁	Editar un producto/cliente
⦁	Asignar producto/cliente a la clasificación deseada
⦁	Visualizar cuantos y cuales son los productos/clientes dado un nodo especifico.


Bono: 
⦁	Permitir la creación de jerarquías mediante archivos.



