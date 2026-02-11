import pyautogui, sys, time, random, pynput, threading, pystray
from PIL import Image, ImageDraw

last_activity = time.time()
automatedInput = False

def create_icon():
    image = Image.new('RGB', (64, 64), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse([16, 16, 48, 48], fill=(0, 255, 0))
    return image

def callbackFunction(*args):
    global automatedInput
    global last_activity
    if automatedInput == False:
        last_activity = time.time()

mouse_listener = pynput.mouse.Listener(on_move=callbackFunction)
keyboard_listener = pynput.keyboard.Listener(on_press=callbackFunction)

def trayFunction():
    def quitFunction(icon, menu):
        icon.stop()
        sys.exit(0)
    icon = pystray.Icon(
    name = "Working hard...",
    icon = create_icon(),
    menu = pystray.Menu(
        pystray.MenuItem("Quit", quitFunction)
        )
    )
    icon.run()

tray_thread = threading.Thread(target=trayFunction)
tray_thread.daemon = True
tray_thread.start()

def mouseMove():

    try:
        global automatedInput
        automatedInput = True
        pyautogui.dragTo(random.randint(0, 1920), random.randint(0, 1200), 2, pyautogui.easeInBounce)
        pyautogui.keyDown('shift')
        pyautogui.keyUp('shift')
        pyautogui.press('left', presses=2, interval=0.5)
        pyautogui.press('right', presses=2, interval=0.5)
        automatedInput = False
    except KeyboardInterrupt:
        sys.exit(0)

def main():
    global last_activity
    keyboard_listener.start()
    mouse_listener.start()
    while True:
        try:
            if (time.time() - last_activity) > 5:
                mouseMove()
                last_activity = time.time()
            time.sleep(30)
        except KeyboardInterrupt:
            sys.exit(0)

main()