**URL Deployment PWS: https://rosanne-valerie-ecommerce.pbp.cs.ui.ac.id/**

<details>
  <summary>Tugas 2</summary>
# TUGAS 2
## 1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.**  
Jawaban:  
Setelah membuat folder bernama e-commerce, saya menginstal semua yang dibutuhkan, termasuk Django. Untuk memulai proyek, saya menjalankan command `django-admin startproject e_commerce`. Setelah proyek jadi, saya buat aplikasi baru bernama dengan command `python manage.py startapp main`, setelah dijalankan Django akan otomatis membuat folder main yang sudah ada file-file dasarnya. Selanjutnya, saya mengatur routing URL supaya aplikasi main nya bisa dijalankan buat file `urls.py` di dalam folder main dan masukkan URL yang kita inginkan. Setelah itu, saya menambahkan atribut yang dibutuhkan di `models.py`, seperti nama, harga, deskripsi dan sweetness. Saya menggunakan tipe data yang tepat seperti `CharField`, `DecimalField`, `IntegerField`, dan `TextField`. Kemudian saya melakukan migrasi supaya perubahan diterapkan ke database. Kemudian, saya membuat fungsi di `views.py` yang akan mengembalikan halaman HTML. Fungsi ini akan menampilkan nama aplikasi dan item yang saya jual. Fungsi ini akan mengembalikan request dan menampilkan template HTML yang kita buat di `main.html`. Setelah itu, saya menambahkan routing di file `urls.py` di aplikasi main. Terakhir, saya deploy aplikasinya ke PWS agar bisa diakses lewat internet, caranya dengan membuat proyek baru. Saya juga menambahkan URL dari PWS ke `ALLOWED_HOSTS` di file `settings.py`, dan isi kredensial yang diperlukan untuk proses deploy.

## 2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**  
Jawaban:  
<img src="bagan.png">  
Saat pengguna mengirim permintaan dari browser, Django akan mengecek `urls.py` untuk menentukan URL yang tepat dan mengarahkan ke fungsi di `views.py`. Di `views.py`, logika dijalankan, dan jika butuh data dari database, Django akan mengambilnya melalui `models.py`. Setelah itu, data dikirim ke template HTML untuk ditampilkan. Lalu, halaman HTML yang sudah jadi dikirim kembali ke browser sebagai respon.

## 3. **Jelaskan fungsi git dalam pengembangan perangkat lunak!**  
Jawaban:  
Git adalah alat yang dapat membantu kita dalam mengelola perubahan kode. Dengan Git, kita bisa melacak setiap perubahan yang kita buat, jadi ketika ada kesalahan, kita bisa kembali ke versi sebelumnya. Kemudian Git juga memudahkan kerja tim karena memunngkinkan banyak orang bekerja di proyek yang sama tanpa bertabrakan.

## 4. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**  
Jawaban:  
Menurut saya, juga berdasarkan apa yang dipelajari di kelas, Django sering dipilih sebagai permulaan dasar dalam pengembangan perangkat lunak karena banyak fitur penting seperti autentikasi, manajemen database, dan routing yang sudah langsung disediakan, jadi tidak perlu repot mengatur semuanya dari awal. Selain itu, Django juga menggunakan bahasa Python yang lebih sederhana dan mudah dipahami.

## 5. **Mengapa model pada Django disebut sebagai ORM?**  
Jawaban:  
Disebut sebagai ORM (Object-Relational Mapping) karena dia membantu kita berhubungan dengan database tanpa perlu menulis query SQL langsung. ORM ini memungkinkan kita untuk mengelola data di databse dengan menggunakan kode Python yang lebih mudah dipahami. Jadi, Django akan menerjemahkan kode Python kita ke dalam bahasa yang dimengerti database secara otomatis.
</details>

<details>
  <summary>Tugas 3</summary>
# TUGAS 3
## 1. Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?  
Jawaban:  
Pengiriman data dalam platform itu penting karena harus cepat dan aman. Ini supaya informasi yang dikirim antara pengguna dan sistem tetap benar dan tidak rusak. Kalau datanya lambat atau tidak aman, bisa mengganggu penggunaan platform. Jadi, dengan pengiriman data yang lancar, pengguna bisa menggunakan platform dengan nyaman tanpa khawatir ada masalah dengan informasi yang dikirim atau diterima.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  
Jawaban:  
Menurut saya, JSON lebih baik daripada XML karena lebih sederhana dan gampang dipahami. JSON juga lebih cepat diproses, jadi lebih sering dipakai di aplikasi web. XML masih digunakan, tapi biasanya untuk sistem yang lebih rumit atau saat butuh format data yang lebih kompleks.

