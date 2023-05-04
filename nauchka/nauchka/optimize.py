import os, shutil, re, pathlib
current_path = (os.path.dirname(os.path.abspath(__file__)))
base = ""
folder = []
check = []
def Start():
    with open(f"{current_path}/settings.txt", encoding="utf-8") as settings:
        lines = settings.readlines()
        global base
        base = lines[0].rstrip()
        i=0
        for line in lines:
            global folder
            if i>1 and i<8:
                folder.append(line.rstrip())
            elif i>8:
                check.append(line.rstrip())
            i+=1
        print(base)
        print(folder)
        print(check)
def Sort(e):
    i = 0
    for file in os.listdir(base):
        i+=1
    for file in os.listdir(base):
        new_path = f"{base}/{file}"
        if re.search(check[0],file):
            try:
                shutil.move(new_path, folder[0])
            except: pass
        elif re.search(check[1],file): 
            try:
                shutil.move(new_path, folder[1])
            except: pass
        elif re.search(check[2],file): 
            try:
                shutil.move(new_path, folder[2])
            except: pass
        elif re.search(check[3],file): 
            try:
                shutil.move(new_path, folder[3])
            except: pass
        elif re.search(check[4],file): 
            try:
                shutil.move(new_path, folder[4])
            except:pass
        elif re.search(check[5],file): 
            try:
                shutil.move(new_path, folder[5])
            except:pass
    print(i)
def Save():
    with open(f"{current_path}/settings.txt", "w",encoding="utf-8") as save:
        save.write(f"{base}\n//\n")
        for fold in folder:
            save.write(f"{fold}\n")
        save.write("//\n")
        for crit in check:
            save.write(f"{crit}\n")
        for each in range(8):
            save.write("не хватило :( Но все норм работает, не вылетит\n")
Start()