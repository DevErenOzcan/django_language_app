# Language Learning Application With Django
Django ile çoklu dil desteği ile kelime öğreten bir uygulama geliştirdim. Uygulama; kullanıcının login, register gibi işlemleri yapan "accounts" ve kelime öğrenme kısımlarını kontrol eden "language_app" olmak üzere 2 kısımdan oluşuyor. Detayları görmek için bu kısımları inceleyebilirsiniz.

![Screenshot from 2025-02-27 14-47-24](https://github.com/user-attachments/assets/9729c980-2832-4f55-8638-8faadbbe4466)

## Uygulamayı Çalıştırmak İçin Şunları Yapmanız Yeterli: 

### virtual env i kur:
	# Linux:
	python3.12 -m venv .venv
	source .venv/bin/activate
	
	# Windows:
	python3.12 -m venv .venv
	.venv\Scripts\activate


### Gerekli dosyaları indir
	pip install -r requirements.txt

### Migration'ları Çalıştır:
	python manage.py makemigrations
 	python manage.py migrate

### Server'ı Çalıştır:
	python manage.py runserver
