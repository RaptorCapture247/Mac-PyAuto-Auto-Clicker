# Mac PyAutoGUI Setup Instructions

## ⚠️ IMPORTANT WARNING ⚠️

**The PyAutoGUI script WILL click ALL pop-ups that match the screenshots you take for the ENTIRE monitor that are saved in the PyAutoGUI folder.**

**IF YOU ARE NOT USING IT FOR AUTO MINING/SWAPPING TURN IT OFF!!!!**

If you get stuck, tag and ping me in: https://discord.com/channels/1335026643214929952/1352139613539401760

## Resources

- **Mac Python Download**: https://www.python.org/downloads/release/python-3111/
- **Mac PyAutoGUI Instructions**: https://x.com/i/grok/share/R4LDUWywrP3jwDFTkIAIFNSab
- **Mac PyAutoGUI Script**: https://x.com/i/grok/share/dqNScbIuKwE2lPLgZgBTCf5NL
  (This is the script you will copy in step 4 of the instructions above. Scroll down until you see a box with colored text. That is what you copy.)

When you install Python, install 3.11.11 - I have added a link to the correct download page.

*This is not needed if you are using the Ez Mode extension.*

**Auto Clicker**: https://mahdi.jp/apps/autoclick

## Step 1: Install Python

*Skip if you are already running the previous PyAutoGUI script*

Your Mac doesn't come with the full Python setup we need, so let's install Python 3.11.1 from a specific link.

### Open your web browser:
- At the bottom of your screen in the Dock (the row of app icons), find Safari (a compass icon) or Chrome (a red-yellow-green circle) and click it.

### Go to the Python download page:
- In the address bar at the top, click, then type or paste this exact link:
  https://www.python.org/downloads/release/python-3111/
- Press Enter on your keyboard.

