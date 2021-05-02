# Unzipper and Unrarer By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## The Progress Bar :

### I've Creted The Progress Bar Using THE Tqdm (تقدم) and Import it

`from tqdm import tqdm`

### Then Imported The Sleep Library To Control The Time Flow

`from time import sleep`

</br>

---

## I've Created Also 2 Functions One To Deal With Zip File And Another To Deal With Rar Files

### The One For Zip File :

    def unzip():

> ### To get The Location

    direct = input("Enter The Location :")

> ### To Name The Folder When It is Unzipped

    inp = input("Name a Folder : ")
    with ZipFile(rf'{direct}') as zipObj:

> ### Call The Progress Bar Function with Argument Info To Make it Process in a Real Time

        progress(zipObj.infolist())

> ### And Finally Extract All The Files

        zipObj.extractall(inp)

---

### The One For Rar File :

    def unrar():

> ### To get The Location

        direct = input("Enter The Location :")

> ### To Name The Folder When It is Unzipped

        inp = input("Your RAR name : ")

> ### Call The Extract Function with 2 arguments The OUTDIRECTORY and the File Name

        prog = patoolib.extract_archive(rf"{inp}", outdir=rf"{direct}")

> ### Call The Progress Bar Function with Argument Prog To Make it Process in a Real Time

        progress(prog)

---

## I Hope My Project Get Your Admiration

</br>
Thanks For Using My Code If You Have Any Problem Contact Me On email : mouedrhiri492@gmail.com

> Mohammed Ouedrhiri &copy;

![logo](https://www.laformation.ma/images/contenu/24214a91e4.png)
