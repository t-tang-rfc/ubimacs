# OS-wide Emacs/macOS keymapping for Ubuntu.

This configuration remaps keys in a way that is consistent with Emacs and macOS keybindings, making it easier for users familiar with those environments to work in Ubuntu.

## Prerequisites

Requires `python3-evdev` package.
Note, if you are using Ubuntu 24.04, you will need to install it via `apt` instead of `pip`.

## Setup for /dev/uinput Access

This program requires write access to `/dev/uinput` to create virtual input devices and inject key events. By default, this device is only accessible by root.

### Step 1: Add your user to the input group
```bash
sudo usermod -a -G input $USER
```

After running this command, you need to log out and log back in (or start a new shell session) for the group membership to take effect.

### Step 2: Set permissions on /dev/uinput (Temporary Method)
```bash
sudo chgrp input /dev/uinput
sudo chmod 660 /dev/uinput
```

**WARNING:** This method is temporary and will be reset after each reboot because `/dev` is mounted as a tmpfs (temporary filesystem). The device files are recreated by udev on boot with default permissions.

### Step 3: Make permissions persistent (Recommended)
To make the permissions persistent across reboots, create a udev rule:
```bash
echo 'KERNEL=="uinput", GROUP="input", MODE="0660"' | sudo tee /etc/udev/rules.d/99-uinput.rules
```

Then reload udev rules:
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Security Considerations

Access to `/dev/uinput` allows programs to simulate keyboard and mouse input system-wide. Only grant this access to users and programs you trust, as malicious software could potentially:
- Log keystrokes
- Simulate malicious key combinations
- Interfere with system operation

## Usage

Once the setup is complete, run the program with:
```bash
python3 pykeymacs.py
```

The program will display a list of available input devices and prompt you to select which device to monitor for key remapping.
