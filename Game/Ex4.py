from Game.Main import Main
from gui import Gui
import time
from client_python.client import Client

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)

gui = Gui(client)
control = Main(client)
client.start()

while client.is_running() == 'true':
    control.allocate()
    gui.draw()
    control.load()
    time.sleep(0.073)
    client.move()
    time.sleep(0.014)


client.stop_connection()
