from zipfile import ZipFile
from tqdm import tqdm
from time import sleep
import zipfile
import patoolib
def progress(prog):
    for i in tqdm(prog, desc ="Progress : "):
        sleep(.1)
def unzip():
    direct = input("Enter The Location :")
    inp = input("Name a Folder : ")
    with ZipFile(rf'{direct}') as zipObj:
        progress(zipObj.infolist())
        zipObj.extractall(inp)
def unrar():
   direct = input("Enter The Location :") 
   inp = input("Your RAR name : ")
   prog = patoolib.extract_archive(rf"{inp}", outdir=rf"{direct}")
   progress(prog)

print("Welcome To Ultimate Unzeipper and Unrarer Program By Mohammed Ouedrhiri ")
print("If You Want To Unzip Press Z / If You Want To Unrar Press R")
answer = input("Your Answer Please : ")
answer = answer.lower()
while answer != quit:
    if answer == 'z':
        unzip()
    elif answer == 'r':
        unrar()
    else:
        print("Uknown Choice !! Try Again")