import pyautogui, sys, time, random

last_activity = time.time()

def mouseMove():

    try:
        while True:
            pyautogui.dragTo(random.randint(0, 1920), random.randint(0, 1200), 2, pyautogui.easeInBounce)
            pyautogui.keyDown('shift')
            pyautogui.keyUp('shift')
            pyautogui.press('left', presses=2, interval=0.5)
            pyautogui.press('right', presses=2, interval=0.5)
            time.sleep(240)
    except KeyboardInterrupt:
        sys.exit(0)

def main():

    mouseMove()

main()