import web
from mvc.models.modelo_productos import ModeloProductos

# Define the render object
render = web.template.render('mvc/views', base="master")
m_productos = ModeloProductos()
class Productos:
    def GET(self):
        try:
            productos = m_productos.listaProductos()
            return render.lista_productos(productos)
        except Exception as e:
            return "Error " + str(e.args)
    