### Download Python 3.11.1:
- Scroll down the page until you see a section called "Files."
- Look for "macOS 64-bit universal2 installer" (it'll say something like `python-3.11.1-macos11.pkg`).
- Click that link to start the download.

### Open the downloaded file:
- After a few seconds, check the bottom of your browser or your Downloads folder:
  - In Safari, click the downward arrow in the top-right corner to see it.
  - In Chrome, look at the bottom bar or click the three dots (top-right) > "Downloads."
- The file will be named `python-3.11.1-macos11.pkg`. Double-click it.

### Run the installer:
- A window pops up. Click "Continue" (bottom-right) three times to move through the welcome screens.
- Click "Agree" when it asks about the license.
- Click "Install" (it might show space needed, like 50MB—that's fine).
- If it asks for your password, type the one you use to log into your Mac, then click "OK" or press Enter.
- Wait a minute—it'll say "Installing" with a progress bar. When it says "The installation was successful," click "Close."

## Step 2: Open Terminal

*Skip if you are already running the previous PyAutoGUI script*

Terminal is a tool where we'll type commands. It's easy—I'll guide you!

### Find Terminal:
- Click the Apple logo (🍎) in the top-left corner of your screen.
- Click "System Settings" or "System Preferences" (depending on your macOS version).
- OR, press Command (⌘) (the key with a cloverleaf next to the spacebar) + Space.

### Search for Terminal:
- A search bar (Spotlight) pops up. Type `Terminal`.
- When "Terminal" appears (a black box icon with white text), press Enter or click it.

### Understand Terminal:
- A black window opens with text like `yourname@Mac ~ %` or `$`. That's normal—it's ready for your commands.

## Step 3: Install PyAutoGUI

*Skip if you are already running the previous PyAutoGUI script*

The script needs PyAutoGUI to work. We'll add it using Terminal, and we'll upgrade a tool called pip too.

### Type the first command:
- In Terminal, type this exactly (copy-paste if you can):
```bash
pip3 install pyautogui
```
- Press Enter.

### Wait for it to finish:
- Text will scroll by—it's downloading and installing. This takes 1-2 minutes.
- When it's done, you might see a message saying "You should consider upgrading pip" with a command. Even if you don't, let's upgrade it now.

### Upgrade pip:
- Type this in Terminal and press Enter:
```bash
python3 -m pip install --upgrade pip
```
- Wait a minute—it'll update pip. You'll see text scroll by, and then it'll return to a `%` or `$` prompt.

### Add one more tool:
- Type this and press Enter:
```bash
pip3 install opencv-python
```
- Wait again (1-2 minutes). This helps the script "see" the Confirm button.

## Step 4: Get the Script

We need to grab the script from an online link, and we'll use the copy button for the one with colored text.

### Open the link:
- In your browser, go to this X conversation: https://x.com/i/grok/share/dqNScbIuKwE2lPLgZgBTCf5NL
- You'll see a conversation with some text and code.

### Copy the script with colored text:
- Look for a box of code that has colored text—it's the script we want. The text will have colors like:
  - `import` in purple
  - Words like `True` or `False` in orange
  - Numbers like `0.1` or `2` in green
  - Comments starting with `#` in gray
- At the top-right of this colored script box, you'll see a "Copy" button (it might look like a small clipboard icon or say "Copy").
- Click that "Copy" button—it'll copy the entire colored script for you automatically.

## Step 5: Create, Modify, and Save the Script and Prepare the Image

Now we'll create the script, update it with your username, save it, and set up the "Confirm" button image—all in one go.

### Open TextEdit:
- Press Command (⌘) + Space.
- Type `TextEdit` and press Enter. A blank white window opens.

### Paste the script:
- Click inside the TextEdit window, then press Command (⌘) + V to paste the script. (It'll lose the colors in TextEdit—that's okay!)

### Switch to plain text:
- In the top menu, click Format > Make Plain Text (if it says "Make Rich Text," skip this—it's already plain).

### Update the script with your username:
- Find the line that says: `BASE_DIR = "/Users/YourUsername/Pyautogui/"` (use the search: press Command (⌘) + F, type `YourUsername`, and press Enter).
- Replace `YourUsername` with your username:
  - To find your username, open Finder (the blue face icon in your Dock). In the sidebar on the left, look for your home folder—it's usually your name (e.g., "jane" for `/Users/jane`).

### Make a folder:
*This should be done if already running the previous PyAutoGUI script*

- Open Finder (the blue face icon in your Dock).
- In the sidebar on the left, click your username (e.g., "jane"—it's your home folder).
- If it does not appear, in Finder go to Finder > Preferences > Sidebar. Check the box next to your home folder to display it in the sidebar.
- Right-click (or two-finger tap) in the empty space, then click "New Folder."
- Name it `PyAutoGUI` and press Enter.

### Save the script in the folder:
- Back in TextEdit, click File > Save.
- In the "Save As" box, type `autoclicker2.py` (make sure it ends with `.py`).
- Where to save:
  - Click the little arrow next to "Save As" to expand the options.
  - In the sidebar, click your username, then double-click the `PyAutoGUI` folder.
  - Click "Save."
- If it asks about ".py," click "Use .py."

## Step 6: Take Screenshots

Now we will create and take a few screenshots of the Phantom popup windows.

Travel to Pond0x.com and perform a swap of SOL to wPOND. **DO NOT CONFIRM THE TRANSACTION**.

Once you have the popup on screen, using your keyboard press **Command (⌘) + Shift + 4**.

Take your cursor over to the popup, click and hold, then drag a box around the area seen in the image with this message.

If you see a popup to open the screenshot, do so.

If not, open your file explorer and go to your "Photos" and look for a folder titled "Screenshots". Right-click the icon and select "Open with" and select the Snipping Tool.

Once open, you can further crop the image to trim down excess borders not seen in the example image.

Click the save icon and travel to the PyAutoGUI folder we created in Step 4. Save the file as `confirm1.png`.

Check the folder to ensure the image is now saved there.

This step can be performed with any wallet that you are using.

**IMPORTANT NOTE**: Once this script is started, it will approve ANY and ALL popups that match your images. If you are not using the auto swapper, **TURN OFF THE SCRIPT!**

### Slippage Tolerance Screenshot

The next image we are going to grab will be off the slippage tolerance exceeded popup.

In order to force this image, we will adjust our slippage to Fixed and a value of 0.01% and use $SOL>USDC.

Once we do that, we can repeat the above actions. Cancel and retry until you see the image in this message. We will call this image `cancel1.png`.

### Mining Session Screenshot

Finally, we will now grab the popup for the xminer when we start a mining session.

Again, follow the steps at the beginning of this section to capture the screenshot except you will start a mining session and use the confirm popup that appears. You will want it to look like the example in this message.

We will call this `mine.png`.

### Additional Screenshots

Additionally, you will encounter other popups that are not listed here. You will want to grab screenshots of them and save them:

- The first image you will notice a `<` symbol in the network fee section. You will want to save this one as `confirm2.png`.
- The other is a "no balance found" error message. This one will need to be saved as `cancel2.png`.

These are both built into the script and after saving will be handled appropriately.

Any other popups that appear will cause the script to pause, making it easy to grab them. If you encounter one, and after grabbing the image and cropping to look similar to the other examples here, you can save it as either:

**If you want confirm clicked:**
- `confirm3.png`
- `confirm4.png`
- `confirm5.png`

**If you want cancel clicked:**
- `cancel3.png`
- `cancel4.png`
- `cancel5.png`

This gives you a little customization ability to help the script work for you. If you run out of image slots, then let us know and we can help you with adding more to the script.

## Step 7: Give Python Permission

*This should be done if already running the previous PyAutoGUI script*

macOS needs to allow Python to control your screen.

### Open System Settings:
- Click the Apple logo (🍎) in the top-left corner.
- Click "System Settings" (or "System Preferences" on older macOS).

### Go to Accessibility:
- Scroll down in the sidebar and click "Privacy & Security" (or "Security & Privacy").
- Click "Accessibility."

### Unlock it:
- At the bottom-left, click the lock icon.
- Type your Mac password and click "Unlock."

### Add Python:
- Click the `+` button below the list.
- A Finder window opens. Click "Applications" in the sidebar.
- Find "Python 3.11" (since we installed 3.11.1), click it, then select "Python.app" inside.
- Click "Open."
- Ensure "Python" is in the list and checked.

### Lock it back:
- Click the lock again to lock it.

## Step 8: Run the Script

Let's test it from the right folder!

### Go to the PyAutoGUI folder in Terminal:
- In Terminal, type:
```bash
cd ~/PyAutoGUI
```
- Press Enter. (This takes you to the PyAutoGUI folder you made in your home directory in Step 5.)

### Run it:
- Type:
```bash
python3 autoclicker2.py
```
- Press Enter.

### What you'll see:
```
Screen size: 1920x1080 pixels
Attempting to initialize Tkinter...
Tkinter initialized successfully.
Start button created
Stop button created
Starting Tkinter mainloop...
```

If so, then the script is running as intended and you should now have a control panel on screen.

The script will print error messages for the missing images. This is normal, as you encounter and save the popup images these will disappear.

If you receive any other error, copy the error and paste it into Grok or tag myself or Bearly and we will help you troubleshoot.

## Step 9: Create Command Cheat Sheet

Now we will create a command cheat sheet for you to reference when you need to start the autoswap script.

Open a new notepad document and paste the commands in the following message.

*If you are using the old PyAutoGUI script you will have two run commands now, `autoswap.py` and `autoswap2.py`. This is so if you do not get the newest one running immediately you can still revert back to and use the old one.*

### Commands:
```bash
cd ~/PyAutoGUI
python3 autoclicker2.py
```

Then save as, name it "cheat sheet", and put it into the PyAutoGUI folder or save it to your desktop for easy finding.

## Step 10: Fine-tune Coordinates

1. Minimize the command prompt window.
2. Bring back your Pond0x browser window and the new Autoclicker control panel.
3. On the new control panel, you will notice that there are two sections to adjust X and Y coordinates for the confirm offsets and the cancel offsets. These are the button locations.

Before you can run the auto clicker without worry, you will need to fine-tune these values to ensure it clicks accurately on each style button:

- Simply stop the clicker with the stop button
- Change the value in X for horizontal direction or Y for vertical direction
- Use small increments, probably no more than 5 at a time to get it just right
- **Do not run the extension while you are doing this**
- Simply manually process transactions through

To fine-tune the cancel button, apply the same settings as you did to force the popup you grabbed the image from in Step 6.

Once you have them set, return to your cheat sheet and record the confirm and cancel X,Y coordinates. You will need to re-enter these every time you restart the autoclicker program after you close the window.

## Congratulations!

You are now ready to press start and begin your automation journey.

### To end the Autoclicker program:
- Simply close the control panel window or close command prompt.

### To restart:
- Simply open command prompt and your cheat sheet
- Copy paste each command line into the terminal one at a time and hit enter after each
- Once the Autoclicker control panel is on screen, re-enter your saved coordinates from the cheat sheet and you're ready to press start

## ⚠️ FINAL REMINDER ⚠️

**The PyAutoGUI script WILL click ALL confirm images that match your screenshots for the ENTIRE monitor.**

**IF YOU ARE NOT USING IT FOR AUTO MINING/SWAPPING TURN IT OFF!!!!**

Here are all the images I currently have in use. Watch for new ones and be sure to grab them when you can. A quick way to grab them is to simply screenshot the entire screen and then crop the image to just the area needed within the popup.