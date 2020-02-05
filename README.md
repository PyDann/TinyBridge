![Screenshot](https://raw.githubusercontent.com/PyDann/TinyBridge/master/Screenshot.png)

# TinyBridge
## A Homebridge CLI Manager
This project is for quick and easy management of Homebridge installed via the **systemd** method. Providing both interaction through a menu like system or using *options* (ex `HomeBridge.py -s`). 

### *Pre Install READ*
Depending on your install, updating Homebridge and plugins may require `sudo`, or advanced permissions. This is always important to be aware of and understand. By default TinyBridge does not have this enabled. To change this, open TinyBridge.py and modify `sudo = True`.


## To Run
>Set the script to executable: `sudo chmod +x HomeBridge.py`

`./HomeBridge.py -option`

or

`python3 HomeBridge.py -option`


## Features
**Start Homebridge:** `'s', 'start'`

**Halt Homebridge:** `'h', 'halt', 'stop'`

**View Log** `'l', 'log'`

**Update Plugins:** `'u', 'update'`

- updates all installed plugins & Homebridge itself

**Quit/Exit Menu:** `'q', 'quit'`


## Future Updates

\- Update individual plugins

\- Uninstall individual plugins

\- Remote control via ssh

\- Manage Homebridge installed under any method