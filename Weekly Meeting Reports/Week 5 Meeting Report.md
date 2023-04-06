# Xor Ve Ötesi – Mini Mini Robotlar Projesi – 5.Hafta Toplantı Raporu
## Katılımcılar

- Buğra Koku
- İsmail Özçil
- Yusuf Onat Yılmaz
- Emir Bahadır Ünsal
- Burak Arslan
- Mert Kerem Ülkü
- Musa Doruk Uçar
- Abdulkadir Sarıtepe

## ÖN Hazırlık

### Olması Gerekenler
- Robot 90 derece dönebilmeli.
- Üst Kamera ile renk tanınabilmeli.
- Robotlar renkleri seçip taşıyabilmeli.
- Ana bilgisayar ile robotlar arasında kesintisiz iletişim olmalı.
- Otomatik şarj istasyonu olmalı.
- Robotlar şarjları azaldığında bunu otonom tespit edebilmeli.
- Robotların tepki süresi kısa olmalı.
- Sistem güvenli olmalı.
- Android uygulama ile uyumlu olmalı.
 
### Olsa Güzel Olacaklar
- Arayüz kullanıcı dostu olmalı.
- Hız ayarı yapılabilmeli.
- Android uygulamada png-to pixel dönüşümü yapılabilmeli.
- Gerçek zamanlı takip yapılabilmeli.
- Kamera ile geribildirim mekanizması olmalı.
- Tasarım modüler olmalı.

## Toplantı Raporu
### Toplantı Notları

1.	Düşük robot maliyeti bekleniyor.
2.	Fiziksel actuation kabiliyeti olacaksa düşük olmalı. 
3.	Mümkünse tamamen 3D Printer ve gerekirse planar lazer kesimle üretilecek 
4.	Custom pcb teşvik ediliyor
5.	Mümkün olan en küçük robot yapılmalı
6.	Bu robotların her biri uzaktan kontrol edilebilir olmalı
7.	RP2040 ile ilerlemek güzel olur. Micropython ile dönse güzel olur.
8.	Alternatifleri üretelim bu şekilde.
9.	Mümkünse PCB board sturctural element olarak da kullanılabilir.
10.	Belki SG90'ın üst seviyesi gibi continuous rotation servo ile motor sürücü ortadan kalkabilir.
11.	PCB tek kat olmak zorunda değil. Birden fazla da PCB yapılabilir. 
12.	Çok PCB özelleştirmede de sürekli dizgi ile uğraştırmayı gerektirebilir.
13.	Hedef hızlı ürettirip ME461’deki her gruba birer set verebilir hale getirelim.
14.	Mümkünse içerisinde biraz lehim de olsun ki 461 öğrencilerinin biraz da montaj lehim ile uğraşabilmesi için fırsat olsun.
15.	KOBOT gibi bir şey beklenmiyor. 
16.	Bireysel olarak her 461 grubunun masa üzerinde kendi AR'lerini oluşturabilmeli.
17.	Sensör olmasın: Çünkü en kompakt hale inilsin, ucuz olsun ve ucu açık olsun.
18.	Webots ile simülasyona aktarılabilmeli.
19.	Basit sensörler ile temel işleri yapabilsinler.
20.	LED'ler olmalı, NeoPixel led net olsun. Minimum birer tane.
21.	IO'larda yer kaldıysa Game Of LEDs için temel lehim ve denemeler yapabilirler.
22.	Tepeden kamerayla kolay ayırt edilebilecek robotlar olmalı. Aruco çalışır, alternatifler de bulunabilir.
23.	Kamera ve lazer tarayıcı sadece Webots’ta. Tutucusu olacak ama sadece Webots'ta olacak gibi. Her türlü özelleştirme Webots'ta, gerçekte üstten bakılarak yer tespiti yapılacak.
24.	Gerçek tarafta ekstra engeller (küpler, silindirler vs.) olur, bu sayede AR'ı gerçeğe geçirebiliriz. Webots'ta bunlar bina vs. olur. Av-Avcı’da robotlar birbirinin personasını görebilir. Aslan, ceylan, araba vs. gibi.
25.	AR ile 461 CV ve Search ü eğlenceli şekilde yapılabilir. Eş zamanlı gerçek robotlar da iletişimde kalınacağı için iki taraf da kontrol edilir. 
26.	Zor işler AR tarafına simülasyona atılacak. 
27.	Bu altyapı ile kendi evinde üstte kamera bağlanarak aynı sistemi çalıştırabilir. Ev ödevleri verilebilir.
28.	Mesela masanın 2 köşesine Aruco koyunca arenayı AR ile tanımlayabiliriz?
29.	Kurgu esnek olmalı.
30.	Robotta Self Charging olmalı. Charger'ı tespit edip kendi şarjına göre otomatik şarja gitmeli.
31.	Genel olarak testler ile alternatiflere bakılmalı, test edilmeli ve çıktılara göre karar verilmeli.
32.	Piller kompaktlığı belirleyecek asıl nokta. Piller chargerlar ile birlikte belirlenmeli. 
33.	Sensörler için: self docking ve self charging için sensör gerekecek. Analog sensing lazım.
34.	Minik OLED ile opsiyonel bir şeyler yapabilir miyiz? İsteyen alıp takabilmeli.
35.	Opsiyonel Add-on'lara açık. Ancak yeni add-onlar çok da büyütmemeli robotu.
36.	Step motor labında kullandığımız motora bakılmalı. Tork'u yeterli olabilir. Teker yarıçapını da ayarlayabiliyormuşuz.
37.	Hedef Footprint'i mümkün olduğunca küçültmek. 2 motor arası 1 kalem pil (14500-AA) in dışına çıkmamalı boyutumuz.
38.	Ne kadar küçük olursa kırılma ihtimali o kadar azalır.
39.	Webots server modunda uzaktan başlatılabiliyor. Araştırılmalı
40.	Her robotun ROS2 üzerinden webots+robot ile iletişim kurabilmesi lazım.
41.	Motor tekerlek için palet ya da 2motor+2kayış denenebilir.

### Toplantı Çıktıları

#### Olması Gerekenler
- Küçüklük
- Self-charging
- AR adaptivitiy
- LED Ring'ler
- Motor olacak
 
#### Olsa Güzel Olacaklar
- PCB'yi structural element olarak kullanmak