# WiFi-Backup
Cross Platform python script for backing up saved WiFi Keys on MacOS, Windows and Linux.

Runs out of box on both Linux and MacOS. Requires either python 2 or python 3 on Windows to run.

File Name:	getWifiKeys.vbs, WiFi-Backup.py  
Authors:	Seinu
Purpose:	Backup WiFi Keys from MacOS, Windows and Linux  
History:  
*	01/26/2015 - v1.0	Initial creation of the script in vbscript by Seinu
*	02/05/2015 - v1.1	by Hackoo
*	02/xx/2015 - v1.2	Both scripts merged
*	10/01/2016 - v1.3a	v1.2 rewrite doto losing script
*	10/05/2016 - v1.3b	changed admin code added Option Explicit
*	10/05/2016 - v1.3c	updated to camelcase
*	11/20/2018 - v2.0a	completely rewrote script in python with multiplatform support
		for both Windows and MacOS
*	11/20/2018 - v2.0b	Added Linux support via NetworkManager
*	05/07/2019 - v2.1  Fixed errors after testing on my high Sierra Hackintosh,
		Original testing was on a Sierra Virtual Machine
		added a check for the package networkmanager
		changed some windows code
		
	TODO: Test on Proper Mac  
	TODO: Linux Update with wider distro and package support
