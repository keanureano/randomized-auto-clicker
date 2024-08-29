import pyautogui
import time
import random
import keyboard
import winsound

# Global variable to control the running state
is_left_clicking = True
is_right_holding = True


def main():
    keyboard.add_hotkey("left", toggle_left_click)
    keyboard.add_hotkey("right", toggle_right_hold)
    toggle_left_click()
    toggle_right_hold()

    while True:
        if is_left_clicking:
            mouse_down_duration = generate_gaussian_random(0.085, 0.135, std_factor=3)
            mouse_up_duration = generate_gaussian_random(1.4, 1.6, std_factor=3)
            print(
                f"Mouse click duration: Down for {mouse_down_duration:.3f} seconds, Up for {mouse_up_duration:.3f} seconds"
            )
            click_with_delay(mouse_down_duration, mouse_up_duration)
        else:
            # Sleep briefly to avoid high CPU usage while paused
            time.sleep(1)


def generate_gaussian_random(
    min_value: float, max_value: float, std_factor: float = 6
) -> float:
    """
    Generates a Gaussian (normally distributed) random float around the min_value and max_value range.
    The mean is set to the midpoint of the range, and the standard deviation is controlled by the std_factor.
    This allows for occasional values outside the min/max range, simulating human variability, including long rests.
    """
    mean = (min_value + max_value) / 2
    std_dev = (max_value - min_value) / std_factor
    return random.gauss(mean, std_dev)


def click_with_delay(mouse_down_duration: float, mouse_up_duration: float) -> None:
    """
    Simulates a mouse click with a specified hold duration and delay between clicks.
    """
    pyautogui.mouseDown()
    time.sleep(mouse_down_duration)
    pyautogui.mouseUp()
    time.sleep(mouse_up_duration)


def toggle_left_click():
    global is_left_clicking
    if is_left_clicking:
        is_left_clicking = False
        print("Left mouse button is NOT clicking.")
        winsound.Beep(300, 100)
    else:
        is_left_clicking = True
        print("Left mouse button is clicking.")
        winsound.Beep(600, 100)


def toggle_right_hold():
    global is_right_holding
    if is_right_holding:
        pyautogui.mouseUp(button="right")
        is_right_holding = False
        print("Right mouse button is NOT holding.")
        winsound.Beep(300, 100)
    else:
        pyautogui.mouseDown(button="right")
        is_right_holding = True
        print("Right mouse button is holding.")
        winsound.Beep(600, 100)


if __name__ == "__main__":
    main()
