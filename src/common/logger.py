from datetime import datetime

print("i will be a logger someday")

def getDate():
	# datetime object containing current date and time
	now = datetime.now()
#	return now.strftime("%d/%m/%Y %H:%M:%S")
	return now.strftime("%Y-%m-%d %H:%M:%S.{0}".format(now.microsecond))

def info(message = ""):
	print("\x1b[0;32m{0}\x1b[0;37m info: {1}\x1b[0m".format(getDate(), message))

def warning(message = ""):
	print("\x1b[0;32m{0}\x1b[0;33m warning: \x1b[0;37m{1}\x1b[0m".format(getDate(), message))

def error(message = ""):
	print("\x1b[0;32m{0}\x1b[0;31m error: \x1b[0;37m{1}\x1b[0m".format(getDate(), message))
