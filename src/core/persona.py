from ..validators.validators import ValidadorDatosPersonales, ValidadorDatosContacto

class PersonaBuilder:
    """
    Clase Builder para construir objetos Persona paso a paso.
    """

    def __init__(self):
        self.persona = Persona()
        self.validador_personal = ValidadorDatosPersonales()
        self.validador_contacto = ValidadorDatosContacto()

    def set_datos_personales(self, nombre, edad, documento):
        """Establece y valida los datos personales."""
        if not self.validador_personal.validar_nombre(nombre):
            raise ValueError("Nombre no válido.")
        if not self.validador_personal.validar_edad(edad):
            raise ValueError("Edad no válida.")
        if not self.validador_personal.validar_documento_identidad(documento):
            raise ValueError("Documento de identidad no válido.")
        
        self.persona.nombre = nombre
        self.persona.edad = edad
        self.persona.documento = documento
        return self

    def set_datos_contacto(self, email, celular, direccion):
        """Establece y valida los datos de contacto."""
        if not self.validador_contacto.validar_email(email):
            raise ValueError("Email no válido.")
        if not self.validador_contacto.validar_celular(celular):
            raise ValueError("Número de celular no válido.")
        if not self.validador_contacto.validar_direccion(direccion):
            raise ValueError("Dirección no válida.")

        self.persona.email = email
        self.persona.celular = celular
        self.persona.direccion = direccion
        return self

    def build(self):
        """Construye y devuelve el objeto Persona."""
        return self.persona

class Persona:
    """
    Clase que representa una persona.
    Se construye a través de la clase PersonaBuilder.
    """

    def __init__(self):
        self.nombre = None
        self.edad = None
        self.documento = None
        self.email = None
        self.celular = None
        self.direccion = None

    def __str__(self):
        return (f"Persona:\n"
                f"  Nombre: {self.nombre}\n"
                f"  Edad: {self.edad}\n"
                f"  Documento: {self.documento}\n"
                f"  Email: {self.email}\n"
                f"  Celular: {self.celular}\n"
                f"  Dirección: {self.direccion}")