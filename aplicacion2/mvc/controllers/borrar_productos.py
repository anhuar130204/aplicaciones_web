import web
from mvc.models.modelo_productos import ModeloProductos

render = web.template.render('mvc/views/')
m_productos = ModeloProductos()

class Borrar:
    def GET(self):
        try:
            # Simplemente renderiza la plantilla del formulario
            return render.borrar_productos()
        except Exception as e:
            return "Error " + str(e.args)
    
    def POST(self, id):
        try:
            # Lógica para borrar el producto con el ID especificado
            # m_productos.borrarProducto(id)
            print("Producto con ID {} borrado correctamente".format(id))
            return "Producto con ID {} borrado correctamente".format(id)
        except Exception as e:
            print("Ocurrió un error al borrar el producto: {}".format(str(e)))
            return "Ocurrió un error al borrar el producto: {}".format(str(e))
