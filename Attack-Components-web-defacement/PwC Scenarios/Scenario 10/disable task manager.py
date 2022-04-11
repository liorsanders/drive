import ctypes
import sys
import os

# check privileges
if os.name == 'nt':
	if not ctypes.windll.shell32.IsUserAnAdmin():
		print('\nThis script requires to be ran with admin privileges\n')
		sys.exit()

# import the right version
if sys.version[0] == '2':
	input = raw_input
	import _winreg as wreg
else:
	import winreg as wreg


def Disable():
	key = wreg.CreateKey(wreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
	wreg.SetValueEx(key, 'DisableTaskMgr', 0, wreg.REG_SZ, '1')
	wreg.CloseKey(key)


def Enable():
	key = wreg.CreateKey(wreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
	wreg.DeleteValue(key, 'DisableTaskMgr')
	wreg.CloseKey(key)

Enable()

# usage: run change the code to run disable or enable
# requires admin privileges
