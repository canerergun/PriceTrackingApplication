import time  # Zaman işlemleri için gerekli kütüphane
import requests  # HTTP istekleri yapmak için gerekli kütüphane
from bs4 import BeautifulSoup  # Web sayfalarını analiz etmek için gerekli kütüphane
import smtplib  # E-posta göndermek için gerekli kütüphane
from email.mime.text import MIMEText  # Metin tabanlı e-posta oluşturmak için gerekli kütüphane
from email.mime.multipart import MIMEMultipart  # Çoklu parçalı e-posta oluşturmak için gerekli kütüphane

# Kullanıcıdan girdileri almak için bir fonksiyon
def get_user_input():
    url = input("İzlemek istediğiniz ürünün URL'sini girin: ")  # Kullanıcıdan URL iste
    beklenen_fiyat = float(input("Ürünün düşmesini beklediğiniz fiyatı girin: "))  # Kullanıcıdan beklenen fiyatı iste
    alici_email = input("Bildirim almak istediğiniz e-posta adresini girin: ")  # Kullanıcıdan alıcı e-posta adresini iste
    return url, beklenen_fiyat, alici_email  # Alınan bilgileri döndür

# Fiyatı kontrol etmek için bir fonksiyon
def check_price(url, beklenen_fiyat, alici_email):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}  # HTTP isteği başlığı
    try:
        sayfa = requests.get(url, headers=headers)  # URL'ye istek gönder
        sayfa.raise_for_status()  # Hata durumunda istisna oluştur
        soup = BeautifulSoup(sayfa.content, 'html.parser')  # Sayfa içeriğini parse et
        title = soup.find(id="product-name")  # Ürün başlığını bul
        
        if title:
            baslik = title.get_text().strip()  # Başlığı temizle
            print(baslik)  # Başlığı yazdır
        else:
            print("'product-name' id'sine sahip eleman bulunamadı.")  # Başlık bulunamadıysa uyarı yazdır

        span = soup.find(id="offering-price")  # Fiyat bilgisini bul
        
        if span:
            price = span.get_text().strip().split()  # Fiyatı temizle ve parçala
            price_str = price[0] + ' ' + price[1]  # Fiyatı string olarak birleştir
            print(f"Fiyat (string): {price_str}")  # String fiyatı yazdır
            price_float = float(price[0].replace('.', '').replace(',', '.'))  # Fiyatı float'a çevir
            print(f"Fiyat (float): {price_float}")  # Float fiyatı yazdır
            if price_float < beklenen_fiyat:  # Fiyat beklentinin altındaysa
                send_mail(baslik, url, alici_email)  # E-posta gönder
        else:
            print("'offering-price' id'sine sahip eleman bulunamadı.")  # Fiyat bilgisi bulunamadıysa uyarı yazdır
    except requests.exceptions.RequestException as e:
        print(f"Web sayfası alınırken hata oluştu: {e}")  # İstekle ilgili hata varsa uyarı yazdır

# E-posta göndermek için bir fonksiyon
def send_mail(product_title, product_url, receiver_email):
    sender = 'pricetrackinq@gmail.com'  # Gönderen e-posta adresi
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # SMTP sunucusuna bağlan
        server.ehlo()  # Bağlantıyı başlat
        server.starttls()  # TLS şifrelemesini başlat
        server.login(sender, 'rphr krip kjbg iuxz​')  # SMTP sunucusuna giriş yap

        subject = product_title + ' istediğiniz fiyata düştü!!!'  # E-posta konusu
        body = "Bu Linkten Gidebilirsin => " + product_url  # E-posta içeriği

        msg = MIMEMultipart()  # Çoklu parçalı e-posta oluştur
        msg['From'] = sender  # Gönderen adresi
        msg['To'] = receiver_email  # Alıcı adresi
        msg['Subject'] = subject  # Konu

        msg.attach(MIMEText(body, 'plain', 'utf-8'))  # Metin tabanlı e-postayı ekle

        server.sendmail(sender, receiver_email, msg.as_string())  # E-postayı gönder
        print("Mail gönderildi")  # Gönderme işlemi başarılı mesajı
    except smtplib.SMTPException as e:
        print(e)  # E-posta gönderirken hata oluşursa uyarı yazdır
    finally:
        server.quit()  # Bağlantıyı kapat

# Ana program akışı
if __name__ == "__main__":
    url, beklenen_fiyat, alici_email = get_user_input()  # Kullanıcı girdilerini al
    while True:  # Sonsuz döngü başlat
        check_price(url, beklenen_fiyat, alici_email)  # Fiyatı kontrol et
        time.sleep(60*60)  # Her saatte bir kontrol et
