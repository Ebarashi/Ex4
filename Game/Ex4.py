from Game.Main import Main
from gui import Gui
import time
from client_python.client import Client


PORT = 6666
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)
gui = Gui(client)
play = Main(client)
client.start()

while client.is_running() == 'true':
    play.allocate()
    gui.draw()
    play.load_all()
    time.sleep(0.073)
    client.move()
    time.sleep(0.014)
client.stop_connection()
