#!/usr/bin/python3

import os
import sys
import time
import subprocess

#################
## C O N F I G ##
use_sudo = False
#################

class Term_Colors():
    BLINK = "\33[5m"
    END = "\033[0m"
    BLACK = "\33[30m"
    RED = "\33[91m"
    GREEN = "\33[92m"
    GREENBG = "\33[102m"
    REDBG = "\33[41m"

class Menu():
    def __init__(self, title, status, options):
        self.title = title
        self.status = status
        self.options = options
        self.keys = []
        for option in options:
            key = option[0:1]
            if key not in self.keys:
                self.keys.append(key)
            else:
                raise ValueError("All Menu Options Must Start With A Different Letter!")
        self.menu_constructor()

    def display(self):
        for item in self.built:
            print(item)

    def title_build(self):
        title_bar = ("╭TITLE")
        title_bar = title_bar.replace("TITLE", self.title)
        while len(title_bar) < 12:
            title_bar += ("─")
        if self.status:
            LED = (Term_Colors.GREEN + "•")
        if not self.status:
            LED = (Term_Colors.RED + "•")
        title_end = (Term_Colors.BLINK + LED + Term_Colors.END + "╮" )
        title_bar += title_end
        return(title_bar)

    def menu_constructor(self):
        if len(self.title) > 12:
                raise ValueError("Title Too Long -> {0}" .format(option))
        built = [self.title_build()]
        built.append(self.line_break_build())
        for option in self.options:
            if len(option) > 12:
                raise ValueError("One Or More Items Name Too Long -> {0}" .format(option))
            built.append(self.menu_item_build(option))
        built.append(self.bottom_row_build())
        self.built = built

    def line_break_build(self):
        return("├────────────┤")

    def empty_row_build(self):
        return("│            │")

    def bottom_row_build(self):
        return("├────────────╯")

    def menu_item_build(self, option):
        menu_item = ("│ OPTION")
        option = "[" + Term_Colors.GREEN + option[0:1] + Term_Colors.END + "]" + option[1:]
        menu_option = ("│ {0}" .format(option))
        while len(menu_option) < 22:
            menu_option += (" ")
        menu_option += ("│")
        return(menu_option)


def main():
    title = "TinyBridge"
    status = is_running()
    if status:
        options = ["Halt", "Log", "Update", "Config"]
    if not status:
        options = ["Start", "Log", "Update", "Config"]
    os.system('clear')
    MainMenu = Menu(title = title, status = status, options = options)
    MainMenu.display()
    user_input()

def user_input(option = None):
    try:
        if option:
            i = option.upper()
        else:
            i = input("> ").upper()
        if i in ["S", "-S", "START"]:
            start()
        if i in ["H", "-H", "HALT", "STOP"]:
            stop()
        if i in ["L", "-L", "LOG"]:
            log()
        if i in ["U", "-U", "UPDATE"]:
            update()
        if i in ["C", "-C", "CONFIG"]:
            edit()
        if i in ["Q", "QUIT"]:
            os.system("clear")
            sys.exit()
        else:
            print("[" + Term_Colors.RED + "Q" + Term_Colors.END + "] to exit" + Term_Colors.END)
            time.sleep(2)
            main()
    except KeyboardInterrupt:
        os.system("clear")
        sys.exit()

def is_running():
    process = ("homebridge")
    processes = (os.popen("ps -Af").read())
    if process in processes:
        status = True
    else:
        status = False
    return(status)

def start():
	start_cmd = ("systemctl start homebridge")
	if is_running():
		print("Already Running!")
		time.sleep(2)
		sys.exit()
	else:
		print("Starting...")
		if use_sudo == True:
			start_cmd = ('sudo ' + start_cmd)
		subprocess.run([i for i in start_cmd.split(" ")])
		time.sleep(2)
		if is_running():
			print(Term_Colors.GREENBG + Term_Colors.BLACK +  "Succesfull " + Term_Colors.END)
		else:
			print(Term_Colors.REDBG + Term_Colors.BLACK +  "Error      " + Term_Colors.END)
			time.sleep(2)
			log()
		time.sleep(2)
		sys.exit()

def stop():
	halt_cmd = ("systemctl stop homebridge")
	if is_running():
		print("Halting...    ")
		if use_sudo:
			halt_cmd = ('sudo ' + halt_cmd)
		subprocess.run([i for i in halt_cmd.split(" ")])
		time.sleep(2)
		if is_running():
			print(Term_Colors.REDBG + Term_Colors.BLACK +  "Error      " + Term_Colors.END)
			time.sleep(2)
			log()
		else:
			print(Term_Colors.GREENBG + Term_Colors.BLACK +  "Halted     " + Term_Colors.END)
			time.sleep(2)
			sys.exit()
	else:
		print("Not Running!")
		time.sleep(2)
		sys.exit()

def log():
	log_cmd = ("journalctl -f -u homebridge")
	os.system("clear")
	print(Term_Colors.BLINK + Term_Colors.REDBG + "CTRL C to exit" + Term_Colors.END)
	try:
		subprocess.run([i for i in log_cmd.split(" ")])
	except KeyboardInterrupt:
		main()

def update():
	if is_running():
		print("[" + Term_Colors.RED + "H" + Term_Colors.END + "]alt Before Updating" + Term_Colors.END)
		time.sleep(2)
		main()
	plugins = (subprocess.check_output(["ls", "/usr/lib/node_modules/"]).splitlines())
	for (item, plugin) in enumerate(plugins):
		if ("homebridge") in str(plugin):
			plugin_update = ["npm", "update", "-g", plugin.decode("utf-8")]
			if use_sudo:
				(plugin_update.insert(0, 'sudo'))
			plugin_name = (plugin.decode("utf-8"))
			plugin_name = (plugin_name.replace("homebridge-", ""))
			print(Term_Colors.GREENBG + Term_Colors.BLACK + "Updating: " + plugin_name + Term_Colors.END)
			subprocess.run(plugin_update)
	else:
			#Skipping This, Not A HomeBridge Plugin!
			pass
	print(Term_Colors.GREENBG + Term_Colors.BLACK + "Updating: HomeBridge" + Term_Colors.END)
	time.sleep(2)
	main()

def edit():
    subprocess.run(["nano", "/var/homebridge/config.json"])
    main()

if __name__ == "__main__":
	try:
		user_input(option = sys.argv[1])

	except IndexError:
		main()
