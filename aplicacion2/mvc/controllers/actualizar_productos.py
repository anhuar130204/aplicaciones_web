import web
from mvc.models.modelo_productos import ModeloProductos

m_productos = ModeloProductos()

render = web.template.render('mvc/views', base="master")

class Actualizar:
    def GET(self):
        try:
            # Simplemente renderiza la plantilla del formulario
            return render.actualizar_productos()
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            datos = web.input()

            producto_actualizado = Producto(
                id_producto=int(datos.id_producto),
                nombre=datos.nombre,
                descripcion=datos.descripcion,
                precio=float(datos.precio),
                existencias=int(datos.existencias)
            )

            m_productos.actualizarProducto(producto_actualizado)

            return web.seeother('/detalle/{}'.format(datos.id))
        except Exception as e:
            # Manejar cualquier error
            return "Error: {}".format(str(e))
