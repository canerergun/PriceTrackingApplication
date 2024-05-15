# PriceTrackingApplication

[TR]
 Bu Python programı, kullanıcının belirlediği bir ürünün fiyatını izleyen ve belirlenen fiyatın altına düştüğünde kullanıcıya e-posta ile bildirim gönderen bir fiyat takip uygulamasıdır.
Kullanıcı, programı çalıştırdığında izlemek istediği ürünün URL'sini, beklediği fiyatı ve bildirim almak istediği e-posta adresini girer. Program, belirtilen URL'yi düzenli aralıklarla kontrol eder ve ürün fiyatı beklenen fiyatın altına düştüğünde, kullanıcıya bir e-posta gönderir.
Bu program, Requests ve BeautifulSoup gibi harici kütüphaneleri kullanarak web scraping işlemleri gerçekleştirir. Ayrıca, smtplib kütüphanesini kullanarak e-posta gönderme işlemlerini gerçekleştirir..


[EN]
 This Python program is a price tracking application that monitors the price of a product specified by the user and sends an e-mail notification to the user when it falls below the specified price.
When the user runs the program, he enters the URL of the product he wants to track, the price he expects and the email address he wants to receive notifications from. The program checks the specified URL at regular intervals and when the product price drops below the expected price, it sends an email to the user.
This program performs web scraping using external libraries such as Requests and BeautifulSoup. It also performs email sending operations using the smtplib library.
