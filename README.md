# VizLock
This program provides a visual indication of the active CAPS and NUM lock states by adding a Windows system tray icon.

## Usage

1. Downlaod and unzip VizLock.zip
2. Run VizLock.exe
3. An icon is added to the system tray
4. Watch the icon change with the CAPS and NUM lock status.

## Icons

The icon names are hardcoded, but the icons can be changed if maintaining the naming convention. Icons are located in the /data folder.

The program looks for an ICO file named for the combined CAP and NUM lock state. For example, if CAP is on and NUM is off it will activate the file named C1N0.ico, while if CAP is off and NUM is on it will activate the file named C0N1.ico. These ICO files can be changed, as long as this file naming scheme is followed.
