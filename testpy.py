import os, winshell, win32com.client

desktop = winshell.desktop()
#desktop = r"path to where you wanna put your .lnk file"

path = os.path.join(desktop, 'File Shortcut Demo.lnk')
target = r"C:/Users/techm/AppData/Local/AmeyBot/__init__.py"
icon = r"C:/Users/techm/AppData/Local/AmeyBot/__init__.py"

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()