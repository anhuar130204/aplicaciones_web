import web
from mvc.models.modelo_productos import ModeloProductos

render = web.template.render('mvc/views/')
m_productos = ModeloProductos()

class Borrar:
    def GET(self, id):
        try:
            # Lógica para obtener los detalles del producto con el ID especificado
            producto = m_productos.detalleProducto(id)
            return render.borrar_producto(producto)
        except Exception as e:
            return "Ocurrió un error al obtener los detalles del producto: {}".format(str(e))
    
    def POST(self, id):
        try:
            # Lógica para borrar el producto con el ID especificado
            # m_productos.borrarProducto(id)
            print("Producto con ID {} borrado correctamente".format(id))
            return "Producto con ID {} borrado correctamente".format(id)
        except Exception as e:
            print("Ocurrió un error al borrar el producto: {}".format(str(e)))
            return "Ocurrió un error al borrar el producto: {}".format(str(e))
