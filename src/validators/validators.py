import re

class ValidadorBase:
    """Clase base con métodos de validación genéricos."""

    def validar_solo_numeros(self, texto):
        """Valida que la cadena contenga solo dígitos."""
        return texto.isdigit()

    def validar_solo_letras(self, texto):
        """Valida que la cadena contenga solo letras."""
        return texto.isalpha()

    def validar_alfanumerico(self, texto):
        """Valida que la cadena contenga letras y números."""
        return texto.isalnum()

class ValidadorDatosPersonales(ValidadorBase):
    """Clase especializada para validar datos personales."""

    def validar_edad(self, edad):
        """Valida que la edad sea un número entre 0 y 120."""
        return self.validar_solo_numeros(str(edad)) and 0 < int(edad) < 120

    def validar_nombre(self, nombre):
        """Valida que el nombre contenga solo letras y no esté vacío."""
        return self.validar_solo_letras(nombre)

    def validar_documento_identidad(self, documento):
        """Valida que el documento de identidad sea un número de 8 a 12 dígitos."""
        return self.validar_solo_numeros(documento) and 8 <= len(documento) <= 12

class ValidadorDatosContacto(ValidadorBase):
    """Clase especializada para validar datos de contacto."""
    
    def validar_email(self, email):
        """Valida el formato de un correo electrónico usando una expresión regular."""
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(regex, email) is not None

    def validar_celular(self, celular):
        """Valida que el número de celular contenga solo dígitos y tenga una longitud específica."""
        # Suponiendo un formato de 10 dígitos, por ejemplo
        return self.validar_solo_numeros(celular) and len(celular) == 10

    def validar_direccion(self, direccion):
        """Valida que la dirección sea alfanumérica y no esté vacía."""
        return self.validar_alfanumerico(direccion.replace(" ", "")) and len(direccion) > 5