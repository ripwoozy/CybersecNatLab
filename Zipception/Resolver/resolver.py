from zipfile import ZipFile
for z in reversed(range(3001)):
    with ZipFile("flag" + str(z) +".zip", 'r') as zipObj:
        zipObj.extractall()
    print(f"[!] Flag{z} Unzipped")