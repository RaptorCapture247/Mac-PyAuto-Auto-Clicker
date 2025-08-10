import pyautogui
import time

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Move mouse to upper-left corner to abort
pyautogui.PAUSE = 0.1  # Add a small pause between actions for stability

# Print screen size for debugging
screen_width, screen_height = pyautogui.size()
print(f"Screen size (logical): {screen_width}x{screen_height} pixels")

# Adjust for Retina scaling (set to 1 if not using a Retina display)
RETINA_SCALING_FACTOR = 2  # Confirmed correct by user

# Base directory for images (corrected case sensitivity)
BASE_DIR = "/Users/YourUsername/Pyautogui/"

# Define image conditions: (image_name, action)
IMAGE_CONDITIONS = [
    {"name": "mine.png", "action": "confirm"},
    {"name": "confirm1.png", "action": "confirm"},
    {"name": "confirm2.png", "action": "confirm"},
    {"name": "cancel1.png", "action": "cancel"},
    {"name": "cancel2.png", "action": "cancel"},
    {"name": "confirm3.png", "action": "confirm"},
    {"name": "confirm4.png", "action": "confirm"},
    {"name": "confirm5.png", "action": "confirm"},
    {"name": "cancel3.png", "action": "cancel"},
    {"name": "cancel4.png", "action": "cancel"},
    {"name": "cancel5.png", "action": "cancel"}
]


# Approximate offset for buttons relative to the center of the pop-up image
CONFIRM_OFFSET_X = 100  # Pixels to the right of the pop-up center
CONFIRM_OFFSET_Y = 125   # Pixels below the pop-up center
CANCEL_OFFSET_X = -100  # Pixels to the left of the pop-up center
CANCEL_OFFSET_Y = 125    # Pixels below the pop-up center

# Infinite loop to monitor for the specified images
while True:
    try:
        found = False
        for condition in IMAGE_CONDITIONS:
            image_path = BASE_DIR + condition["name"]
            action = condition["action"]

            # Try to locate the image
            try:
                location = pyautogui.locateCenterOnScreen(
                    image_path,
                    confidence=0.9
                )
            except Exception as e:
                print(f"Error loading image {image_path}: {str(e)}")
                continue

            if location:
                found = True
                x, y = location

                # Adjust for Retina scaling
                adjusted_x = int(x / RETINA_SCALING_FACTOR)
                adjusted_y = int(y / RETINA_SCALING_FACTOR)

                # Determine button position based on action
                if action == "confirm":
                    button_x = adjusted_x + CONFIRM_OFFSET_X
                    adjusted_y = adjusted_y + CONFIRM_OFFSET_Y
                    button_position = (button_x, adjusted_y)
                    button_name = "Confirm"
                else:  # action == "cancel"
                    button_x = adjusted_x + CANCEL_OFFSET_X
                    adjusted_y = adjusted_y + CANCEL_OFFSET_Y
                    button_position = (button_x, adjusted_y)
                    button_name = "Cancel"

                # Check if the coordinates are within screen bounds
                if (button_x < 0 or button_x >= screen_width or 
                    adjusted_y < 0 or adjusted_y >= screen_height):
                    print(f"{button_name} coordinates ({button_x}, {adjusted_y}) are off-screen!")
                    continue

                print(f"Found {condition['name']} at (adjusted): ({adjusted_x}, {adjusted_y})")
                print(f"Clicking {button_name} button at: {button_position}")
                pyautogui.doubleClick(button_position)
                print

                print(f"Clicked {button_name} button at {button_position}")
                time.sleep(2)  # Wait after clicking to avoid rapid re-detection
                break  # Exit the loop after handling one image

        if not found:
            print("No target pop-up found - waiting...")

    except pyautogui.FailSafeException:
        print("Fail-safe triggered - exiting...")
        break

    except Exception as e:
        print(f"Unexpected error: {str(e)} - continuing...")

    time.sleep(0.2)  # Small delay to prevent excessive CPU usage