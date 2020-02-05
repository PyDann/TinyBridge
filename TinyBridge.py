#!/usr/bin/python3

import os
import sys
import time
import subprocess

#Config Options
sudo_opt  = True

#Terminal Colors
BLINK = "\33[5m"
END  = "\033[0m"
BLK  = "\33[30m"
RED  = "\33[91m"
GRN  = "\33[92m"
GRNBG = "\33[102m"
REDBG = "\33[41m"

menu = [
	"╭HomeBridge─x╮",
	"├────────────┤ ",
	"│ OPTION    │",
	"│ ["+RED+"L"+END+"]og      │",
	"│ ["+RED+"U"+END+"]pdate   │",
	"├────────────╯" +END
	]

def main():
	os.system("clear")
	if is_running():
		LED = (GRN + BLINK + "•" + END)
		OPTION = ("["+RED+"H"+END+"]alt ")
	else:
		LED = (RED + BLINK + "•" + END)
		OPTION = ("["+RED+"S"+END+"]tart")
	for row in menu:
		row = row.replace("x", LED)
		row = row.replace("OPTION", OPTION)
		print(row)
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
		if i in ["Q", "QUIT"]:
			os.system("clear")
			sys.exit()
		else:
			print("[" + RED + "Q" + END + "] to exit" + END)
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
	os.system("clear")
	if is_running():
		print("Already Running!")
		time.sleep(2)
		sys.exit()
	else:
		print("Starting...")
		if sudo_opt == True:
			start_cmd = ('sudo ' + start_cmd)
		subprocess.run([i for i in start_cmd.split(" ")])
		time.sleep(2)
		if is_running():
			print(GRNBG + BLK +  "Succesfull " + END)
		else:
			print(REDBG + BLK +  "Error      " + END)
			time.sleep(2)
			log()
		time.sleep(2)
		sys.exit()

def stop():
	halt_cmd = ("systemctl stop homebridge")
	os.system("clear")
	if is_running():
		print("Halting...    ")
		if sudo_opt:
			halt_cmd = ('sudo ' + halt_cmd)
		subprocess.run([i for i in halt_cmd.split(" ")])
		time.sleep(2)
		if is_running():
			print(REDBG + BLK +  "Error      " + END)
			time.sleep(2)
			log()
		else:
			print(GRNBG + BLK +  "Halted     " + END)
			time.sleep(2)
			sys.exit()
	else:
		print("Not Running!")
		time.sleep(2)
		sys.exit()

def log():
	log_cmd = ("journalctl -f -u homebridge")
	os.system("clear")
	print(BLINK + REDBG + "CTRL C to exit" + END)
	try:
		subprocess.run([i for i in log_cmd.split(" ")])
	except KeyboardInterrupt:
		main()

def update():
	if is_running():
		print("[" + RED + "H" + END + "]alt Before Updating" + END)
		time.sleep(2)
		main()
	plugins = (subprocess.check_output(["ls", "/usr/lib/node_modules/"]).splitlines())
	for (item, plugin) in enumerate(plugins):
		if ("homebridge") in str(plugin):
			plugin_update = ["npm", "update", "-g", plugin.decode("utf-8")]
			if sudo_opt:
				(plugin_update.insert(0, 'sudo'))
			plugin_name = (plugin.decode("utf-8"))
			plugin_name = (plugin_name.replace("homebridge-", ""))
			print(GRNBG + BLK + "Updating: " + plugin_name + END)
			subprocess.run(plugin_update)
	else:
			#Skipping This, Not A HomeBridge Plugin!
			pass
	print(GRNBG + BLK + "Updating: HomeBridge" + END)
	time.sleep(2)
	main()


if __name__ == "__main__":
	try:
		user_input(option = sys.argv[1])

	except IndexError:
		main()
