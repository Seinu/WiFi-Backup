#*****************************************************************************'
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#*****************************************************************************'
#   File Name:	getWifiKeys.vbs, WiFi-Backup.py
#   Authors:	Hackoo & Seinu
#   Purpose:	Backup WiFi Keys from MacOS, Windows and Linux 
#   History:
#       01/26/2015 - v1.0	Initial creation of the script in vbscript by Seinu
#       02/05/2015 - v1.1	Hackoo shared his version of the same script
#       02/xx/2015 - v1.2	Both scripts merged
#       10/01/2016 - v1.3a	v1.2 rewrite doto losing script
#       10/05/2016 - v1.3b	changed admin code added Option Explicit
#       10/05/2016 - v1.3c	updated to camelcase
#       11/20/2018 - v2.0a  updated script to python with multiplatform support
#                               for both Windows and MacOS
#       11/20/2018 - v2.0b  added Linux support
#
#*****************************************************************************'
import subprocess, platform, re, ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if platform.system() == 'Darwin':
    objFile = open("./WiFi_List.txt", "a+")
    SSID_List = subprocess.check_output("defaults read /Library/Preferences/SystemConfiguration/com.apple.airport.preferences | grep SSIDString", shell=True)
    SSID = re.findall(r'\"(.+?)\"',SSID_List)
    for x in range(0, len(SSID) - 1):
        objFile.write(SSID[x] + ":\n\t")
        password = subprocess.check_output("security find-generic-password -wga \"" + SSID[x] + "\"", shell=True)
        objFile.write(password + "")
        objFile.write("******************************************************************\n")
        objFile.close()

elif platform.system() == 'Windows':
    if is_admin():
        SSID_List = subprocess.check_output("netsh wlan show all > .\\WiFi.txt", shell=True)
        objFile = open("C:\\WiFi.txt", "r")
        strContent = objFile.read()
        objFile.close()
        SSID = re.findall(r'(?<=SSID name              : )\".+\"', strContent)
        objFile = open(".\\WiFi_List.txt", "a+")
        for x in range(0, len(SSID) - 1):
            objFile.write(SSID[x] + ":\n\t")
            password = subprocess.check_output("netsh wlan show profiles name="  + SSID[x] + " key=clear | Findstr /i ""Conten""", shell=True)
            objFile.write(password.decode("utf-8") + "\n")
            objFile.write("******************************************************************\n")
        objFile.close()
    else:
        if sys.version_info<(3,0,0):
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
        elif sys.version_info>(3,0,0):
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

elif platform.system() == 'Linux':
    WiFi_List = subprocess.check_output("sudo grep psk= /etc/NetworkManager/system-connections/*", shell=True)
    objFile = open("./WiFi_List.txt", "a+")
    objFile.write(WiFi_List)
