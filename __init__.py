from os import path as opath, listdir
from sys import path as spath
for path in listdir("."):
	if opath.isdir(path):
		spath.append(opath.abspath(path))
from AmeyBot import mainGui
from os import system
from colorama import init
system("cls")
init()
mainGui()
