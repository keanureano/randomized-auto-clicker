# Randomized Auto Clicker

This tool simulates mouse actions, with the ability to click and hold mouse buttons, and control these actions using hotkeys. The application is distributed as a standalone executable.

## Features

- **Left Mouse Button Clicking**: Simulates mouse clicking with adjustable durations.
- **Right Mouse Button Holding**: Toggles the right mouse button hold.
- **Hotkeys**: Use arrow keys to toggle actions.
- **Sound Alerts**: Provides audio feedback when toggling actions.

## Installation

No installation is needed if you are using the pre-built executable.

## Usage

1. **Run the Executable**:

   - Navigate to the `/dist` directory where the executable (`.exe`) file is located.
   - Double-click on the executable file to run it.

2. **Control the Script**:

   - **Left Arrow Key**: Toggle left mouse button clicking on or off.
   - **Right Arrow Key**: Toggle right mouse button holding on or off.

3. **Observe the Output**:

   - The script provides status updates via console output.
   - Audio feedback is given using the `winsound` library when toggling actions.

4. **Stop the Script**:
   - Press `ESC` to exit the application.

## Code Explanation

- **`main()`**: Sets up hotkeys and starts the main loop for mouse actions.
- **`generate_gaussian_random()`**: Generates random durations for mouse actions based on a Gaussian distribution.
- **`click_with_delay()`**: Simulates a mouse click with a specified hold duration and delay between clicks.
- **`toggle_left_click()`**: Toggles the left mouse button clicking.
- **`toggle_right_hold()`**: Toggles the right mouse button holding.

## Troubleshooting

- **Permission Issues**: Ensure you have the necessary permissions to run the executable.
- **Functionality Issues**: Verify that your system meets the requirements for running the script.
