import web
from mvc.models.modelo_contactos import ModeloContactos

# Define the render object
render = web.template.render('mvc/views', base="master")
m_contactos = ModeloContactos()
class Contactos:
    def GET(self):
        try:
            resultado = m_contactos.consultarContactos()
            return render.contactos(contactos=resultado)
        except Exception as e:
            return "Error " + str(e.args)
    

