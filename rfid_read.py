import time
from pirc522 import RFID
from pynput.keyboard import Key, Controller
rdr = RFID()
keyboard = Controller()
try:
        while True:
                rdr.wait_for_tag()
                uid = rdr.read_id(as_number = True)
                if uid is not None:
                        print(f'UID: {uid:X}')
                        keyboard.type(str(uid))
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        time.sleep(1)

# Calls GPIO cleanup

except KeyboardInterrupt:
    rdr.cleanup()
