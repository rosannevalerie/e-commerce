**URL Deployment PWS: http://rosanne-valerie-ecommerce.pbp.cs.ui.ac.id/**

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

<details>
  <summary>Tugas 5</summary>

# Tugas 5
## 1. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**  
Jawaban: 
Jika terdapat beberapa CSS selector yang diterapkan pada satu elemen HTML, browser akan mengikuti urutan prioritas untuk menentukan gaya mana yang akan digunakan. Berikut urutan prioritas CSS selector tersebut:
* Inline Style
Gaya yang ditulis langsung dalam elemen HTML menggunakan atribut `style` memiliki prioritas tertinggi. Contohnya: `<p style="color: red;">Teks ini berwarna merah</p>`. Gaya ini akan mengesampingkan aturan yang ada dalam file CSS eksternal atau internal.
* ID Selector
Selektor ID, seperti `#header { color: blue; }`, memiliki prioritas lebih tinggi dibandingkan selektor class atau elemen HTML. ID bersifat unik dan hanya dapat digunakan sekali pada halaman.
* Class Selector, Pseudo-class, dan Attribute Selector
Selektor class (misalnya `.button { color: green; }`), pseudo-class (seperti `:hover`), dan attribute selector (seperti `[type="text"]`) memiliki prioritas di bawah ID, tetapi lebih tinggi dari selektor elemen.
* Tag (Type) Selector
Selektor elemen atau tag HTML (misalnya `p { color: yellow; }`) memiliki prioritas paling rendah. Gaya dari ID atau class akan mengesampingkan gaya yang diterapkan oleh selektor elemen ini.
* !important
Deklarasi `!important` dapat memberikan prioritas tertinggi pada suatu aturan CSS, mengesampingkan aturan lain meskipun lebih spesifik. Namun, jika ada lebih dari satu `!important`, urutan prioritas di atas tetap berlaku.
* Urutan dalam File
Jika terdapat beberapa aturan dengan tingkat prioritas yang sama, browser akan menerapkan aturan yang muncul terakhir dalam file CSS.
Dengan aturan ini, browser dapat menentukan gaya mana yang akan diterapkan jika terdapat beberapa gaya yang berkonflik.

## 2. **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**  
Jawaban:  
Responsive design penting dalam pengembangan aplikasi web karena pengguna sekarang mengakses internet dari berbagai perangkat, seperti komputer, tablet, dan smartphone. Ukuran layar dan resolusi perangkat tersebut bervariasi, sehingga jika desain web tidak disesuaikan, tampilan bisa menjadi tidak rapi, sulit dibaca, atau bahkan sebagian konten bisa keluar dari layar. Responsive design memastikan tampilan web otomatis menyesuaikan dengan ukuran layar perangkat, sehingga pengguna dapat dengan nyaman mengakses konten dan fitur yang ada.

Contoh aplikasi yang sudah menerapkan responsive design adalah **X**. Ketika diakses dari berbagai perangkat, baik itu desktop, tablet, atau smartphone, tampilan Twitter tetap konsisten dan mudah digunakan tanpa harus melakukan zoom atau scroll berlebihan. Sedangkan contoh aplikasi yang tidak responsif yang saya pernah gunakan adalah `aren.csui.ac.id`.

Dengan responsive design, aplikasi web dapat memberikan pengalaman pengguna yang lebih baik di semua perangkat, sehingga lebih mudah diakses dan digunakan.

## 3. **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**  
Jawaban:  
* Margin adalah ruang di luar elemen. Ini seperti jarak antara elemen tersebut dengan elemen lain di sekitarnya. Margin tidak terlihat secara visual karena tidak punya warna atau garis; hanya membuat jarak kosong.
     ```css
     .box {
       margin: 20px; /* Memberikan jarak 20px di luar elemen */
     }
     ```

* Border adalah garis di sekeliling elemen. Border berada di antara padding dan margin. Border bisa diatur lebar, warna, dan gayanya (misal solid, dashed, dotted).
     ```css
     .box {
       border: 2px solid black; /* Border hitam, tebalnya 2px */
     }
     ```
* Padding adalah ruang **di dalam** elemen, antara konten dan border. Jadi, padding menambahkan jarak antara konten elemen dengan tepi border. Padding juga tidak punya warna atau bentuk, tapi menambah ruang di dalam elemen.
     ```css
     .box {
       padding: 10px; /* Jarak 10px di dalam elemen */
     }
     ```

