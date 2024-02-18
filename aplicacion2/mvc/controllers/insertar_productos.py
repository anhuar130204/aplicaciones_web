import web
from mvc.models.modelo_productos import ModeloProductos

render = web.template.render('mvc/views/')
m_productos = ModeloProductos()

class Insertar:
    def GET(self):
        try:
            return render.insertar_productos()
        except Exception as e:
            # Manejar el error de alguna manera, por ejemplo, mostrar un mensaje de error genérico
            return "Ocurrió un error al procesar la solicitud GET: {}".format(str(e))

    def POST(self):
        try:
            form = web.input()
            nombre = form.nombre
            descripcion = form.descripcion
            precio = form.precio
            existencias = form.existencias
            # Imprimir los datos en la consola
            print("Nombre:", nombre)
            print("Descripción:", descripcion)
            print("Precio:", precio)
            print("Existencias:", existencias)
            # Aquí deberías llamar al método para insertar los datos en el modelo
            return render.insertar_productos()  # Devolvemos el formulario nuevamente para que se muestre después del POST
        except Exception as e:
            # Manejar el error de alguna manera, por ejemplo, mostrar un mensaje de error genérico
            return "Ocurrió un error al procesar la solicitud POST: {}".format(str(e))
