import web
from mvc.models.modelo_productos import ModeloProductos

render = web.template.render('mvc/views', base="master")
m_productos = ModeloProductos()

class Detalle:
    def GET(self):
        try:
            # Simplemente renderiza la plantilla del formulario
            return render.detalle_productos()
        except Exception as e:
            return "Error " + str(e.args)
