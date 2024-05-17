# saved as greeting-client.py
import Pyro4

ipAdressServer ="192.168.156.39"

name = input("¿Cuál es tu nombre? ").strip()

greetingMaker = Pyro4.core.Proxy('PYRO:Greeting@' + ipAdressServer + ':9090')    # use name server object lookup uri shortcut
print(greetingMaker.get_fortune(name))