import time
import random
import keyboard
import winsound
import win32gui
import win32api
import win32con


def find_window(title):
    """
    Searches for the first window whose title starts with the specified string.
    """

    def enum_window_callback(hwnd, results):
        window_title = win32gui.GetWindowText(hwnd)
        if window_title.lower().startswith(title.lower()):
            results.append(hwnd)

    windows = []
    win32gui.EnumWindows(enum_window_callback, windows)

    return windows[0] if windows else None


# Global variables to manage the clicking and holding states
is_left_clicking = True
is_right_holding = True
window_title = "Minecraft*"  # Title pattern to match
hwnd = find_window(window_title)


def main():
    if not hwnd:
        print(f"Error: No window matching '{window_title}' found.")
        return

    # Register hotkeys for toggling actions
    keyboard.add_hotkey("right ctrl+left", toggle_left_click)
    keyboard.add_hotkey("right ctrl+right", toggle_right_hold)
    print(
        "Hotkeys registered: Right Ctrl + Left Arrow to toggle left click, Right Ctrl + Right Arrow to toggle right hold."
    )

    # Initial state
    toggle_left_click()
    toggle_right_hold()

    while True:
        if is_left_clicking:
            mouse_down_duration = generate_gaussian_random(0.085, 0.135, std_factor=3)
            mouse_up_duration = generate_gaussian_random(1.4, 1.6, std_factor=3)
            print(
                f"Simulating click: Down for {mouse_down_duration:.3f} seconds, Up for {mouse_up_duration:.3f} seconds."
            )
            send_click_to_window(mouse_down_duration, mouse_up_duration)

        if is_right_holding:
            # Ensure the right mouse button is being held down
            win32api.PostMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, 0)
        else:
            # Ensure the right mouse button is released
            win32api.PostMessage(hwnd, win32con.WM_RBUTTONUP, None, 0)

        time.sleep(0.1)  # Adjust this sleep duration if needed


def generate_gaussian_random(
    min_value: float, max_value: float, std_factor: float = 6
) -> float:
    """
    Generates a Gaussian-distributed random float within the specified range.
    """
    mean = (min_value + max_value) / 2
    std_dev = (max_value - min_value) / std_factor
    return random.gauss(mean, std_dev)


def send_click_to_window(mouse_down_duration: float, mouse_up_duration: float) -> None:
    """
    Sends a simulated mouse click to the specified window.
    """
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    time.sleep(mouse_down_duration)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, None, 0)
    time.sleep(mouse_up_duration)


def toggle_left_click():
    global is_left_clicking
    if is_left_clicking:
        is_left_clicking = False
        print("Left mouse button clicking disabled.")
        winsound.Beep(300, 100)
    else:
        is_left_clicking = True
        print("Left mouse button clicking enabled.")
        winsound.Beep(600, 100)


def toggle_right_hold():
    global is_right_holding
    if is_right_holding:
        is_right_holding = False
        print("Right mouse button holding disabled.")
        winsound.Beep(300, 100)
    else:
        is_right_holding = True
        print("Right mouse button holding enabled.")
        winsound.Beep(600, 100)


if __name__ == "__main__":
    main()
