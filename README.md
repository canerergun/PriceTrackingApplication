# PriceTrackingApplication

Bilgi: Program Yalnızca Hepsiburada Linkleri Üzerinde Çalışmaktadır!

# Ürün Fiyat İzleyici

Bu kod, belirli bir ürünün fiyatını izlemek ve fiyat beklenen bir seviyeye düştüğünde kullanıcıya bildirim göndermek için tasarlanmıştır.

## Gereksinimler

- Python 3.x
- requests kütüphanesi: HTTP istekleri yapmak için gereklidir.
- BeautifulSoup kütüphanesi: Web sayfalarını analiz etmek için kullanılır.
- smtplib kütüphanesi: E-posta göndermek için gereklidir.
- email.mime.text ve email.mime.multipart alt kütüphaneleri: E-posta oluşturmak için kullanılır.

## Kullanım

1. Kullanıcıdan ürün URL'si, beklenen fiyat ve alıcı e-posta adresi istenir.
2. Belirtilen URL'den ürün bilgileri alınır ve fiyat kontrol edilir.
3. Eğer ürünün fiyatı beklenen fiyatın altındaysa, kullanıcıya e-posta gönderilir.
4. Belirli aralıklarla fiyat kontrolü yapılır (varsayılan olarak her saatte bir).

## Kod Açıklaması

- `get_user_input()`: Kullanıcıdan girdi almak için bir fonksiyon.
- `check_price(url, beklenen_fiyat, alici_email)`: Belirtilen URL'den ürün bilgilerini alıp fiyatı kontrol eden bir fonksiyon.
- `send_mail(product_title, product_url, receiver_email)`: Belirtilen başlık, URL ve alıcı e-posta adresine e-posta gönderen bir fonksiyon.
- Ana program akışı: Kullanıcı girdilerini al, fiyatı kontrol et ve belirli aralıklarla tekrar et.

## Örnek Kullanım

1. Kullanıcıdan URL, beklenen fiyat ve e-posta adresi alınır.
2. URL'den alınan ürünün fiyatı beklenen fiyatın altındaysa, kullanıcıya e-posta gönderilir.
3. Belirli aralıklarla fiyat kontrolü yapılır ve gerekirse e-posta gönderilir.

## Notlar

- Kodda Gmail SMTP sunucusu kullanıldığı için, gönderen e-posta adresi ve şifresi Google hesabınızın güvenlik ayarlarından "Daha az güvenli uygulamalara erişim" seçeneğinin etkinleştirilmesi gerekmektedir.
- Kodda varsayılan olarak her saatte bir fiyat kontrolü yapılmaktadır. Gerekirse bu aralık değiştirilebilir.

## Güvenlik Uyarısı

Kod, üçüncü taraf web sitelerinden veri almak ve e-posta göndermek için kullanıcıdan alınan bilgileri kullanır. Bu nedenle, bu tür işlemlerin yasalara uygun olması ve hedef web sitesinin kullanım şartlarına uygun olması önemlidir. Ayrıca, kodu güvenliği göz önünde bulundurarak kullanmak önemlidir. Özellikle, e-posta adresi ve şifre gibi hassas bilgilerin güvenliğini sağlamak için gerekli önlemler alınmalıdır.

## Lisans

Bu kod örnek bir proje olarak sunulmuştur ve herhangi bir lisans altında dağıtılmaktadır. Kodu kendi projenizde veya ihtiyaçlarınıza göre değiştirebilir ve kullanabilirsiniz.

---

Bu belge, ürün fiyat izleme kodunun çalışma mantığını ve kullanımını anlatır. Daha fazla bilgi için kod içindeki yorum satırlarını ve ilgili kütüphanelerin belgelerini inceleyebilirsiniz.
