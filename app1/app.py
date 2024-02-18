import web

urls = (
    '/', 'hello',
    '/pagina2', 'pagina2',
    '/soy3','soy3'
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello pagina1.miaf'
        
class pagina2:
    def GET(self):
        return "Hola pagina 2"

class soy3:
    def GET(self):
        return 'Hello soy 3'
    
if __name__ == "__main__":
    app.run()
