from src.core.persona import PersonaBuilder

if __name__ == "__main__":
    try:
        # Usando el patrón Builder para crear una persona
        persona_ejemplo = (
            PersonaBuilder()
            .set_datos_personales("Ana", 30, "123456789")
            .set_datos_contacto("ana.gomez@mail.com", "9876543210", "Calle Falsa 123")
            .build()
        )
        print("¡Persona creada con éxito!")
        print(persona_ejemplo)

        # Ejemplo de validación fallida
        print("\nIntentando crear una persona con datos inválidos...")
        (
            PersonaBuilder()
            .set_datos_personales("Ana123", 150, "123")
            .build()
        )
    except ValueError as e:
        print(f"Error de validación: {e}")