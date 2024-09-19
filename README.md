# Prueba Técnica para Desarrolladores Backend - Habi

## Introducción

Este proyecto consiste en el desarrollo de dos microservicios que permitirán a los usuarios de Habi consultar los inmuebles disponibles para la venta y, adicionalmente, darles "me gusta" a los inmuebles que les resulten interesantes. Los usuarios podrán aplicar diferentes filtros a sus búsquedas para facilitar la localización de inmuebles específicos y se mantendrá un registro del histórico de "me gusta" por usuario.

## Tecnologías Utilizadas

- **Lenguaje**: Python
- **Framework**: Flask o FastAPI para la creación de los microservicios.
- **Base de Datos**: PostgreSQL
- **ORM**: SQLAlchemy (en caso de usar Flask) o Tortoise ORM (en caso de usar FastAPI).
- **Autenticación**: JWT (JSON Web Tokens) para la autenticación de usuarios.
- **Documentación de API**: Swagger o ReDoc integrado con la herramienta seleccionada.
- **Pruebas Unitarias**: Pytest para las pruebas unitarias.
- **Versionamiento**: Git

## Estructura del Proyecto

real-state-microservices
│
├── consulta_servicio/
│   ├── app.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   ├── db/
│   │   └── database.py
│   └── tests/
│       └── test_routes.py
│
├── me_gusta_servicio/
│   ├── app.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   └── tests/
│       └── test_routes.py
│
├── README.md
└── requirements.txt


## Historias de Usuario

### Servicio de Consulta

1. Los usuarios pueden consultar los inmuebles con los estados: `pre_venta`, `en_venta` y `vendido`. Inmuebles con estados distintos nunca deben ser visibles por el usuario.
2. Los usuarios pueden filtrar los inmuebles por:
   - Año de construcción
   - Ciudad
   - Estado
3. Los usuarios pueden aplicar varios filtros en la misma consulta.
4. Los usuarios pueden ver la siguiente información del inmueble:
   - Dirección
   - Ciudad
   - Estado
   - Precio de venta
   - Descripción

### Servicio de “Me gusta”

1. Los usuarios pueden darle "me gusta" a un inmueble en específico y esto debe quedar registrado en la base de datos.
2. Los "me gusta" son de usuarios registrados, y debe quedar registrado en la base de datos el histórico de “me gusta” de cada usuario y a cuáles inmuebles.

## Instrucciones para la Prueba Técnica

1. El código debe quedar almacenado en un repositorio de Git.
2. Como tu primer commit, incluye este README detallando las tecnologías que vas a utilizar y cómo vas a abordar el desarrollo.
3. Si tienes dudas, escríbelas en este README y resuélvelas tú mismo, junto con la razón de por qué las resolviste de esa manera.
4. En el correo que recibiste la prueba deben estar las credenciales de acceso para conectarse a la base de datos.
5. El primer requerimiento (Servicio de consulta) es práctico, por lo tanto, se espera el código funcional.
6. Para el primer requerimiento, crear un archivo JSON con los datos que esperas que lleguen del front con los filtros solicitados por el usuario.
7. El estado actual de un inmueble es el último estado insertado en la tabla `status_history` para dicho inmueble.
8. No se espera que modifiques ningún registro en la base de datos, pero si necesitas una mayor cantidad de registros, puedes agregar nuevos.
9. La información de otros registros puede que tenga inconsistencias, recuerda manejar esas excepciones.
10. El segundo requerimiento (Servicio de “Me gusta”) es conceptual. No existe el modelo en la base de datos para soportar esta información.
11. Para el segundo requerimiento se espera que extiendas el modelo con un diagrama de Entidad-Relación para soportar esta información. No se espera código, sino el diagrama y el SQL para extender el modelo.
12. Tu código debe tener pruebas unitarias.
13. Recuerda divertirte haciendo este reto, si tienes bloqueos, continúa con otra parte.
14. Al terminar la prueba, responde al mismo correo desde el cual se te envió la prueba con el enlace al repositorio.

## Diagrama de Entidad-Relación (Segundo Requerimiento)

Agrega aquí el diagrama de Entidad-Relación propuesto, describiendo cómo has extendido el modelo para soportar la funcionalidad de "me gusta".

### Código SQL para Extender el Modelo

Incluye aquí el código SQL necesario para implementar la extensión del modelo.

## Preguntas y Resoluciones

1. **Duda**: ¿Debo utilizar JWT para la autenticación de usuarios?
   - **Respuesta**: Sí, es recomendable utilizar JWT para manejar la autenticación de usuarios de manera segura.
   
2. **Duda**: ¿Cómo manejar los estados de los inmuebles?
   - **Respuesta**: Utilizaré la tabla `status_history` para obtener el estado más reciente de cada inmueble y solo mostraré los inmuebles con los estados `pre_venta`, `en_venta` o `vendido`.

## Requerimientos no Funcionales

- Código fácil de mantener, leer y autodocumentado.
- Seguir la guía de estilos PEP8 para Python.
- Microservicios construidos para ser consumidos en una arquitectura REST.

## Puntos Extra

- Hacer las pruebas unitarias usando TDD (Test-Driven Development).
- Proponer un mejor modelo de la estructura actual de base de datos con el objetivo de mejorar la velocidad de las consultas, proporcionando un diagrama y la explicación de por qué lo modelaste de esa forma.
