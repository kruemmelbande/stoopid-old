import sys,os
installdir="%appdata%\\stoopid"

#resolve path
installdir=installdir.replace("%appdata%",os.getenv("APPDATA"))
if not os.path.exists(installdir):
    os.mkdir(installdir)
files=[
    "stoopid.py",
    "build.bat",
    "stoopid.exe"
]
#install the requirements
os.system("pip install -r requirements.txt")
for file in files:
    os.system("copy %s %s" % (file,installdir))
#add the path to the environment variables
user=os.getenv("USERNAME")
cpath=os.getenv("PATH")

if not installdir in cpath:
    cpath+=";%s" % installdir
    #print(cpath)
    command="setx PATH \"%s\"" % cpath
    #print(command)
    os.system(command)
    print("Added %s to PATH" % installdir)

print("You can now run stoopid by typing stoopid in your terminal")

print("Installation complete!")