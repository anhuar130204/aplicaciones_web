"""libreria web.py"""
#rutas de los controladores
import web

urls = (
    '/', 'mvc.controllers.hello.Hello',
    '/pagina2', 'mvc.controllers.pagina2.Pagina2'  
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
