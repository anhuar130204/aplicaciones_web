import web

class ModeloContactos:
    def __init__(self):
        pass
    def consultarContactos(self):
        contactos = [
            {
                "nombre": "Juan",
                "correo": "juan@ejemplo.com"
            },
            {
                "nombre": "Maria",
                "correo": "maria@ejemplo.com"
            }
        ]
        return contactos
