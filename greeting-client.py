# saved as greeting-client.py
import Pyro4

name = input("¿Cuál es tu nombre? ").strip()

greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut
print(greeting_maker.get_fortune(name))