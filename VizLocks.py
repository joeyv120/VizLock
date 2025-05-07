"""Visual indicator of active keyboard lock state

Author: Joe Vinciguerra
Date: 2025.05.07

This program provides a visual indication of the active CAPS and NUM lock
states by adding a Windows system tray icon.

"""

from infi.systray import SysTrayIcon as sti
import ctypes
from time import sleep
import sys

hllDll = ctypes.WinDLL("User32.dll")

icons = {
    "default": ".\\data\\default.ico",
    "C0N0": ".\\data\\C0N0.ico",
    "C0N1": ".\\data\\C0N1.ico",
    "C1N0": ".\\data\\C1N0.ico",
    "C1N1": ".\\data\\C1N1.ico",
}


systray = sti(
    icon=icons["default"],
    hover_text="Key Locks",
)

systray.start()


def change_locks(lock_states_new):
    if lock_states_new["CAP"] != 0:
        c = "C1"
    else:
        c = "C0"
    if lock_states_new["NUM"] != 0:
        n = "N1"
    else:
        n = "N0"
    k = c + n
    systray.update(icon=icons[k])


def check_locks():
    lock_keys = {
        "CAP": 0x14,
        "NUM": 0x90,
        # 'VK_SCROLL': 0x91,
    }
    lock_states = {k: hllDll.GetKeyState(v) for k, v in lock_keys.items()}
    return lock_states


lock_states_old = None
while True:  # The event loop
    lock_states_new = check_locks()
    if lock_states_new != lock_states_old:
        change_locks(lock_states_new)
        lock_states_old = lock_states_new
    sleep(0.1)
