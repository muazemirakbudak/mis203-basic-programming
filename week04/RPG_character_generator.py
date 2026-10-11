import math
import random
import time

# Terminal Renk Kodları (ANSI)
YEŞİL = "\033[92m"
MAVİ = "\033[94m"
SARI = "\033[93m"
KIRMIZI = "\033[91m"
CYAN = "\033[96m"
SIFIRLA = "\033[0m"


def animasyonlu_yazdir(metin, renk=SIFIRLA, gecikme=0.015):
  """Renk ve daktilo efektiyle metin yazdırır."""
  print(renk, end="")
  for karakter in metin:
    print(karakter, end="", flush=True)
    time.sleep(gecikme)
  print(SIFIRLA)


def guc_bari_ciz(deger, maksimum=100, genislik=20):
  """Math kütüphanesini kullanarak dinamik güç barı oluşturur."""
  oran = deger / maksimum
  dolu_miktar = math.floor(oran * genislik)
  bos_miktar = genislik - dolu_miktar
  bar = "█" * dolu_miktar + "░" * bos_miktar
  return f"[{bar}] %{int(oran * 100)}"


def kahraman_sentezle():
  animasyonlu_yazdir(
      "=== 🗡️ EFSANEVİ KAHRAMAN OLUŞTURUCU 🛡️ ===", SARI, 0.01
  )
  print("=" * 50)

  isim = input("\nKahramanının adını gir: ").strip()
  if not isim:
    isim = "Bilinmeyen Savaşçı"

  # Random kütüphanesi ile rastgele sınıf ve unvan seçimi
  siniflar = [
      "Büyücü 🧙‍♂️",
      "Savaşçı ⚔️",
      "Okçu 🏹",
      "Gölge Suikastçı 🗡️",
      "Ejderha Süvarisi 🐉",
  ]
  unvanlar = [
      "Karanlıklar Efendisi",
      "Fırtına Getiren",
      "Unutulmuş Ruh",
      "Alevlerin Efendisi",
      "Kayıp Krallığın Muhafızı",
  ]

  secilen_sinif = random.choice(siniflar)
  secilen_unvan = random.choice(unvanlar)

  # Time kütüphanesi ile yükleme simülasyonu
  animasyonlu_yazdir(
      f"\n✨ {isim} için kader zarları atılıyor...", MAVİ, 0.02
  )
  for i in range(3, 0, -1):
    print(f"[{i}] Zarlar dönüyor...", end="\r")
    time.sleep(0.5)

  # Rastgele stat puanları (10 - 100 arası)
  can = random.randint(60, 100)
  guc = random.randint(40, 100)
  zeka = random.randint(30, 100)
  hiz = random.randint(50, 100)

  print("\n" + "=" * 50)
  animasyonlu_yazdir(
      f"📜 KAHRAMAN KÜNYESİ: {isim.upper()} THE {secilen_unvan.upper()}",
      YEŞİL,
      0.02,
  )
  animasyonlu_yazdir(f"Sınıf: {secilen_sinif}", CYAN, 0.01)
  print("=" * 50)

  # Math ve Random verilerini ekrana renkli barlarla basma
  time.sleep(0.3)
  print(f"CAN  : {guc_bari_ciz(can)}  ({KIRMIZI}{can} HP{SIFIRLA})")
  time.sleep(0.3)
  print(f"GÜÇ  : {guc_bari_ciz(guc)}  ({SARI}{guc} STR{SIFIRLA})")
  time.sleep(0.3)
  print(f"ZEKA : {guc_bari_ciz(zeka)}  ({MAVİ}{zeka} INT{SIFIRLA})")
  time.sleep(0.3)
  print(f"HIZ  : {guc_bari_ciz(hiz)}  ({YEŞİL}{hiz} AGI{SIFIRLA})")

  print("-" * 50)

  # Genel Güç Puanı Hesaplama (Math kütüphanesi kullanımı)
  ortalama_guc = math.ceil((can + guc + zeka + hiz) / 4)
  animasyonlu_yazdir(
      f"⭐ Toplam Savaş Puanı (Power Level): {ortalama_guc} / 100", SARI, 0.02
  )

  if ortalama_guc >= 80:
    animasyonlu_yazdir(
        "🔥 Değerlendirme: Bu kahraman bir efsane olmaya aday!", YEŞİL
    )
  elif ortalama_guc >= 60:
    animasyonlu_yazdir(
        "⚔️ Değerlendirme: Güçlü bir savaşçı, loncaya kabul edildi.", MAVİ
    )
  else:
    animasyonlu_yazdir(
        "🛡️ Değerlendirme: Henüz acemi. Biraz daha antrenman yapmalı.",
        KIRMIZI,
    )


if __name__ == "__main__":
  kahraman_sentezle()
