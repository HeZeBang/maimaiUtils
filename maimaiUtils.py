import pyautogui as pag
import pygetwindow as gw
import mss.tools

GAME_TITLE = 'Sinmai'

while len(gw.getWindowsWithTitle(GAME_TITLE)) < 1:
    print("Game not started, please start game and continue...")
    input("Press ENTER to continue, Ctrl+C to terminate")

window = gw.Win32Window(gw.getWindowsWithTitle(GAME_TITLE)[0]._hWnd)
print("Sinmai found!", window)

DEFAULT = [window.width, window.height, window.left, window.top]
print(f"Window size: {window.width}, {window.height}")
print(f"Window position: {window.left}, {window.top}")

print(f"Found {len(mss.mss().monitors) - 1} monitors")

# Define the functions

def get_window():
    """
    Return the latest Sinmai window
    """
    global window
    window = (gw.getWindowsWithTitle(GAME_TITLE)[0])
    print(window)
    return window

def window_move(dx: int, dy: int):
    """
    Move the window by dx, dy

    Arguments:
        dx(int) - the distance to move the window in the x axis
        dy(int) - the distance to move the window in the y axis
    """
    window.move(int(dx), int(dy))
    print(f"Current position: {window.left}, {window.top}")

def window_moveTo(x: int, y: int, monitor: int = 0):
    """
    Move the window to x, y

    Arguments:
        x(int) - the x coordinate to move the window to
        y(int) - the y coordinate to move the window to
        [optional] monitor(int) - the monitor to move the window to, start from 1
    """
    monitor = int(monitor)
    if(monitor > 0 and monitor < len(mss.mss().monitors)):
        monitor = mss.mss().monitors[monitor]
        x = monitor['left'] + int(x)
        y = monitor['top'] + int(y)
    window.moveTo(int(x), int(y))
    print(f"Current position: {window.left}, {window.top}")

def window_resize(dw: int, dh: int):
    """
    Resize the window by dw, dh

    Arguments:
        dw(int) - the width to resize the window by
        dh(int) - the height to resize the window by
    """
    window.resize(int(dw), int(dh))
    print(f"Current size: {window.width}, {window.height}")

def window_resizeTo(w: int, h: int):
    """
    Resize the window to w, h

    Arguments:
        w(int) - the width to resize the window to
        h(int) - the height to resize the window to
    """
    window.resizeTo(int(w), int(h))
    print(f"Current size: {window.width}, {window.height}")

def window_reset():
    """
    Reset the window to default size (when maimaiUtils started)
    """
    window.resizeTo(DEFAULT[0], DEFAULT[1])
    window.moveTo(DEFAULT[2], DEFAULT[3])
    print("Done")

def window_info():
    """
    Print the basic info of window / monitor
    """
    print("Window info: ")
    print(window)
    print("Monitor info: ")
    sct = mss.mss().monitors
    for i in range(len(sct)):
        print(f"Monitor #{i}")
        if(i == 0):
            print("This is the whole screen")
        elif(i == 1):
            print("This is the primary monitor")
        print(sct[i])

# Make a command line

FUNCTIONS = {
    'getwindow': get_window,
    'move': window_move,
    'moveto': window_moveTo,
    'resize': window_resize,
    'resizeto': window_resizeTo,
    'reset': window_reset,
    'info': window_info,
}

def help():
    print("Available commands: ")
    print(*(list)(FUNCTIONS.keys()), sep=", ")
    print()
    print("help - show this message")
    print("exit - exit the program")
    print()
    print("use 'help <command>' to get more information about a command")

def main():
    print()
    print("Welcome to maimaiUtils")
    help()
    while True:
        command = input("maimaiUtils> ").split()
        if command[0] in FUNCTIONS:
            try:
                FUNCTIONS[command[0]](*command[1:])
            except Exception as e:
                print("Error:", e)

        elif command[0] == 'help':
            if(len(command) == 1):
                help()
            elif(len(command) == 2):
                if command[1] in FUNCTIONS:
                    print(FUNCTIONS[command[1]].__doc__)
                else:
                    print("Command not found or no help available for this command", e)

        elif command[0] == 'exit':
            break

        else:
            print("Invalid command")
            

if __name__ == "__main__":
    main()