## 4. **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**  
Jawaban:  
* Flexbox dirancang untuk mengatur elemen secara satu dimensi, artinya cocok untuk tata letak elemen secara baris (horizontal) atau kolom (vertikal), tapi fokusnya lebih ke salah satu arah tersebut. Berguna saat ingin membuat elemen dalam satu baris atau kolom yang bisa dengan mudah diatur agar responsif dan rapi.
* Grid memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan, cocok untuk tata letak yang lebih kompleks. Berguna saat ingin mengatur layout halaman secara keseluruhan dengan baris dan kolom, misalnya seperti tata letak halaman majalah atau dashboard dengan berbagai komponen.

## 5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**
Jawaban:  
Langkah pertama yang saya lakukan adalah menambahkan fungsi baru di views.py, yaitu `edit_candy` dan `delete_candy`, yang masing-masing berfungsi untuk mengedit dan menghapus produk yang sudah ada. Setelah mengimplementasikan kedua fungsi tersebut, saya menambahkan path-nya ke `urls.py` di aplikasi utama. Kemudian, saya membuat folder `static` untuk menyimpan file CSS. Saya juga melakukan penyesuaian pada `settings.py` agar aplikasi bisa menggunakan static files tersebut. Selanjutnya, saya mengubah `base.html` untuk menggunakan Tailwind CSS. Saya juga membuat navbar, `navbar.html` yang digunakan di `main.html`. Saya menyesuaikan semua tampilan HTML agar sesuai dengan preferensi saya dengan mencari inspirasi dari internet. Selain itu, saya juga melakukan penyesuaian pada `login.html` dan `register.html` agar sesuai dengan keinginan saya. Untuk desain keseluruhan aplikasi, saya menggunakan Tailwind CSS dan mengedit file `global.css` guna mendefinisikan gaya tampilan aplikasi.
</details>

<details>
  <summary>Tugas 6</summary>

# Tugas 6
## 1. **Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**
Jawaban:  
JavaScript merupakan bahasa pemrograman esensial dalam pengembangan aplikasi web karena kemampuannya meningkatkan dinamika dan interaktivitas halaman web. Berikut adalah beberapa manfaat utama dari penggunaan JavaScript:

* Responsivitas dan Interaktivitas  
JavaScript memungkinkan halaman web untuk merespons aksi pengguna secara cepat, mengubah tata letak konten, dan menyediakan pembaruan real-time tanpa perlu memuat ulang seluruh halaman. Hal ini menjadikan aplikasi web terasa lebih dinamis dan meningkatkan pengalaman pengguna.
* Pemrograman Asinkron  
Dengan teknologi seperti AJAX dan fungsi `fetch()`, JavaScript memungkinkan pemrosesan data dari server secara asinkron, sehingga interaksi dalam aplikasi tidak mengganggu pengalaman pengguna secara keseluruhan.
* Validasi Input di Sisi Klien  
JavaScript memfasilitasi validasi input sebelum data dikirim ke server, mengurangi risiko kesalahan dan beban pada backend.
* Kompatibilitas Lintas Platform  
JavaScript mendukung berbagai platform dan browser, membuat aplikasi web dapat diakses dari berbagai perangkat dan sistem operasi tanpa hambatan.
* Integrasi dengan API Eksternal  
JavaScript sangat efektif dalam mengintegrasikan API eksternal, memungkinkan aplikasi untuk menampilkan data dari sumber lain secara dinamis dan kaya.
* Pengembangan Mobile  
JavaScript juga memudahkan pengembangan lintas platform, sehingga pengembang dapat menggunakan satu bahasa pemrograman untuk berbagai platform, baik itu web atau mobile.

## 2. **Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**  
Jawaban:  
Menggunakan `await` dalam `fetch()` adalah esensial dalam pengembangan aplikasi web menggunakan JavaScript karena memungkinkan penghentian sementara eksekusi kode selanjutnya hingga operasi asinkron dari `fetch()` selesai. Fungsi `await` menunggu hingga data respons siap digunakan, memastikan bahwa program tidak melanjutkan eksekusi tanpa data yang diperlukan. Jika `await` tidak digunakan, hasil dari `fetch()` akan berstatus promise yang masih pending, yang berarti data belum siap untuk diproses dan variabel yang seharusnya menyimpan data ini mungkin masih kosong atau tidak terisi dengan benar, berpotensi menyebabkan kesalahan dalam aplikasi.

Dalam praktiknya, penggunaan `await` memperjelas alur eksekusi dengan menunggu promise dari `fetch()` terpenuhi, sementara tanpa `await`, kode harus bergantung pada metode `.then()` untuk menangani data yang diterima. Ini membuat kode lebih mudah dibaca dan dikelola, sementara menghindari kesalahan yang dapat terjadi jika data diakses sebelum sepenuhnya tersedia. Tanpa penggunaan `await` atau `.then()`, aplikasi mungkin mengalami kesalahan data atau error selama proses eksekusi karena mencoba menggunakan data yang belum tersedia.