## 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?  
Jawaban:  
Fungsi `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke form sudah benar dan sesuai aturan. Kalau datanya valid, form bisa diproses lebih lanjut. Kita membutuhkan method ini supaya bisa memastikan data yang masuk ke sistem sudah sesuai dan tidak ada kesalahan sebelum disimpan atau digunakan.

## 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawaban:  
Kita butuh `csrf_token` di form Django untuk melindungi dari serangan CSRF (Cross-Site Request Forgery). Jika tidak menambahkannya, penyerang bisa membuat pengguna tanpa sadar mengirim permintaan berbahaya ke situs, misalnya mengubah data atau melakukan tindakan yang tidak diinginkan. Dengan `csrf_token`, sistem bisa memastikan bahwa permintaan benar-benar datang dari pengguna yang sah dan bukan dari penyerang.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).  
Jawaban:  
Keseluruhan proyek ini saya kerjakan dengan mengikuti semua step yang ada di turorial. Selain mengikuti tutorial yang ada, terdapat beberapa hal yang saya lakukan untuk mengimplementasikan *checklist* di atas yaitu dengan menambahkan *default items* dan mengubah format kode `main.html` dari kode yang ada di tutorial agar tampilannya sesuai dengan tampilan yang saya mau. Setelah itu saya juga melakukan.

**SCREENSHOTS**
<img src="ecommerce_json.jpg"> 
<img src="ecommerce_xml.jpg"> 
<img src="ecommerce_json_id.jpg">   
<img src="ecommerce_xml_id.jpg">  
</details>

<details>
  <summary>Tugas 4</summary>
# Tugas 4
## 1. **Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**  
Jawaban:  
`HttpResponseRedirect()` digunakan untuk mengalihkan pengguna ke URL yang ditentukan. Fungsi ini hanya menerima URL sebagai argumen. Jadi, saat kita menggunakan `HttpResponseRedirect()`, kita harus menyediakan URL lengkap tempat kemana kita ingin diarahkan. Di sisi lain, `redirect()` adalah fungsi yang lebih fleksibel. Selain menerima URL, fungsi ini juga bisa mengambil nama view atau objek model sebagai argumen. Hal ini membuat `redirect()` lebih praktis dan sering digunakan dalam berbagai situasi, karena dapat menangani berbagai jenis argumen, tidak hanya URL.

## 2. **Jelaskan cara kerja penghubungan model Product dengan User!**  
Jawaban:  
Dalam Django, relasi antara model `Product` dan `User` diatur menggunakan *Foreign Key* untuk menghubungkan setiap instance `Product` dengan `User` yang bertindak sebagai pembuat atau pemilik. Contohnya, pada model `Candy`, field `user` yang merupakan ForeignKey menghubungkan setiap permen dengan pengguna yang terkait, menunjukkan kepemilikan. Kode `on_delete=models.CASCADE` berarti bahwa penghapusan pengguna akan menyebabkan penghapusan semua permen yang terkait dengannya, menjaga integritas data dalam aplikasi.

## 3. **Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**  
Jawaban:  
*Authentication* adalah proses untuk memverifikasi identitas pengguna. Ini terjadi saat pengguna login dengan memasukkan kredensial seperti username dan password. Django memverifikasi ini melalui sistem *authentication* bawaan yang mengatur login dan logout. *Authorization* adalah proses menentukan apa yang bisa dilakukan pengguna setelah mereka terverifikasi. Ini berkaitan dengan mengatur akses ke sumber daya tertentu, seperti halaman atau fungsi dalam aplikasi, berdasarkan peran atau izin pengguna.

Alur implementasi dalam Django:
* Pengguna mengirimkan permintaan melalui browser ke internet, yang kemudian diteruskan ke web server.
* Sebelum mengizinkan akses ke server, Django akan melakukan proses autentikasi dan otorisasi pada sesi pengguna. Autentikasi memverifikasi keaslian pengguna, sementara otorisasi menentukan hak akses pengguna.
* Jika pengguna lolos kedua proses tersebut, Django akan meneruskan permintaan ke web server. Di sini, argumen diekstrak dari permintaan untuk diolah di `views.py`, yang berisi logika Python (fungsi-fungsi) untuk menghasilkan respons.
* Output dari `views.py` akan dikombinasikan dengan template HTML untuk membuat halaman web yang akan dikirim kembali ke pengguna.
* Pengguna menerima halaman web yang telah diproses melalui internet dan dapat melihatnya di browser mereka.

Dalam pengimplementasian ini, contoh dari proses autentikasi bisa dilihat pada fungsi `login_user` di `views.py`, di mana pengguna diminta memasukkan kredensial mereka. Jika kredensial tersebut valid, pengguna dianggap terautentikasi dan status login mereka disimpan dalam sesi. Contoh otorisasi adalah penggunaan *decorator* `@login_required(login_url='/login')` di atas fungsi tertentu, yang memastikan bahwa hanya pengguna yang sudah masuk yang dapat mengakses fungsi tersebut. Karena proyek ini belum memiliki pembatasan akses lebih lanjut, pengguna yang telah masuk dapat menggunakan semua fungsi yang tersedia.

## 4. **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**  
Jawaban:  
Django mengingat pengguna yang telah login menggunakan mekanisme yang dikenal sebagai *sessions* dan **cookies*. Ketika users login, Django membuat sebuah *session* di server dan menyimpan *session* ID dalam sebuah *cookie* yang dikirim ke browser pengguna. *Cookie* ini memungkinkan server untuk mengenali dan mempertahankan status logged-in pengguna setiap kali mereka melakukan request ke server.

Kegunaan lain dari *cookies*
* Dapat menyimpan preferensi seperti layout atau bahasa yang dipilih pengguna.
* Membantu dalam melacak kegiatan pengguna di situs, yang berguna untuk analisis dan peningkatan layanan.
* Digunakan untuk mempertahankan status autentikasi pengguna di seluruh sesi.
* Digunakan untuk menyajikan iklan yang disesuaikan dengan kebiasaan dan preferensi pengguna.  

Tidak semua *cookies* itu aman. Jika *cookies* tidak diatur dengan baik, seperti tidak menggunakan enkripsi atau pengaturan keamanan, bisa jadi celah untuk serangan dari hacker. Ini bisa menyebabkan informasi pribadi bocor atau disalahgunakan.

## 5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Jawaban:  
* Pertama-tama, saya menyiapkan halaman registrasi dan login dengan membuat `register.html` dan `login.html` di folder templates di aplikasi utama. Halaman ini akan ditampilkan saat pengguna ingin mendaftar atau masuk.
* Untuk proses pendaftaran, saya menggunakan `UserCreationForm` dari Django dan modul `messages` untuk memberi tahu pengguna jika akunnya berhasil dibuat. Saya membuat fungsi `register` yang merender `register.html`.
* Untuk login, saya menambahkan import fungsi `authenticate` dan `login`, serta membuat fungsi `login_user` yang merender `login.html`.
* Untuk memungkinkan pengguna yang sudah login untuk logout, saya mengimpor `logout` dan membuat fungsi `logout_user` yang mengarahkan pengguna kembali ke halaman login. Saya menambahkan tombol di `main.html` yang terhubung ke fungsi `logout_user`.
* Saya menggunakan dekorator `@login_required` pada `show_main` agar pengguna harus login terlebih dahulu sebelum mengakses halaman utama.
* Semua fungsi ini dikonfigurasikan di `urls.py` dan ditambahkan ke `urlpatterns` agar bisa diakses oleh aplikasi.
* Saya juga menggunakan cookies untuk melacak kapan pengguna terakhir login. Setelah pengguna berhasil login, saya mengatur cookie, dan menghapusnya saat pengguna logout. Informasi ini ditampilkan di `show_main` dan dirender di `main.html`.
* Untuk menghubungkan pengguna dengan produk, saya mengimpor `User` dan menggunakan `ForeignKey` di `models.py` untuk mengasosiasikan produk dengan pengguna. Dalam `views.py`, saya memodifikasi `create_item_entry` untuk mengaitkan item dengan pengguna yang login sebelum menyimpannya ke database. Saya juga menyaring produk yang ditampilkan di `show_main` berdasarkan pengguna yang login.
* Akhirnya, saya melakukan migrasi database dan mengatur variabel `DEBUG` di `settings.py` untuk persiapan produksi. Saya juga membuat dua akun pengguna dan tiga data dummy di lingkungan lokal untuk pengujian.
</details>