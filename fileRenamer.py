import os
import numpy as np

# işlem yapılan kalsörler: neutral_out, negative_out, positive_out
# uygulama, yukardaki klasörlerden biri içerisindeki klasörlerin içerisindeki dosyalara rastgele numaralarda isim vermeye yarar
toplam = 0
for i in os.listdir("neutral_out"):
    toplam += len(os.listdir(f"neutral_out/{i}"))
print("pozitif seslerin sayisi: ", toplam)

liste = list(range(toplam))

for i in os.listdir("neutral_out"):
    for j in os.listdir(f"neutral_out/{i}"):
        choice = np.random.choice(liste)
        print(f"neutral_out/{i}/{j} değiştiriliyor...")
        os.rename(f"neutral_out/{i}/{j}", f"neutral_out/{i}/{choice}")
        print(f"{choice} olarak değiştirildi...")
        liste.remove(choice)