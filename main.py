import pyautogui, sys, time, random, pynput

last_activity = time.time()
automatedInput = False

def callbackFunction(*args):
    global automatedInput
    global last_activity
    if automatedInput == False:
        last_activity = time.time()

mouse_listener = pynput.mouse.Listener(on_move=callbackFunction)
keyboard_listener = pynput.keyboard.Listener(on_press=callbackFunction)        

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
            if (time.time() - last_activity) > 240:
                mouseMove()
                last_activity = time.time()
            time.sleep(30)
        except KeyboardInterrupt:
            sys.exit(0)

main()