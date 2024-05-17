# saved as greeting-server.py
import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hola, {0}. Aquí tienes tu mensaje de la fortuna:\n" \
               "Tu número de la suerte de mañana es el: 10234, que tengas un excelente día.".format(name)

Pyro4.Daemon.serveSimple({
    GreetingMaker: "Greeting",
}, host="0.0.0.0" , port=9090, ns=False, verbose=True)