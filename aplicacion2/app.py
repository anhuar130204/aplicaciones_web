
import web

urls = (
    '/', 'mvc.controllers.lista_productos.Productos',
    '/insertar', 'mvc.controllers.insertar_productos.Insertar',
    '/detalle','mvc.controllers.detalle_productos.Detalle',
    '/borrar','mvc.controllers.borrar_productos.Borrar',
    '/actualizar','mvc.controllers.actualizar_productos.Actualizar'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
