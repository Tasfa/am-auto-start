#-*-encoding:utf-8-*-
#   
#   Name:       am-start
#   Author:     tasfa
#   Info:       www.tasfa.cn
#   Version:    1.0


import os
import sys

def amstart(apk_p):
	"""
	Try to auto am start !
	"""	
	apk = apk_p

	global index_start
	index_start=0
	global index_end
	index_end=6
	global index_end_2
	index_end_2=''

	pkgname =  os.popen('aapt dump badging '+apk+' | findstr "package"').readlines()
	pkgname = pkgname[0]

	for i in xrange(len(pkgname)):
		if  pkgname[i:i+4]=='name':
			index_start= i+6
			for x in xrange(index_start,len(pkgname)):
				if pkgname[x]=="'":
					index_end= x
					break
	pkgname=pkgname[index_start:index_end]


	activity =  os.popen('aapt dump badging '+apk+' | findstr "launchable-activity"').readlines()
	activity = activity[0]
	

	for i in xrange(len(activity)):
		if  activity[i:i+4]=='name':
			index_start= i+6
			for x in xrange(index_start,len(activity)):
				if activity[x]=="'":
					index_end = x
					for y in xrange(index_end,0,-1):
						if activity[y]==".":
							index_start = y
							break
					break

	activity=activity[index_start:index_end]

	am_name = pkgname+"/"+activity
	print "am_name: "+am_name

	try:
		rel = os.system("adb shell am start -D -n "+am_name)
		if rel != 0:
			print "Please check the packge whether it has been installed!"
			print "Please check your phone whether it has been connected!"
		else:
			print ""
			print "**********************"
			print "Start Successfully!!!"
			print "**********************"
	except Exception as e:
		print "Please check your path (without Chinese)!"
		print "Please check your phone whether it has been connected!"
	

def banner():
    """
        Print the banner and Version Info
    """
    print """ 
     _____          __       
    |_   _|_ _ ___ / _| __ _ 
      | |/ _` / __| |_ / _` |
      | | (_| \__ \  _| (_| |
      |_|\__,_|___/_|  \__,_|
                             
    """
    print "Welcome to use am-auto-start!"
    print "For more infomation --> www.tasfa.cn!!"
    print "<--------------------------------------------------->"

def main():
	banner()
	if len(sys.argv) == 2:
		apk = sys.argv[1]
		amstart(apk)
	else:
		print "Usage: python am-start.py apkname "


if __name__ == '__main__':
	main()