![Screenshot](https://raw.githubusercontent.com/PyDann/TinyBridge/master/Screenshot.png)

# TinyBridge
## A Homebridge CLI Manager
This project is for quick and easy management of Homebridge installed via the **systemd** method. Providing both interaction through a menu like system or using *options* (`HomeBridge.py -s`).

### *Pre Install READ*
Depending on your install, updating Homebridge and plugins may require `sudo`, or advanced permissions. This is always important to be aware of and understand. By default TinyBridge does not have this enabled. To change this, open TinyBridge.py and modify Line 10: `sudo_opt = True`.


## To Run

`./HomeBridge.py -option`


## Features
**Start Homebridge:** `'s', 'start'`

**Halt Homebridge:** `'h', 'halt', 'stop'`

**View Log** `'l', 'log'`

**Update Homebridge & Plugins:** `'u', 'update'`

**Edit Config.json:** `'c', 'config'`

**Quit/Exit Menu:** `'q', 'quit'`


## Future Updates

\- Update individual plugins

\- Uninstall individual plugins

\- Remote control via ssh

\- Manage Homebridge installed under any method


## Recent Changes

### 2/21

\- Users can change default editor on line 11
