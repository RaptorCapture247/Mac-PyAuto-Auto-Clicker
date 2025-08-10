# Mac-PyAuto-Auto-Clicker
Use this script for automating clicks on a MacOS. Script is setup for wallet confirmations or cancels depending on users saved screenshots. 

Images in this repository will not work for your setup and are intended for example and reference purposes only. You must take your own screenshots using your main monitor (must be monitor 1 in multi monitor setups).

# PyAutoGUI Pond0x Automation Script

## Overview

This PyAutoGUI automation script was specifically designed for **Pond0x crypto swapping and starting the crypto miner**. It automatically detects and clicks on various popup windows that appear during cryptocurrency transactions and mining operations, eliminating the need for manual intervention.

## Purpose and Functionality

### Primary Use Case: Pond0x Operations
- **Automated Transaction Confirmations**: Automatically confirms swap transactions between cryptocurrencies (e.g., SOL to wPOND)
- **Mining Session Management**: Automatically starts and manages crypto mining sessions
- **Error Handling**: Manages common errors like slippage tolerance exceeded, network fee notifications, and insufficient balance warnings
- **Multi-popup Support**: Handles various popup types with customizable confirm/cancel actions

### How It Works
1. **Image Recognition**: Uses OpenCV and PyAutoGUI to scan the screen for predefined popup images
2. **Smart Clicking**: Automatically clicks the appropriate button (Confirm or Cancel) based on popup type
3. **Offset Calibration**: Uses adjustable X/Y offsets to ensure accurate button clicking
4. **Real-time Monitoring**: Continuously scans the screen for new popups
5. **GUI Control Panel**: Provides a user-friendly interface for starting/stopping and adjusting settings

## Key Features

- **Multiple Image Support**: Handles up to 11 different popup types simultaneously
- **Retina Display Compatible**: Includes scaling adjustments for high-DPI displays
- **Safety Features**: Built-in fail-safe (move mouse to upper-left to abort)
- **Error Recovery**: Continues operation even when individual images can't be found
- **Customizable Offsets**: Fine-tune click positions for different popup layouts
- **Real-time Feedback**: Console logging shows detection and click activities

## System Requirements

- **Operating System**: macOS 
- **Python**: 3.11.1 or higher
- **Dependencies**:
  - `pyautogui` - Screen automation and image recognition
  - `opencv-python` - Enhanced image processing capabilities
  - `tkinter` - GUI control panel (included with Python)

## File Structure

```
~/PyAutoGUI/
├── autoclicker2.py          # Main script file
├── mine.png                 # Mining confirmation popup
├── confirm1.png             # Primary transaction confirmation
├── confirm2.png             # Network fee confirmation
├── confirm3.png             # Additional confirmation popup
├── confirm4.png             # Additional confirmation popup  
├── confirm5.png             # Additional confirmation popup
├── cancel1.png              # Slippage error popup
├── cancel2.png              # Balance insufficient popup
├── cancel3.png              # Additional cancel popup
├── cancel4.png              # Additional cancel popup
└── cancel5.png              # Additional cancel popup
```

## Security and Safety

### Built-in Safety Features
- **Fail-safe Mechanism**: Move mouse to screen corner to immediately stop
- **Screen Bounds Checking**: Prevents clicking outside visible screen area
- **Error Handling**: Graceful handling of image loading and detection failures
- **Manual Override**: GUI stop button for immediate termination

### Important Security Notes
⚠️ **WARNING**: This script will automatically click on ANY popup that matches your saved screenshots across your entire monitor. Only use when actively performing Pond0x operations.

## Configuration

### Essential Setup
1. **Username Path**: Update `BASE_DIR` variable with your actual username:
   ```python
   BASE_DIR = "/Users/YourUsername/Pyautogui/"
   ```

2. **Image Capture**: Take screenshots of actual wallet popups you encounter during Pond0x use
3. **Offset Calibration**: Adjust button click positions using the GUI control panel

### Advanced Configuration
- **Confidence Level**: Adjust image recognition sensitivity (default: 0.9)
- **Scan Delay**: Modify scanning frequency (default: 0.2 seconds)
- **Click Delay**: Adjust pause after clicking (default: 2 seconds)
- **Retina Scaling**: Configure for different display types

## Other Potential Use Cases

While designed specifically for Pond0x, this script framework can be adapted for other automation scenarios:

### General Applications
- **Web Application Testing**: Automate clicking through web app workflows
- **Game Automation**: Handle repetitive clicking in browser or desktop games  
- **Software Installation**: Automate installer wizards and license agreements
- **Data Entry Tasks**: Speed up forms that require frequent confirmations
- **System Maintenance**: Automate routine popup dismissals during updates

### DeFi and Crypto Applications
- **Multi-DEX Trading**: Adapt for other decentralized exchanges
- **Yield Farming**: Automate reward claiming across multiple platforms
- **NFT Minting**: Handle high-frequency minting operations
- **Liquidity Pool Management**: Automate LP token staking/unstaking
- **Cross-chain Bridging**: Manage bridge transaction confirmations

### Business Process Automation
- **Batch Processing**: Handle confirmation dialogs in data processing workflows
- **Report Generation**: Automate report export confirmations
- **Email Marketing**: Handle bulk sending confirmations
- **Customer Support**: Automate ticket system interactions

### Development and Testing
- **QA Testing**: Automated UI testing for popup-heavy applications
- **Deployment Automation**: Handle deployment confirmation dialogs
- **Database Operations**: Automate backup/restore confirmations
- **Server Management**: Handle system administration prompts

## Customization Guidelines

### Adding New Popup Types
1. **Capture Screenshot**: Use macOS screenshot tool (Cmd+Shift+4)
2. **Crop Image**: Remove excess borders, focus on popup content
3. **Save with Convention**: Use `confirm#.png` or `cancel#.png` naming
4. **Update Script**: Add new image to `IMAGE_CONDITIONS` array if needed

### Modifying Click Behavior
```python
# Example: Add new popup type
{"name": "newpopup.png", "action": "confirm"}  # or "cancel"
```

### Adjusting Performance
```python
# Scan frequency (lower = faster, higher CPU usage)
time.sleep(0.2)  # Current setting

# Image recognition sensitivity
confidence=0.9   # Range: 0.1 to 1.0
```

## Troubleshooting

### Common Issues
- **Permission Denied**: Enable Accessibility and Screen Recording in macOS System Preferences
- **Images Not Found**: Verify screenshot quality and file paths
- **Wrong Click Positions**: Recalibrate offsets using GUI control panel
- **High CPU Usage**: Increase scan delay interval

### Performance Optimization
- Use smaller, focused screenshots for faster recognition
- Adjust confidence levels based on screen clarity
- Fine-tune scan intervals based on popup frequency
- Monitor system resources during extended operation

## Contributing

To extend functionality or fix issues:
1. Test changes with non-production popups first
2. Maintain backward compatibility with existing image files
3. Document any new configuration requirements
4. Consider security implications of automated clicking

## License and Disclaimer

This script is provided for educational and automation purposes. Users are responsible for:
- Ensuring compliance with terms of service of automated platforms
- Understanding security implications of automated clicking
- Proper testing before production use
- Monitoring script behavior during operation

**Use at your own risk. The script will click on matching popups across your entire screen.**
