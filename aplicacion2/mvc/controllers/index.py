import web
from mvc.models.modelo_index import ModeloIndex

# Define the render object
render = web.template.render('mvc/views', base="master")
m_index = ModeloIndex()
# Define the Index class
class Index:
    def GET(self):
        try:
            resultado = m_index.consultarProductos()
            return render.index(resultado)
        except Exception as e:
            return "Error " + str(e.args)
    

