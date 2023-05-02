import os
folders=["photos"]
for folder in folders:
    sayac=0
    for i in os.listdir(folder):
        os.rename(f"{folder}/{i}",f"{folder}/{sayac}.jpg")
        sayac+=1