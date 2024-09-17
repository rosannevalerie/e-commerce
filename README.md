**URL Deployment PWS: https://rosanne-valerie-ecommerce.pbp.cs.ui.ac.id/**

# TUGAS 1
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

# TUGAS 2
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
<img src="ecommerce_json.png"> 
<img src="ecommerce_xml.png"> 
<img src="ecommerce_json_id.png">   
<img src="ecommerce_xml_id.png">   