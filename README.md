# PG2_PAARCIALL3

# nombre_apellido_pg2_tecba

Esta es una librería de Python para la validación de datos personales y de contacto, y la gestión de objetos `Persona`. El proyecto fue desarrollado como parte de una tarea académica.

---

### 1. Instalación

Para instalar la librería desde el entorno de prueba de TestPyPI, utiliza el siguiente comando:

```bash
pip install --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) --no-deps nombre_apellido_pg2_tecba==0.0.1
```
Si necesitas la versión completa del `README`, aquí la tienes:

---

```markdown
# nombre_apellido_pg2_tecba

Esta es una librería de Python para la validación de datos personales y de contacto, y la gestión de objetos `Persona`. El proyecto fue desarrollado como parte de una tarea académica.

---

### 1. Instalación

Para instalar la librería desde el entorno de prueba de TestPyPI, utiliza el siguiente comando:

```bash
pip install --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) --no-deps nombre_apellido_pg2_tecba==0.0.1
```

```python
from nombre_apellido_pg2_tecba.core.persona import PersonaBuilder

try:
    # Construcción de un objeto Persona de manera fluida y segura
    persona = PersonaBuilder() \
        .set_datos_personales("Celso", 30, "1234567890") \
        .set_datos_contacto("celso.p@example.com", "9876543210", "Calle Falsa 123") \
        .build()

    print("¡Persona creada con éxito!")
    print(persona)

    # Ejemplo de validación fallida con datos incorrectos
    print("\nIntentando crear una persona con datos inválidos...")
    PersonaBuilder() \
        .set_datos_personales("Cels0", 150, "123") \
        .build()

except ValueError as e:
    print(f"Error de validación: {e}")
```

```bash
testpy : https://test.pypi.org/project/validador-datos-personas/0.0.1/
```