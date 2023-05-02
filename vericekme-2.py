import requests
from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter import ttk

url = "https://www.bloomberght.com/doviz"
response = requests.get(url=url)
content = bs(response.content, "html.parser")

div = content.find('div', {"class": "widget-table-data type3 marketsData"})#Döviz kurlarının tablolarının bulunduğu div etiketi belirtilir.

tables = div.find_all('table') #div etiketindeki tüm tablolar find_all() fonksiyonu kullanılarak tables listesine eklenir.
#print(tables)

root = Tk()
root.title("Döviz Kurları")#tkinter kütüphanesi kullanılarak pencere oluşturulur ve pencere başlığı belirlenir.

treeview = ttk.Treeview(root)#ttk.Treeview() fonksiyonu kullanılarak treeview adında bir ağaç görünüm bileşeni oluşturulur ve her bir sütunun adı belirlenir.
treeview["columns"] = ("Birim", "Alış", "Satış", "Saat")


#GUI'deki Treeview bileşeni, öncelikle sütunları belirtmek için kullanılan "columns" özelliği ile yapılandırılır. "#0" sütunu, diğer sütunlarla birlikte genişliği ayarlanabilir bir başlık sütunu sağlamak için kullanılır. Her sütunun genişliği, column metoduyla belirlenir ve sütun başlığı, heading metodu kullanılarak belirlenir.

#Her bir sütunun genişliği ve hizalaması belirlenir.
treeview.column("#0", width=0, stretch=NO)
treeview.column("Birim", anchor=CENTER, width=100)
treeview.column("Alış", anchor=CENTER, width=100)
treeview.column("Satış", anchor=CENTER, width=100)
treeview.column("Saat", anchor=CENTER, width=100)

#Her bir sütunun başlığı belirlenir.
treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("Birim", text="Birim", anchor=CENTER)
treeview.heading("Alış", text="Alış", anchor=CENTER)
treeview.heading("Satış", text="Satış", anchor=CENTER)
treeview.heading("Saat", text="Saat", anchor=CENTER)

#Tablolardaki veriler for döngüsü kullanılarak ayrıştırılır ve her bir döviz kuru, treeview bileşenine eklenir.
for table in tables:
    rows = table.find_all('tr')
    for row in rows[1:]:  # ilk satırda başlıklar olduğu için atlanır
        cells = row.find_all('td')
        symbol = str(cells[1].text).strip()
        buying = cells[2].text
        selling = cells[3].text
        clock = cells[5].text
        # Altta yapılan işlem cells den alınan verilerin ne şekilde olduğunu görmek içindir. Bu sayede cells[1] de önde ve arkada aşırı boşluklar olduğunu tespit ettim ve strip() fonksiyonuyla bu sorunu giderdim. Ayrıca hangi indexde hangi veri tutulduğu da gösteriliyor.
        #sayac=0
        #for j in cells:
        #    print(f"eleman{sayac}: {j}")
        #    sayac+=1
        treeview.insert("", "end", text="", values=(symbol, buying, selling, clock)) #insert() yöntemi, treeview'a bir satır eklemek için kullanılır. "" ifadesi, eklenecek satırın hangi üst öğe altında yer alacağını belirtir. Bu durumda, satırın en üst düzeyde yer alacağı belirtilir. "end" ifadesi, satırın ağaç düzenindeki konumunu belirtir. "end", satırın mevcut son pozisyona eklenmesini sağlar. text="" ifadesi, satırın metin içeriğini belirtir. Bu durumda, satırın metin içeriği boştur. values=(symbol, buying, selling, clock) ifadesi, satırın değerlerini belirtir. Bu satır, döviz kuru verilerinin bir satırını temsil eder. 

treeview.pack(expand=YES, fill=BOTH) #treeview tablo pencereye yerleştirilir. expand=YES ifadesi, treeview bileşeninin, eğer pencere boyutlarından daha büyükse, pencerenin boyutlarına uyacak şekilde genişletilmesini sağlar. fill=BOTH ifadesi, treeview bileşeninin, hem yatayda hem de dikeyde pencere boyutlarına uyacak şekilde genişletilmesini sağlar.

def refresh_data():
    #requests kütüphanesi kullanılarak URL'deki sayfa tekrardan istenir ve BeautifulSoup ile sayfa içeriği analiz edilir.
    response = requests.get(url=url)
    content = bs(response.content, "html.parser")

    div = content.find('div', {"class": "widget-table-data type3 marketsData"})
    tables = div.find_all('table')

    # Treeview bileşenini temizleyin
    treeview.delete(*treeview.get_children())

    # Yeni verileri Treeview'a ekle
    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:  # ilk satırda başlıklar olduğu için atlanır
            cells = row.find_all('td')
            symbol = str(cells[1].text).strip()
            buying = cells[2].text
            selling = cells[3].text
            clock = cells[5].text
            treeview.insert("", "end", text="", values=(symbol, buying, selling, clock))

# Yenile butonu, basıldığında refresh_data fonksiyonunu çalıştırır
refresh_button = Button(root, text="Yenile", command=refresh_data)
refresh_button.pack()

root.mainloop()