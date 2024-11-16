import time
import keyboard

def sureHesapla(baslangicZamani):
    fark = time.time() - baslangicZamani
    print(f"Süre: {fark:.2f} saniye")

print("""Kronometre için aşağıdaki tuşları kullanın:
b: başlat
d: durdur
q: çık""")
baslangicZamani = time.time()
durum = False

while True:
    if durum:
        sureHesapla(baslangicZamani)
        time.sleep(1)  # 1 saniye bekleyerek çıktıyı günceller

    if keyboard.is_pressed("b"):
        baslangicZamani = time.time()  # Zamanı sıfırla ve başlat
        durum = True
        print("Kronometre başlatıldı.")
        time.sleep(1)  # Yanlışlıkla tekrar başlatmamak için kısa bir bekleme süresi

    elif keyboard.is_pressed("d"):
        durum = False
        print("Kronometre durduruldu.")
        time.sleep(1)  # Yanlışlıkla tekrar durdurmamak için kısa bir bekleme süresi

    elif keyboard.is_pressed("q"):
        print("Kronometre kapatılıyor.")
        break
