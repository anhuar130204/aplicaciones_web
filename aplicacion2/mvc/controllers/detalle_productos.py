import web
from mvc.models.modelo_productos import ModeloProductos, Producto
render = web.template.render('mvc/views', base="master")
m_productos = ModeloProductos()
class Detalle:
    def GET(self):
        try:
            datos = web.input()
            id_producto = datos.id_producto
            producto = m_productos.detalleProducto(id_producto)
            return render.detalle_productos(producto)
        except Exception as e:
            return "Error " + str(e.args)
        

        
