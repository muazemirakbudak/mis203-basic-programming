branslar = ("Yazılım", "Tasarım", "Pazarlama")


tum_ogrenciler = []

tum_ogrenciler.append(["Ahmet Yılmaz".strip(), ["Yazılım"]])
tum_ogrenciler.append(["Zeynep Demir".strip(), ["Tasarım", "Pazarlama"]])
tum_ogrenciler.append(["  Mehmet Kaya  ".strip(), ["Yazılım"]])

print("Mevcut Öğrenci Listesi:")
print(tum_ogrenciler)

tum_ogrenciler.insert(0, ["Buse Korkmaz".strip(), ["Yazılım", "Pazarlama"]])


toplam_ogrenci = len(tum_ogrenciler)
print(f"Toplam Kayıtlı Öğrenci Sayısı: {toplam_ogrenci}")


silinecek_ogrenci = ["Ahmet Yılmaz", ["Yazılım"]]
for silinecek_ogrenci in tum_ogrenciler:
    tum_ogrenciler.remove(silinecek_ogrenci)

son_ogrenci = tum_ogrenciler.pop()
print(f"Sistemden en son çıkan öğrenci: {son_ogrenci[0]}")


tum_ogrenciler.append(["Burak Tan".strip(), ["Tasarım"]])


sirali_gecici = sorted(tum_ogrenciler, key=lambda x: x[0])  
print("Geçici Alfabetik Liste (sorted):")
print(sirali_gecici)

print("\nOrijinal Listenin Değişmediğinin Kanıtı:")
print(tum_ogrenciler)


print("Ana Listenin Kalıcı Olarak Sıralanmış Hali (sort):")
print(tum_ogrenciler)