## 3. **Mengapa kita perlu menggunakan decorator `csrf_exempt` pada *view* yang akan digunakan untuk AJAX `POST`?**
Jawaban:  
Menggunakan decorator `csrf_exempt` pada view yang menangani AJAX POST di Django adalah karena beberapa alasan praktis meskipun melibatkan pertimbangan keamanan yang serius. Ketika sebuah aplikasi Django menangani AJAX POST, terutama dari domain yang berbeda atau dalam konteks aplikasi single-page yang tidak memperbarui halaman secara keseluruhan, token CSRF yang diperlukan untuk mengautentikasi permintaan mungkin tidak tersedia karena tidak di-generate secara otomatis tanpa refresh halaman.

Decorator `csrf_exempt` memungkinkan permintaan POST dari sumber AJAX untuk diproses tanpa perlu token CSRF yang biasanya diperlukan oleh Django untuk menghindari serangan Cross-Site Request Forgery. Ini sangat bermanfaat dalam situasi di mana AJAX request hanya berasal dari pengguna yang telah diverifikasi dan dapat dipercaya atau dari bagian aplikasi yang terbatas aksesnya.

Meskipun demikian, mengabaikan pemeriksaan CSRF dapat menimbulkan risiko keamanan, karena menghilangkan salah satu lapisan pertahanan terhadap serangan CSRF. Oleh karena itu, penggunaan `csrf_exempt` harus dilakukan dengan sangat hati-hati. Idealnya, view yang tidak menggunakan pemeriksaan CSRF harus memiliki mekanisme keamanan tambahan untuk memastikan bahwa hanya permintaan yang sah dan aman yang dapat diproses, sehingga meminimalisir potensi risiko serangan.

## 4. **Pada tutorial PBP minggu ini, pembersihan data *input* pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?**  
Jawaban:  
Pembersihan data input pengguna pada backend tetap penting dan tidak dapat sepenuhnya digantikan oleh validasi di frontend karena:

* Keamanan yang Lebih Kuat  
Frontend mudah dimanipulasi pengguna, misalnya dengan menonaktifkan JavaScript atau menggunakan alat seperti Postman. Oleh karena itu, backend perlu mengonfirmasi keamanan dan kebenaran data sebelum diproses lebih lanjut.

* Integritas Data Terjaga  
Backend mengontrol dan memastikan semua data yang masuk ke dalam sistem memenuhi standar dan aturan yang telah ditetapkan. Hal ini penting untuk mencegah data yang tidak valid atau berbahaya memasuki sistem.

* Perlindungan dari Serangan  
Backend berperan krusial dalam menghindari serangan seperti SQL injection atau cross-site scripting (XSS) yang dapat terjadi jika data yang masuk tidak disanitasi dengan baik.

* Validasi Data yang Kompleks  
Validasi yang memerlukan akses database atau pemeriksaan terhadap aturan bisnis tertentu tidak dapat dilakukan di frontend. Backend menyediakan kemampuan untuk melakukan validasi yang lebih kompleks ini.

* Efisiensi Penggunaan Sumber Daya  
Validasi di backend mengurangi beban pada frontend, memungkinkan aplikasi berjalan lebih ringan dan responsif pada perangkat pengguna.

Pembersihan data di backend bukan hanya tentang keamanan, tetapi juga tentang menjaga kualitas data yang dikelola dan diproses oleh sistem, memastikan aplikasi beroperasi dengan efisien dan aman dari potensi serangan.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!
Jawaban:  
Saya menambahkan fungsi baru yaitu `add_candy_entry_ajax` pada `views.py`. Ini adalah method utama yang digunakan untuk menambahkan candy baru menggunakan ajax dan menambahkan candy barunya ke dalam basis data. Kemudian di `main.html` saya mengganti kode yang menampilkan candy list sebelumnya dengan `<div id="candy_entry_cards"></div>`. Lalu saya juga menambahkan modal, yaitu form yang akan muncul sebagai pop up ketika nanti saya ingin menambahkan candy by AJAX. dan saya juga menambahkan buttonnya. Kemudian di `main.html` saya membuat beberapa fungsi javascript yaitu `showModal()` dan `hideModal()` untuk menampilkan form modal, dan juga menghide modal. Selanjutnya ada fungsi `getCandyEntries()` yang akan me-fetch data dan mengubahnya menjadi object JavaScript dan `refreshItemEntries()` yang berguna untuk merefresh data item yang akan ditampilkan di web secara ansikronus. Selanjutnya, saya menambahkan `addCandyEntry()` yang mengambil data dari form modal, dan menambahkannya ke database untuk ditampilkan, dan merefresh content (bukan page) dengan memanggil `refreshItemEntries()`. Terakhir, saya juga melakukan `strip_tags` untuk membersihkan data baru.
</details>