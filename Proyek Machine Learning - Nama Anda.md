# Proyek Machine Learning - Zulfikar Setyo Priyambudi

---

## 1. Domain Proyek

**Latar Belakang:**
Performa akademik siswa merupakan indikator utama keberhasilan pendidikan. Berbagai faktor seperti waktu belajar, kehadiran, dukungan keluarga, akses internet, dan kegiatan ekstrakurikuler diyakini memainkan peran penting dalam menentukan hasil belajar. Namun, sering kali sulit untuk menentukan fitur mana yang paling berpengaruh dan bagaimana memanfaatkan data tersebut secara optimal agar dapat mendukung intervensi dan strategi peningkatan mutu pendidikan.

**Mengapa masalah ini perlu diselesaikan?**
Pemahaman mendalam mengenai faktor-faktor yang mempengaruhi performa siswa dapat membantu pendidik dan pembuat kebijakan dalam merancang intervensi yang tepat, mengalokasikan sumber daya secara efisien, dan mengembangkan strategi yang dapat meningkatkan kualitas pembelajaran secara keseluruhan.

**Referensi Penelitian:**
Studi yang dilakukan oleh Priyambudi dan Nugroho tahun 2024 telah menunjukkan hubungan signifikan antara dukungan lingkungan, motivasi, dan kualitas akses sumber belajar dengan hasil akademik siswa. selain itu pada penelitian yang dilakukan oleh Farooq dkk tahun 2011 menunjukan bahawa selain faktor internal, yaitu nilai akademik siswa dan kegiatan di sekolah, faktor eksternal seperti ekonomi keluarga, pendidikan orang tua, dan pekerjaan orang tua juga berpengaruh dalam performa belajar siswa.

Dari Referensi-referensi tersebut mendukung urgensi penyelesaian masalah ini dari sudut pandang ilmiah dan praktis.

**Daftar Pustaka:**
- Zulfikar Setyo Priyambudi, Yusuf Sulistyo Nugroho; Which algorithm is better? An implementation of normalization to predict student performance. AIP Conf. Proc. 17 January 2024; 2926 (1): 020110 ([tautan Penelitian](https://doi.org/10.1063/5.0182879))
- Farooq M.S., Chaudhry A.H., Shafiq M, Berhanu G. Factors Affecting Students’ Quality of Academic Performance: A Case of Secondary School Level. Journal of quality and technology management. 2011;7(2):1–14. ([tautan Penelitian](https://www.researchgate.net/publication/284150574_Factors_affecting_students'_quality_of_academic_performance_A_case_of_secondary_school_level))

---

## 2. Business Understanding

### Problem Statements

- **Pernyataan Masalah 1:**
    *Bagaimana mengidentifikasi faktor-faktor utama yang mempengaruhi performa akademik siswa?*
    **Penjelasan:** Banyak variabel, baik internal maupun eksternal, berpotensi mempengaruhi hasil belajar, namun belum diketahui secara pasti mana yang memiliki pengaruh paling dominan.

- **Pernyataan Masalah 2:**
*Bagaimana mengembangkan model prediksi yang optimal dan robust sehingga dapat digunakan sebagai alat bantu pengambilan keputusan pendidikan?*
**Penjelasan:** Membangun model dengan performa tinggi dan kestabilan yang terjamin dapat membantu sekolah/instansi dalam mengidentifikasi siswa yang berisiko serta mengarahkan intervensi yang tepat.

### Goals

- **Goal 1:**
Mengidentifikasi fitur paling kritis melalui analisis eksplorasi data dan teknik feature importance (misalnya, analisis koefisien dari Linear Regression).
*Jawaban:* Melalui analisis, ditemukan bahwa dukungan sosial (misalnya, Peer Influence) dan akses sumber belajar (misalnya, Internet Access) memiliki pengaruh positif signifikan, sedangkan faktor seperti akses yang rendah dan keterlibatan orang tua yang minim berdampak negatif.

- **Goal 2:**
Mengembangkan dan membandingkan performa berbagai model (Linear Regression, SVR, Random Forest, XGBoost) untuk prediksi nilai ujian siswa.
*Jawaban:* Dengan menggunakan evaluasi berbasis metrik seperti MSE, RMSE, MAE, dan R², serta validasi silang, akan dipilih model yang memberikan kinerja terbaik dan generalisasi tinggi.

### Solution Statements

- **Solution Statement 1:**
Menggunakan pendekatan multialgoritma dengan membangun model prediksi menggunakan Linear Regression, SVR, Random Forest, dan XGBoost. Pendekatan ini bertujuan untuk mengevaluasi kemampuan masing-masing model dalam menangkap hubungan antar fitur dan hasil belajar siswa.

- **Solution Statement 2:**
Melakukan optimasi hyperparameter dengan teknik RandomizedSearchCV dan validasi silang (cross-validation) pada model-model non-linear (SVR, Random Forest, XGBoost) untuk memastikan bahwa solusi yang diambil tidak hanya optimal secara numerik tetapi juga robust terhadap variasi data.

---

## 3. Data Understanding

**Informasi Dataset:**
Dataset *Student Performance Factors* diperoleh dari Kaggle ([tautan dataset](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)).
Dataset ini menyediakan gambaran yang komprehensif mengenai berbagai faktor yang mempengaruhi kinerja akademik siswa dalam ujian. Data ini mencakup informasi seputar kebiasaan belajar, kehadiran di kelas, keterlibatan orang tua, serta faktor lain yang berkontribusi terhadap keberhasilan akademis siswa.

Berikut informasi pada dataset :
- Dataset memiliki format CSV (Comma-Seperated Values).
- Dataset memiliki 6,607 sample dengan 20 fitur.
- Tidak ada missing value dalam dataset.

**Deskripsi Fitur / Variabel pada Data**
Berikut adalah penjabaran lengkap dari masing-masing variabel yang terdapat dalam dataset:

1. Hours_Studied
Deskripsi: Jumlah jam yang dihabiskan siswa untuk belajar setiap minggunya. Variabel ini memberikan indikasi seberapa banyak waktu yang dicurahkan siswa untuk belajar dan mempersiapkan diri menghadapi ujian.
2. Attendance
Deskripsi: Persentase kehadiran siswa di kelas. Variabel ini menunjukkan seberapa konsisten siswa dalam mengikuti proses pembelajaran di sekolah.
3. Parental_Involvement
Deskripsi: Tingkat keterlibatan orang tua dalam pendidikan siswa, yang dikelompokkan menjadi kategori Low, Medium, dan High. Informasi ini membantu dalam memahami sejauh mana dukungan orang tua terhadap prestasi akademik anak mereka.
4. Access_to_Resources
Deskripsi: Ketersediaan sumber daya pendidikan yang dapat diakses siswa, seperti buku, perpustakaan, dan fasilitas belajar lainnya, yang dikategorikan menjadi Low, Medium, dan High. Variabel ini mencerminkan sejauh mana lingkungan pendidikan mendukung proses pembelajaran siswa.
5. Extracurricular_Activities
Deskripsi: Partisipasi siswa dalam kegiatan ekstrakurikuler (Yes, No). Variabel ini mengidentifikasi apakah siswa mengikuti kegiatan di luar pelajaran formal yang dapat memberikan pengaruh positif maupun negatif terhadap kinerja akademis.
6. Sleep_Hours
Deskripsi: Rata-rata jumlah jam tidur siswa setiap malam. Informasi ini penting karena kualitas dan durasi tidur dapat berpengaruh besar terhadap konsentrasi dan kinerja akademik.
7. Previous_Scores
Deskripsi: Nilai yang diperoleh siswa pada ujian sebelumnya. Variabel ini berguna untuk menilai tren kinerja akademik dan sebagai indikator prediktif terhadap nilai akhir.
8. Motivation_Level
Deskripsi: Tingkat motivasi siswa, dikategorikan menjadi Low, Medium, dan High. Variabel ini menggambarkan semangat dan keinginan siswa dalam mencapai prestasi akademik yang lebih baik.

9. Internet_Access
Deskripsi: Ketersediaan akses internet bagi siswa (Yes, No). Akses internet merupakan faktor pendukung penting terutama dalam era digital untuk mencari informasi dan bahan belajar tambahan.

10. Tutoring_Sessions
Deskripsi: Jumlah sesi bimbingan belajar yang diikuti siswa setiap bulannya. Informasi ini menunjukkan seberapa sering siswa mendapatkan bantuan tambahan di luar pelajaran formal untuk meningkatkan pemahaman materi.

11. Family_Income
Deskripsi: Tingkat pendapatan keluarga, yang dikelompokkan ke dalam kategori Low, Medium, dan High. Variabel ini dapat memengaruhi berbagai aspek pendidikan, termasuk akses terhadap sumber daya dan dukungan ekstra akademik.

12. Teacher_Quality
Deskripsi: Kualitas pengajaran yang diberikan oleh guru, dikategorikan menjadi Low, Medium, dan High. Faktor ini merupakan elemen penting dalam proses belajar mengajar dan berdampak langsung pada kemampuan siswa.

13. School_Type
Deskripsi: Jenis sekolah yang dihadiri siswa, misalnya Public atau Private. Variabel ini membantu mengidentifikasi perbedaan metode pengajaran dan fasilitas yang tersedia di berbagai jenis sekolah.

14. Peer_Influence
Deskripsi: Pengaruh teman sebaya terhadap kinerja akademik siswa, dengan kategori Positive, Neutral, dan Negative. Lingkungan sosial dan interaksi dengan teman sekelas dapat memainkan peran besar dalam memotivasi atau menghambat prestasi akademik.

15. Physical_Activity
Deskripsi: Rata-rata jumlah jam aktivitas fisik yang dilakukan siswa setiap minggu. Aktivitas fisik yang cukup dapat membantu dalam meningkatkan konsentrasi dan kesehatan secara keseluruhan yang berdampak positif pada kinerja akademis.

16. Learning_Disabilities
Deskripsi: Indikasi apakah siswa memiliki gangguan belajar (Yes, No). Variabel ini penting untuk memahami tantangan tambahan yang mungkin dihadapi siswa dalam proses belajar.

17. Parental_Education_Level
Deskripsi: Tingkat pendidikan tertinggi yang dicapai oleh orang tua, seperti High School, College, atau Postgraduate. Informasi ini bisa mencerminkan seberapa besar kemungkinan orang tua dapat membantu dalam mendukung kegiatan belajar anaknya.

18. Distance_from_Home
Deskripsi: Jarak dari rumah ke sekolah, dengan kategori seperti Near, Moderate, dan Far. Jarak tempuh yang jauh mungkin mempengaruhi kehadiran dan kesiapan siswa setiap harinya.

19. Gender
Deskripsi: Jenis kelamin siswa (Male, Female). Variabel ini digunakan untuk analisis demografis dan potensi perbedaan performa berdasarkan gender.

20. Exam_Score
Deskripsi: Skor akhir yang diperoleh siswa pada ujian. Variabel inilah yang menjadi indikator utama performa akademik siswa dalam dataset ini.

Data ini mencakup berbagai variabel yang berhubungan dengan kondisi siswa, seperti:

- **Numerik:** Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Tutoring_Sessions, Physical_Activity, Exam_Score.

- **Kategorikal:** Variabel kategori seperti Parental_Involvement, Access_to_Resources, Extracurricular_Activities, Motivation_Level, Internet_Access, Family_Income, School_Type, Peer_Influence, Learning_Disabilities, Gender (setelah encoding).

---

### Tahapan Data Understanding

- Melakukan tahapan EDA seperti mendeskripsikan variabel
- Mengecek data missing value dan membersihkan data missing value
- Mengecek data yang duplikat
- Melihat statistik data yang bernilai int
- Melakukan visualisasi data mulaidari univariate analysis, bivariate analysiss sampai multivariate analysis

### **Exploratory Data Analysis:**

1. **Univariate Analysis:**

**-- Grafik Distribusi Hours Studied**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(2).png)
**Insight:**
grafik ini menunjukkan bahwa sebagian besar individu cenderung menghabiskan waktu belajar di sekitar 20 jam/minggu. Ini terlihat dari puncak grafik yang berada di area tersebut. Bisa kita katakan bahwa 20 jam adalah durasi belajar yang paling umum atau paling banyak dilakukan oleh siswa.
Kedua, distribusi jam belajar ini menyerupai kurva normal, yang artinya sebaran datanya cukup merata di sekitar rata-rata. Meskipun demikian, kita bisa melihat bahwa ada sedikit lebih banyak individu yang belajar di bawah 20 jam dibandingkan yang belajar jauh di atas 20 jam.
Ketiga, penting untuk diperhatikan bahwa hanya sedikit sekali individu yang belajar untuk waktu yang sangat singkat, misalnya di bawah 5 jam, atau sangat lama, misalnya di atas 35 jam. Ini mengindikasikan bahwa sebagian besar individu memiliki durasi belajar yang terpusat.
**Secara keseluruhan,** insight utama dari grafik ini adalah bahwa mayoritas siswa memiliki kecenderungan untuk belajar sekitar 20 jam/minggu, dengan variasi yang tidak terlalu signifikan di antara mereka. Informasi ini bisa berguna untuk memahami pola belajar dan mungkin juga untuk merencanakan alokasi waktu belajar yang efektif

**-- Grafik Boxplot Hours_Studied**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(3).png)
**Insight:**
kita bisa melihat bahwa rentang jam belajar terbanyak (50% data) berada antara sekitar 16 hingga 24 jam. Median, atau nilai tengah dari data, berada di sekitar 21 jam, yang menunjukkan bahwa sebagian besar individu belajar di sekitar durasi ini.
Kedua, whisker pada grafik ini menunjukkan rentang jam belajar yang dianggap 'normal' dalam kelompok ini, yaitu dari sekitar 4 jam hingga 36 jam.
Yang menarik adalah adanya beberapa outlier, baik di sisi bawah maupun sisi atas. Di sisi bawah, kita melihat beberapa individu yang belajar sangat sedikit, bahkan ada yang hanya sekitar 1 atau 2 jam. Ini bisa menjadi indikasi adanya kelompok yang mungkin tidak terlalu terlibat atau memiliki pendekatan belajar yang berbeda.
Dari sisi paling ujung kanan, kita juga melihat beberapa outlier, termasuk satu individu yang belajar hingga lebih dari 40 jam. Ini menunjukkan adanya individu yang menghabiskan waktu belajar yang sangat banyak dibandingkan dengan kelompok lainnya.

**-- Grafik Distribusi Attendance**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(4).png)
**Insight:**
kita bisa melihat bahwa **tingkat kehadiran siswa di satu semester** tidak terdistribusi secara merata. Ada tiga area utama di mana jumlah individu dengan tingkat kehadiran tertentu lebih tinggi dibandingkan area lainnya.
1. Puncak pertama yang cukup signifikan berada pada tingkat kehadiran sekitar 60%. Ini menunjukkan bahwa ada sejumlah besar siswa yang memiliki tingkat kehadiran yang relatif rendah.
2. Puncak yang paling tinggi terlihat pada tingkat kehadiran sekitar 80%. Ini adalah tingkat kehadiran yang paling umum dalam kelompok ini, di mana jumlah individunya paling banyak.
3. Menariknya, kita juga melihat puncak yang cukup tinggi pada tingkat kehadiran 100%. Ini menunjukkan bahwa ada juga sejumlah besar individu yang memiliki catatan kehadiran yang sempurna.

Di sisi lain, kita melihat siswa yang lebih sedikit dengan tingkat kehadiran di sekitar 70-75% dan juga di sekitar 85-90%. Ini mungkin mengindikasikan adanya siswa yang cenderung memiliki tingkat kehadiran yang lebih rendah atau sedikit di bawah sempurna.
**Secara keseluruhan,** grafik ini menunjukkan bahwa tingkat kehadiran siswa di tiap semester ini terkonsentrasi pada beberapa titik tertentu, yaitu di sekitar 60%, 80%, dan 100%. Informasi ini bisa sangat berguna untuk memahami pola partisipasi dan mungkin mengidentifikasi siswa yang memerlukan perhatian lebih terkait dengan kehadiran mereka.


**-- Grafik Boxplot Attendance**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(5).png)
**Insight:**
Dari boxplot ini, kita bisa melihat bahwa rentang tingkat kehadiran untuk sebagian besar siswa (50% data) berada antara 70% hingga 90%. Nilai tengah atau median dari tingkat kehadiran adalah sekitar 80%, yang berarti separuh dari kelompok ini memiliki tingkat kehadiran di bawah 80% dan separuhnya lagi di atasnya.
Rentang kehadiran yang dianggap 'normal' dalam kelompok ini, yang ditunjukkan oleh whisker, adalah dari 60% hingga 100%. Ini berarti bahwa tingkat kehadiran semua individu berada dalam rentang ini dan tidak ada nilai yang dianggap sebagai outlier berdasarkan boxplot ini.

**-- Distribusi Exam_Score**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(6).png)
**Insight:**
Dari grafik ini, kita bisa melihat bagaimana hasil belajar siswa dalam ujian akhir.
Pertama, distribusi skor ujian ini cenderung membentuk kurva condong ke kiri, yang mengindikasikan bahwa sebagian besar individu mendapatkan skor di sekitar nilai rata-rata. Puncak grafik berada di sekitar skor 68 atau 69, yang berarti ini adalah rentang skor yang paling banyak diperoleh.
Kedua, sebaran skor ujian sebagian besar berada antara 60 hingga 75. Ini menunjukkan bahwa sebagian besar individu memiliki tingkat pemahaman atau penguasaan materi yang serupa.
Ketiga, kita melihat adanya sedikit condong negatif pada distribusi ini. Artinya, ada sedikit lebih banyak siswa yang mendapatkan skor sedikit di bawah rata-rata dibandingkan dengan individu yang mendapatkan skor jauh di atas rata-rata. Ini bisa menjadi indikasi bahwa ujian ini mungkin sedikit sulit bagi sebagian besar peserta.
Terakhir, kita melihat adanya kemungkinan beberapa individu yang mendapatkan skor sangat rendah, di sekitar 55. Ini bisa menjadi perhatian dan mungkin perlu diinvestigasi lebih lanjut untuk memahami alasan di baliknya. Namun, secara keseluruhan, distribusi skor ujian ini menunjukkan bahwa sebagian besar peserta memiliki kinerja yang cukup terpusat di sekitar nilai 68 atau 69.

**--  Boxplot Exam_Score**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(7).png)
**Insight:**

Dari boxplot ini, kita bisa melihat bahwa rentang skor ujian untuk sebagian besar individu (50% data) sangat sempit, yaitu antara 66 hingga 70. Median skor berada di sekitar 69, yang menunjukkan bahwa nilai tengah dari skor ujian adalah 69.
Rentang skor yang dianggap 'normal' dalam kelompok ini, yang ditunjukkan oleh whisker, adalah dari 58 hingga 76.
Yang menarik adalah adanya sejumlah outlier, terutama di sisi kanan. Kita melihat banyak individu yang mendapatkan skor jauh di atas batas atas, bahkan mencapai skor sempurna 100. Ini menunjukkan adanya kelompok dengan performa yang sangat tinggi dalam ujian ini.
Di sisi kiri, kita juga melihat beberapa outlier dengan skor yang sangat rendah, di sekitar 55. Ini menunjukkan adanya individu yang performanya jauh di bawah rata-rata kelompok.
Keberadaan outlier di kedua sisi ini memberikan informasi penting. Skor rendah mungkin mengindikasikan perlunya bantuan belajar kepada siswa tersebut, sementara skor tinggi menunjukkan adanya potensi atau penguasaan materi yang sangat baik. Distribusi yang cenderung sempit di bagian tengah namun dengan banyak outlier di atas juga bisa mengindikasikan bahwa ujian ini mungkin cukup membedakan antara mereka yang benar-benar menguasai materi dan yang tidak.

**-- Grafik Kategorikal Data**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(8).png)
**Insight:**

**Distribusi Parental Involvement**: "Diagram pertama ini menunjukkan tingkat keterlibatan orang tua. Kita bisa melihat bahwa sebagian besar siswa yang memiliki hasil ujian yang bagus memiliki tingkat keterlibatan orang tua yang tinggi. Ini mengindikasikan adanya dukungan yang kuat dari keluarga dalam kegiatan belajar maupun akademik lainnya dari siswa tersebut."

**Distribusi Access to Resources**: "Diagram selanjutnya menggambarkan akses terhadap sumber daya. Mayoritas siswa memiliki akses yang tinggi terhadap sumber daya yang dibutuhkan. Ini merupakan indikator positif yang menunjukkan bahwa sebagian besar individu memiliki fasilitas dan dukungan yang memadai untuk melaksanakan pembelajaran di sekolah."

**Distribusi Extracurricular Activities**: "Diagram ketiga menyoroti partisipasi dalam kegiatan ekstrakurikuler. Terlihat jelas bahwa sebagian besar siswa aktif dalam kegiatan di luar jam formal. Ini menunjukkan adanya minat dan kesempatan siswa untuk mengembangkan diri dan eksplorasi di berbagai bidang."

**Distribusi Motivasi Level**: "Diagram keempat menunjukkan tingkat motivasi. Sebagian besar siswa memiliki tingkat motivasi yang sedang hingga tinggi. Ini adalah hal yang baik karena motivasi yang tinggi seringkali berkorelasi dengan hasil belajar dan pencapaian yang lebih baik."

**Distribusi Internet Access**: "Diagram kelima memperlihatkan akses internet. Hampir seluruh siswa memiliki akses internet. Ini menunjukkan tingkat konektivitas yang sangat baik, yang menjadi sumber informasi dan komunikasi yang penting di era digital ini."

**Distribusi Family Income**: "Diagram keenam menggambarkan distribusi pendapatan keluarga. Sebagian besar individu berasal dari keluarga dengan tingkat pendapatan menengah dan rendah. Informasi ini penting untuk memahami latar belakang sosio-ekonomi tiap siswa."

**Distribusi School Type**: "Diagram ketujuh menunjukkan jenis sekolah. Mayoritas siswa bersekolah di sekolah negeri. Ini memberikan gambaran tentang preferensi latar belakang siswa yang bersekolah di sekolah negeri."

**Distribusi Peer Influence**: "Diagram kedelapan menyoroti pengaruh teman sebaya. Sebagian besar siswa merasakan pengaruh positif dari teman-teman mereka. Ini menunjukkan lingkungan sosial yang mendukung dan konstruktif."

**Distribusi Learning Disabilities**: "Diagram kesembilan menunjukkan keberadaan kesulitan belajar. Sebagian besar individu tidak memiliki kesulitan belajar yang teridentifikasi. Ini adalah indikasi yang baik terkait dengan kemampuan belajar secara umum."

**Distribusi Gender**: "Diagram kesepuluh menampilkan distribusi jenis kelamin. Jumlah siswa laki-laki sedikit lebih banyak dibandingkan perempuan, namun perbedaannya tidak signifikan. Ini menunjukkan keseimbangan gender yang relatif baik."

**Simpulan Insight**:
Secara keseluruhan, dari analisis kesepuluh diagram ini, kita dapat menyimpulkan bahwa kelompok siswa yang kita amati sebagian besar memiliki dukungan keluarga yang kuat, akses sumber daya dan internet yang baik, aktif dalam kegiatan ekstrakurikuler, dan memiliki tingkat motivasi yang cukup tinggi. Meskipun sebagian besar berasal dari keluarga dengan pendapatan menengah dan rendah serta bersekolah di sekolah negeri, mereka merasakan pengaruh positif dari teman sebaya dan mayoritas tidak memiliki kesulitan belajar.

- **Bivariate Analysis:**

**-- Hours_Studied vs Exam_Score**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(9).png)
**Insight:**

Dari grafik ini, kita bisa melihat adanya korelasi yang cukup jelas antara kedua variabel tersebut.
Secara umum, semakin banyak waktu yang dihabiskan untuk belajar, cenderung semakin tinggi pula skor ujian yang didapatkan. Ini terlihat dari pola titik-titik yang bergerak naik ke kanan dan juga dari garis merah yang memiliki kemiringan positif. Garis merah ini membantu kita melihat tren umum dalam data.
Namun, penting untuk dicatat bahwa hubungan ini tidak sempurna. Ada variasi dalam skor ujian meskipun dengan jumlah jam belajar yang sama. Ini menunjukkan bahwa faktor-faktor lain, selain waktu belajar, juga berperan dalam menentukan hasil ujian. Misalnya, kemampuan individu, metode belajar, atau bahkan kondisi saat ujian juga bisa mempengaruhi skor.
Kita juga melihat beberapa kasus menarik di mana individu dengan jam belajar yang relatif sedikit mampu mendapatkan skor ujian yang cukup tinggi. Ini mungkin menunjukkan adanya perbedaan dalam efektivitas belajar atau bakat alami.
Secara keseluruhan, insight utama dari grafik ini adalah bahwa waktu yang diinvestasikan dalam belajar memang berkorelasi positif dengan hasil ujian. Meskipun demikian, kita juga perlu mempertimbangkan faktor-faktor lain yang mungkin mempengaruhi nilai dalam ujian

**-- Attendance vs Exam_Score**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(10).png)
**Insight:**

Dari grafik ini, kita bisa melihat adanya korelasi positif, meskipun tidak terlalu kuat, antara seberapa sering seseorang hadir dan seberapa baik mereka mengerjakan ujian.
Secara umum, ada kecenderungan bahwa semakin tinggi tingkat kehadiran seseorang, sedikit lebih tinggi pula skor ujian yang mereka dapatkan. Ini ditunjukkan oleh garis hijau yang memiliki kemiringan positif. Namun, perlu ditekankan bahwa hubungan ini tidaklah mutlak.
Kita melihat sebaran data yang cukup luas, yang berarti **ada banyak faktor lain selain kehadiran yang mempengaruhi skor ujian. Misalnya, kita melihat banyak siswa dengan tingkat kehadiran yang sama namun mendapatkan skor ujian yang berbeda-beda**. Ini menunjukkan bahwa kualitas belajar di kelas, belajar mandiri di luar kelas, pemahaman materi, dan faktor-faktor lainnya juga sangat penting.
Menariknya, kita juga melihat beberapa siswa yang memiliki tingkat kehadiran yang tidak sempurna tetapi mampu meraih skor ujian yang tinggi. Ini mungkin menunjukkan bahwa mereka memiliki kemampuan belajar yang efektif atau mungkin menguasai materi dengan cara lain.
**Kesimpulannya**, meskipun kehadiran di kelas mungkin memberikan kontribusi positif terhadap hasil ujian, faktor-faktor lain juga memiliki peran yang signifikan. Kehadiran saja tidak menjamin skor ujian yang tinggi, dan ketidakhadiran tidak selalu berarti skor yang rendah.

**-- Exam_Score berdasarkan Parental_Involvement**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(11).png)
**Insight:**
Dari grafik ini, kita bisa melihat bagaimana tingkat keterlibatan orang tua dapat berhubungan dengan hasil ujian.
1. Pertama, secara umum, terlihat adanya tren peningkatan median skor ujian seiring dengan meningkatnya tingkat keterlibatan orang tua dalam kegiatan belajar siswa. siswa dengan tingkat keterlibatan orang tua yang tinggi cenderung memiliki median skor ujian yang sedikit lebih tinggi dibandingkan dengan kelompok dengan tingkat keterlibatan sedang dan rendah.

2. Kedua, rentang skor ujian (yang ditunjukkan oleh kotak IQR) untuk ketiga kelompok ini relatif mirip, yaitu sekitar 5 hingga 6 poin. Ini menunjukkan bahwa variabilitas skor di dalam setiap kelompok tidak terlalu berbeda.

3. Ketiga, menarik untuk diperhatikan bahwa kelompok dengan tingkat keterlibatan orang tua yang tinggi memiliki lebih banyak outlier dengan skor ujian yang sangat tinggi. **Ini bisa mengindikasikan bahwa ketika orang tua sangat terlibat, ada kemungkinan lebih besar bagi siswa untuk mencapai potensi maksimal mereka dalam ujian**.

Namun, kita juga melihat adanya outlier dengan skor rendah di semua kelompok, termasuk kelompok dengan tingkat keterlibatan orang tua yang tinggi. **Ini menunjukkan bahwa keterlibatan orang tua bukanlah satu-satunya faktor penentu keberhasilan akademik, dan faktor-faktor lain juga berperan**.

Kesimpulannya, grafik ini memberikan indikasi bahwa tingkat keterlibatan orang tua yang lebih tinggi mungkin berkorelasi dengan skor ujian yang sedikit lebih baik secara umum, dan juga meningkatkan kemungkinan siswa untuk mencapai skor yang sangat tinggi. Meskipun demikian, penting untuk diingat bahwa ada banyak faktor yang mempengaruhi hasil ujian selain keterlibatan orang tua.

**-- Exam_Score berdasarkan School_Type**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(12).png)
**Insight:**

Dari grafik ini, kita dapat melihat beberapa perbedaan dan persamaan dalam distribusi skor ujian berdasarkan asal sekolah sebelumnya dari para siswa.

1. Pertama, secara umum, median skor ujian antara siswa yang pernah sekolah negeri dan swasta tidak terlalu berbeda. Median untuk sekolah swasta sedikit lebih tinggi, namun perbedaannya tidak signifikan. Ini menunjukkan bahwa hasil belajar rata-rata siswa dari kedua asal jenis sekolah ini cenderung serupa.

2. Kedua, rentang skor ujian juga sangat mirip antara kedua jenis sekolah, yaitu sekitar 5 hingga 6 poin. Ini menunjukkan bahwa variabilitas skor di antara siswa dalam setiap jenis sekolah juga tidak jauh berbeda.

3. Ketiga, yang menarik adalah kita melihat banyak outlier dengan skor ujian yang sangat tinggi di kedua jenis sekolah. Ini menunjukkan bahwa baik di sekolah negeri maupun swasta, terdapat siswa-siswa yang mampu mencapai skor yang jauh di atas rata-rata kelompok mereka.

Selain itu, kita juga melihat beberapa outlier dengan skor rendah di kedua jenis sekolah, yang mengindikasikan bahwa siswa dengan kinerja di bawah rata-rata juga ada di kedua tipe sekolah ini.
Kesimpulannya, berdasarkan data ini, **tidak ada perbedaan yang mencolok dalam distribusi skor ujian antara siswa yang sekolah sebelumnya di sekolah negeri dan swasta**. Meskipun median skor di sekolah swasta sedikit lebih tinggi, variabilitas dan keberadaan outlier dengan skor tinggi dan rendah terlihat serupa di kedua jenis sekolah. Faktor-faktor lain di luar jenis sekolah kemungkinan memiliki pengaruh yang lebih besar terhadap hasil ujian siswa.

- **Multivariate Analysis:**

**-- Grafik Korelasi Matriks**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(13).png)
**Insight:**

Heatmap ini memberikan gambaran visual yang cepat tentang seberapa kuat dan ke arah mana variabel-variabel ini saling terkait.

1. Pertama, mari kita fokus pada baris atau kolom yang berkaitan dengan 'Exam_Score' karena ini mungkin menjadi variabel yang paling menarik bagi kita.

2. Kita melihat angka 0.45 di sel yang menghubungkan 'Hours_Studied' dan 'Exam_Score'. Warna sel ini juga cenderung merah muda. Ini menunjukkan adanya korelasi positif yang moderat antara jumlah jam belajar dan skor ujian. Artinya, semakin banyak waktu yang dihabiskan untuk belajar, cenderung semakin tinggi skor ujian yang didapatkan, meskipun hubungannya tidak terlalu kuat.

3. Selanjutnya, kita melihat angka 0.58 di sel yang menghubungkan 'Attendance' dan 'Exam_Score'. Warna sel ini lebih merah dibandingkan sebelumnya. Ini menunjukkan korelasi positif yang lebih kuat antara tingkat kehadiran dan skor ujian. Ini mengindikasikan bahwa siswa yang lebih sering hadir cenderung mendapatkan skor ujian yang lebih tinggi. Korelasi ini terlihat lebih kuat dibandingkan dengan korelasi antara jam belajar dan skor ujian.

4. Untuk variabel 'Sleep_Hours' dan 'Exam_Score', kita melihat angka -0.02. Warna sel ini mendekati putih dengan sedikit sentuhan biru. Ini menunjukkan korelasi negatif yang sangat lemah, hampir tidak ada hubungan linear yang signifikan antara jumlah jam tidur dan skor ujian dalam data ini.

5. Korelasi antara 'Previous_Scores' dan 'Exam_Score' adalah 0.18. Warna sel ini juga cenderung putih dengan sedikit merah muda. Ini menunjukkan korelasi positif yang lemah. Skor ujian sebelumnya memiliki sedikit pengaruh positif terhadap skor ujian saat ini.

6. Untuk 'Tutoring_Sessions' dan 'Exam_Score', koefisien korelasinya adalah 0.16. Warna selnya mirip dengan sebelumnya, menunjukkan korelasi positif yang lemah. Keikutsertaan dalam sesi bimbingan belajar mungkin memiliki sedikit dampak positif pada skor ujian.

7. Terakhir, korelasi antara 'Physical_Activity' dan 'Exam_Score' adalah 0.03. Warna sel ini sangat mendekati putih. Ini menunjukkan korelasi positif yang sangat lemah, hampir tidak ada hubungan linear yang berarti antara aktivitas fisik dan skor ujian dalam data ini.

Selain hubungan dengan skor ujian, kita juga bisa melihat korelasi antar variabel lainnya. Misalnya, ada korelasi positif yang cukup kuat antara 'Hours_Studied' dan 'Attendance' (0.45), yang mungkin menunjukkan bahwa siswa yang lebih banyak belajar juga cenderung lebih sering hadir.

**Kesimpulan Insight:**
Dari heatmap korelasi ini, kita dapat menyimpulkan bahwa faktor-faktor seperti tingkat kehadiran ('Attendance') dan jumlah jam belajar ('Hours_Studied') menunjukkan korelasi positif dengan skor ujian ('Exam_Score'). Tingkat kehadiran tampaknya juga memiliki hubungan yang lebih kuat dengan skor ujian dibandingkan dengan jam belajar. Variabel lain seperti jam tidur, skor sebelumnya di sekolahh lama, sesi bimbingan belajar, dan aktivitas fisik menunjukkan korelasi yang lemah atau hampir tidak ada dengan skor ujian. **Informasi ini dapat membantu kita memfokuskan upaya pada faktor-faktor yang paling mungkin berkontribusi pada peningkatan hasil ujian.**

---
## 4. Data Preparation


1.  **Pembersihan Data:**

- Pemeriksaan missing value dengan `df.isnull().sum()` dan penghapusan kolom yang memiliki nilai kosong dengan `df.dropna(axis=1, inplace=True)`.
- Penghapusan duplikat dengan `df.drop_duplicates(inplace=True)`.
- Melihat ringkasan statistik dengan `df.describe().T` untuk mengidentifikasi potensi outlier.

2. **Handling Outlier:**

- Outlier dihapus dari fitur numerik menggunakan metode IQR. Fungsi `remove_outliers_iqr()` mengidentifikasi dan menghapus nilai yang berada di luar 1.5×IQR setiap fitur.

- Hasilnya, jumlah baris yang tersisa diverifikasi dengan `df_cleaned.shape[0]`.

3. **Encoding:**

- Variabel kategorikal dikonversi menggunakan `pd.get_dummies()` dengan `drop_first=True` agar tidak terjadi dummy trap.

- Konversi tipe data dilakukan dengan `df_cleaned.astype(int)` agar semua fitur menjadi numerik.

#### 1. Penjelasan Proses Data Preparation yang Dilakukan

Pada tahap ini, hal yang dilakukan adalah memastikan kualitas dan konsistensi data sebelum dilakukan pemodelan:

1.  **Pemeriksaan dan Penanganan Missing Value**
    
    -   Mengecek jumlah nilai kosong di setiap kolom dengan `df.isnull().sum()`.
    -   Menghapus kolom yang memiliki proporsi missing value terlalu tinggi (menggunakan `df.dropna(axis=1, inplace=True)`) agar variabel yang tersisa tetap representatif dan tidak mengurangi banyak data.
        
2.  **Penghapusan Duplikat**
    
    -   Mengidentifikasi baris yang terduplikasi dengan `df.duplicated()`.
    -   Menghapus baris-baris duplikat menggunakan `df.drop_duplicates(inplace=True)` untuk menghindari bias ganda pada analisis statistik maupun pelatihan model.
        
3.  **Handling Outlier dengan Metode IQR**
    
    -   Menghitung IQR (interquartile range) = Q3 − Q1 untuk setiap fitur numerik.
    -   Menetapkan batas bawah (Q1 − 1.5×IQR) dan batas atas (Q3 + 1.5×IQR).
    -   Menghapus baris yang memiliki nilai di luar batas tersebut dengan fungsi `remove_outliers_iqr()`.
    -   memastika jumlah baris tersisa setelah cleaning dengan `df_cleaned.shape[0]`.
        
4.  **Encoding Variabel Kategorikal**
    -   Mengidentifikasi kolom-kolom kategorikal (contoh: `Parental_Involvement`, `School_Type`, `Gender`, dll.).
    -   Melakukan encoding menggunakan `pd.get_dummies(df, columns=[…], drop_first=True)` untuk mengonversi setiap kategori menjadi kolom biner (0/1).
        ```python
        categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
        df_cleaned = pd.get_dummies(df_cleaned,
                                    columns=categorical_cols,
                                    drop_first=True)
        ```
        
    -   Menyimpan hasilnya di `df_cleaned` yang siap untuk analisis statistik atau pelatihan model.

5.  **Standardisasi Fitur Numerik**
    
    -   Menggunakan `StandardScaler` dari `sklearn.preprocessing` untuk menormalisasi fitur‑fitur numerik (mis. `Hours_Studied`, `Attendance`, `Sleep_Hours`, `Previous_Scores`, `Physical_Activity`, dll.).
    -   StandardScaler mengubah setiap variabel sehingga memiliki mean = 0 dan standar deviasi = 1:
    -   Hasil `df_scaled` memastikan nilai‑nilai numerik sejajar pada skala yang sama, sehingga satu variabel tidak mendominasi yang lain hanya karena rentang nilainya lebih besar.
        
6.  **Membangun Pipeline untuk Data Preparation dan Modeling**
    -   Menggabungkan tahapan scaler dan modeling (contohnya `RandomForestRegressor`) ke dalam satu objek `Pipeline`:
        ```python
        from sklearn.pipeline import Pipeline
        pipeline = Pipeline([
          ('scaler', StandardScaler()),
          ('model', RandomForestRegressor(n_estimators=100))
        ])
        evaluate_model(pipeline_rf, X_train, y_train, X_test, y_test,  "Random Forest Regressor")
        ```
    -   Dengan pipeline, saat melakukan `fit()` dan `predict()`, semua langkah preprocessing dan modeling dieksekusi secara berurutan dan konsisten.
        
----------

#### 2. Alasan Mengapa Tahapan Data Preparation Diperlukan

 1.  **Menangani Missing Value**
   - **Mengurangi bias**: Data yang hilang (missing) dapat menyebabkan model mempelajari pola yang tidak lengkap, sehingga menurunkan akurasi prediksi.
    -   **Menjaga integritas variabel**: Kolom dengan terlalu banyak missing value seringkali tidak menambah informasi signifikan dan justru memperumit proses modeling.
        
2.    **Menghapus Duplikat**
   
   -   **Mencegah over‑representasi**: Baris yang terduplikasi berakibat statistik (rata‑rata, median) dan model machine learning bisa menjadi tidak seimbang. Sehingga saat melakukan analisis data akan terjadi bias
    -   **Mempercepat proses**: Dataset yang lebih ringkas mengurangi beban komputasi tanpa kehilangan informasi baru.
        
3.   **Analisis Deteksi Outlier**
        
   -   **Dampak outlier**: Outlier  bisa merusak perhitungan mean, varians, dan bahkan mempengaruhi parameter model (misalnya koefisien regresi), sehingga mengurangi kemampuan model untuk memahami data.
        
-   **Penghapusan Outlier dengan Metode IQR**
    
    -   **Mempertahankan konsistensi**: Metode IQR bersifat non‑parametrik dan tidak terpengaruh asumsi distribusi normal, sehingga cocok untuk data nyata yang seringkali skewed / condong ke satu sisi.
    -   **Meningkatkan performa model**: Dengan mengeliminasi nilai ekstrem, model dapat “fokus” pada pola yang umum, mengurangi risiko overfitting pada noise atau anomali.

**4. Alasan Pemilihan `get_dummies` dibanding LabelEncoder atau OneHotEncoder dari sklearn**
	1.  **Tidak ada asumsi urutan:** Semua fitur kategorikal diubah jadi kolom biner—model tidak akan “mengira” ada ranking antar kategori.
	2.  **Cepat dan langsung bisa dibaca:** Hasilnya langsung dalam bentuk DataFrame dengan header kolom yang jelas, memudahkan inspeksi dan visualisasi.

Sedangkan **LabelEncoder** Berisiko memicu bias pada model yang menganggap angka lebih besar = lebih penting., dan **OneHotEncoder** – Harus di- _import_  dan di - _fit_transform_ secara eksplisit. Output-nya juga berupa array atau sparse matrix, perlu dikonversi ke DataFrame jika ingin lihat nama kolom. `pd.get_dummies` adalah pilihan yang **efisien** dan **straight‑forward**.

**5.  Alasan Pemilihan Standard Scaler dan Pipeline**
	-   **Standard Scaler**
	    1.  **Menyetarakan skala fitur**: Banyak algoritma (seperti K‑Nearest Neighbors, SVM, regresi, dan neural network) sensitif terhadap skala. Tanpa standardisasi, fitur dengan rentang besar bisa “mendominasi” perhitungan jarak atau gradien.
	    2.  **Mempercepat konvergensi**: Pada algoritma berbasis optimasi (gradient descent), data yang ter‐standardisasi dapat membuat perhitungan koefisien lebih stabil dan cepat mencapai titik minimum.

**Pipeline**
	    1.  **Mencegah Data Leakage**: Semua transformasi (imputasi, encoding, scaling) dilatih hanya pada data pelatihan saat `.fit()`—transformasi yang sama kemudian diterapkan ke data validasi/test tanpa “mencuri” informasi statistik (mean, std, dll.) dari data uji.
	    2.  **Reproduksibilitas & Kebersihan Kode**: Daripada menulis ulang serangkaian transformasi berulang kali, pipeline menyatukan semua langkah dalam satu objek. Ini memudahkan tracking, tuning hyperparameter, dan kolaborasi tim.
	    3.  **Integrasi Mudah dengan Cross‑Validation / GridSearch**: Dengan pipeline, bisa langsung melakukan `GridSearchCV(pipeline, params)` dan seluruh proses preprocessing akan terjadi otomatis pada setiap fold, menjamin validitas evaluasi model.
	    
Dengan menambahkan **Standard Scaler** dan **Pipeline**, proses data preparation menjadi lebih **terstruktur**, **aman** dari kebocoran data, serta **efisien** dalam hal pengembangan dan evaluasi model.



## 5. Modeling

Pada tahap Modeling, ini hal yang dilakukan adalah membangun dan membandingkan empat algoritma regresi untuk menyelesaikan permasalahan prediksi skor ujian (Exam_Score). Setiap model di‑implementasikan dalam sebuah pipeline yang menggabungkan pra‑pemrosesan (scaling) dan estimator, agar alur kerja otomatis, terukur, dan mudah direproduksi.

1.  **Persiapan Data**
    -   Fitur (`X`) dan target (`y`) dipisahkan dari `df_cleaned`.
    -   Data dibagi menjadi **train** (80 %) dan **test** (20 %) menggunakan `train_test_split(random_state=42)`.
        
2.  **Pipeline & Parameter Default**  
    Semua pipeline menggunakan
    ```python
    ('scaler', StandardScaler())
    ```
    untuk menstandarkan skala fitur, penting agar model seperti SVR bekerja optimal. Estimator yang digunakan:
    -   **Linear Regression**
        
        ```python
        ('lr', LinearRegression())
        ```
        
        – tidak memiliki hyperparameter utama selain `fit_intercept` (default dipakai).
        
    -   **Support Vector Regressor (SVR)**
        
        ```python
        ('svr', SVR())
        ```
        
        – default menggunakan kernel RBF.
        
    -   **Random Forest Regressor**
        
        ```python
        ('rf', RandomForestRegressor(random_state=42))
        ```
        
        – default `n_estimators=100`, `max_depth=None`, dsb.
        
    -   **XGBoost Regressor**
        
        ```python
        ('xgb', XGBRegressor(objective='reg:squarederror', random_state=42))
        ```
        
3.  **Hyperparameter Tuning dengan RandomizedSearchCV**  
    Untuk model non‑linear (SVR, Random Forest, XGBoost), kami menerapkan **RandomizedSearchCV** (n_iter=20, cv=5, scoring='r2', random_state=42, n_jobs=-1) untuk menemukan kombinasi parameter optimal:
    
    -   **SVR**
        
        ```python
        'model__C'        : logspace(-2, 2, 50),  
        'model__epsilon'  : linspace(0.01, 1.0, 50),  
        'model__kernel'   : ['rbf','linear']  
        
        ```
        
    -   **Random Forest**
        
        ```python
        'model__n_estimators'    : [100,200,300],  
        'model__max_depth'       : [None,10,20,30],  
        'model__min_samples_split': [2,5,10],  
        'model__min_samples_leaf' : [1,2,4]  
        
        ```
        
    -   **XGBoost**
        
        ```python
        'model__n_estimators'  : [100,200,300],  
        'model__max_depth'     : [3,6,10],  
        'model__learning_rate' : [0.01,0.1,0.2],  
        'model__subsample'     : [0.6,0.8,1.0]  
        
        ```
Setiap pencarian parameter menghasilkan `best_estimator_`, yang kemudian digunakan untuk prediksi dan evaluasi.
    
4.  **Evaluasi & Perbandingan Model**  
    Untuk semua model (default & tuned) kami menghitung metrik:
    -   **Test MSE**, **Test RMSE**, **Test MAE**,
    -   **Test R²** (koefisien determinasi),
    -   **CV R² Mean** & **CV R² Std** via `cross_val_score(pipeline, X_train, y_train, cv=5)`.
    Hasil evaluasi disimpan dalam tabel terurut berdasarkan **Test R²** dari tertinggi ke terendah.

- **Feature Importance & Multikolinearitas:**
    - Koefisien Linear Regression dianalisis untuk menemukan fitur dengan pengaruh positif dan negatif.
    - VIF (Variance Inflation Factor) dihitung menggunakan `variance_inflation_factor()` guna mendeteksi adanya multikolinearitas di antara fitur.
---

**Kelebihan & Kekurangan Tiap Algoritma**
-   **Linear Regression**
    -   _Kelebihan:_
        -   Sangat **interpretatif**: koefisien langsung menggambarkan efek tiap fitur.
        -   **Cepat** dilatih dan diprediksi, cocok sebagai baseline.
        -   Stabil pada data dengan hubungan linier dan sedikit noise.
    -   _Kekurangan:_
        -   **Tidak mampu menangkap non‑linearitas**—jika pola data kompleks, akurasi bisa terbatasi.
        -   Rentan terhadap **multikolinearitas** di antara fitur (meski bisa diatasi dengan Ridge/Lasso).
            
-   **Support Vector Regressor (SVR)**
    -   _Kelebihan:_
        -   Efektif untuk **hubungan non‑linear** berkat penggunaan kernel (rbf, polynomial, linear).
        -   Dapat menangani **outlier** lebih baik jika parameter ε dan C disetel dengan tepat.
    -   _Kekurangan:_
        -   **Perlu tuning yang cermat** (C, epsilon, kernel) untuk performa optimal—tanpa tuning default SVR kalah dari model sederhan
        -   **Kurang scalable** untuk dataset sangat besar 
-   **Random Forest Regressor**
    -   _Kelebihan:_
        -   Mampu menangkap **non‑linearitas** dan **interaksi antar fitur** secara otomatis.
        -   Cenderung **robust** terhadap outlier dan fitur yang saling berkorelasi.
        -   Memberikan **feature importance** built‑in.
    -   _Kekurangan:_
        -   **Rawan overfitting** jika pohon terlalu dalam atau tidak dituning (`n_estimators`, `max_depth`, dst.).
        -   Model kompleks—**kurang interpretatif** dibanding koefisien linear.
-   **XGBoost Regressor**
    -   _Kelebihan:_
        -   Menggabungkan **gradient boosting** dengan regularisasi (L1/L2), sangat **powerful** untuk data non‑linear dan sparsity.
        -   Dapat menangani **missing value** dan memberikan **kontrol kedalaman** via `max_depth`, `subsample`, `learning_rate`.
        -   **Scalable** dengan dukungan training paralel dan handling dataset besar.
    -   _Kekurangan:_
        -   **Hyperparameter banyak**, memerlukan tuning lebih luas (n_estimators, learning_rate, max_depth, subsample) agar tidak overfitting.
        -   Training dan tuning bisa **memakan waktu** jika parameter tidak diatur dengan baik.

----------

### Proses Improvement Tuning & Validasi

Semua model non‑linear (SVR, Random Forest, XGBoost) dioptimasi menggunakan **RandomizedSearchCV** dengan **5‑fold cross‑validation**. Ini memastikan bahwa:

1.  **Hyperparameter** dicari di ruang parameter yang luas secara acak—efisien untuk banyak kombinasi.
2.  **Cross‑validation** menjamin performa model **konsisten** di berbagai subset data, mengurangi risiko overfitting dan memastikan generalisasi yang baik.

---
### Hasil Model Terbaik
 **SVR (Support Vector Regressor - Tuning)**

-   **Test R²: 0.9544**, tertinggi dari semua model → sangat akurat dalam menjelaskan variabilitas data uji.
-   **MAE & RMSE terendah**, menunjukkan error absolut dan rata-rata kuadrat terkecil.
-   **CV R² Mean: 0.9563**  &  **CV Std: 0.0025**, artinya performanya  **sangat konsisten**  di berbagai lipatan cross-validation.
-   🔧  **Best Params**: Kernel linear dan epsilon optimal — cocok untuk data dengan hubungan linear sederhana.

  **Insight**:  
Model ini paling unggul dalam hal akurasi dan konsistensi. Cocok untuk dataset berskala kecil hingga sedang dengan hubungan linear antar fitur dan target.
  

📊 **Ringkasan Evaluasi Model**

  

| No | Model | Test R² | Test RMSE | Test MAE | CV R² Mean | CV R² Std | Insight |
| ---- | ----------------------------------- | ----------| ----------- | ---------- | ------------ |----------- |------------------------------------------------------------------------ |
| 0 |  **SVR (Tuning)**  |  **0.9544**  |  **0.6765**  |  **0.5412**  |  **0.9563**  |  **0.0025**  | 🔥 Akurasi terbaik & sangat konsisten; kernel linear & epsilon optimal. Cocok untuk data dengan relasi linear. |
| 1 |  **Linear Regression**  | 0.9542 | 0.6775 | 0.5422 | 0.9564 | 0.0024 | ⚖️ Performa hampir identik dengan SVR (Tuning), tanpa tuning. Sederhana namun kuat untuk data linear. |
| 2 | XGBoost Regressor (Tuning) | 0.9435 | 0.7525 | 0.6004 | 0.9478 | 0.0038 | ⚡ Akurat & stabil, cocok untuk data kompleks. Perlu tuning untuk performa optimal. |
| 3 | SVR (Default) | 0.9388 | 0.7836 | 0.6252 | 0.9381 | 0.0044 | 👍 Masih cukup baik tanpa tuning, tapi kalah dari SVR (Tuning) & Linear Regression. |
| 4 | XGBoost Regressor (Default) | 0.9158 | 0.9189 | 0.7312 | 0.9205 | 0.0057 | 📉 Menurun tanpa tuning, tapi tetap unggul dari Random Forest. |
| 5 | Random Forest Regressor (Tuning) | 0.8502 | 1.2256 | 0.9661 | 0.8674 | 0.0072 | ❗ Akurasi rendah & error tinggi meski sudah dituning. Overfitting atau kurang cocok untuk data ini. |
| 6 | Random Forest Regressor (Default) | 0.8484 | 1.2332 | 0.9715 | 0.8658 | 0.0075 | ⚠️ Hasil hampir sama dengan versi tuning. Performa paling lemah. |



🧠 **Insight Umum**

  

- ✅ **Model terbaik secara keseluruhan**:

**SVR (Tuning)** dan **Linear Regression** menonjol dengan akurasi tinggi dan konsistensi luar biasa. Sangat cocok untuk hubungan yang mendekati linear antara fitur dan target.

  

- ⚡ **XGBoost** adalah alternatif kuat dan fleksibel untuk dataset yang mungkin lebih kompleks.

Versi tuning lebih unggul signifikan dibanding versi default.

  

- ❌ **Random Forest** tidak memberikan hasil yang kompetitif dalam eksperimen ini. Baik versi default maupun tuning menunjukkan error tinggi dan variansi performa yang lebih besar antar fold CV.


 🏁 **Rekomendasi Akhir**


| Kebutuhan | Model yang Direkomendasikan |
|---------------------------------------------|------------------------------------------|
|  **Model Akurat & Stabil**  | ✅ SVR (Tuning) atau Linear Regression |
|  **Cepat & Sederhana untuk Implementasi**  | ✅ Linear Regression |
|  **Fleksibel untuk Data Lebih Kompleks**  | ✅ XGBoost (Tuning) |
|  **Tidak Disarankan (untuk dataset ini)**  | ❌ Random Forest (Default & Tuning) |
Linear Regression sangat dekat performanya, namun **SVR (Tuning)** unggul tipis dan mampu menangani noise/outlier lebih baik.  
Oleh karena itu, **SVR (Tuning)** dipilih sebagai solusi terbaik untuk prediksi performa siswa dalam proyek ini.

---
## 6. Evaluation
### **Metrik Evaluasi yang Digunakan:**
Model yang digunakan pada proyek ini adalah bertipe regresi. Evaluasi model yang digunakan pada model regresi adalah sebagai berikut.
- **R² Score (Koefisien Determinasi):** Mengukur seberapa besar variasi target dijelaskan oleh model, dengan nilai mendekati 1 menunjukkan performa terbaik.
- **Mean Squared Error (MSE):** Rata-rata kuadrat selisih antara nilai aktual dan prediksi.
- **Root Mean Squared Error (RMSE):** Akar dari MSE, memberikan error dalam satuan target.
- **Mean Absolute Error (MAE):** Rata-rata nilai mutlak selisih prediksi dengan nilai aktual.
- **Cross-validation R² (CV R² Mean dan CV R² Std):** Menunjukkan kestabilan model pada beberapa fold data.

### **Hasil Evaluasi:**
Tabel Ringkasan Evaluasi Model (berisi model-model default serta model hasil tuning) diurutkan berdasarkan Test R², misalnya:

| Model | Test MSE | Test RMSE | Test MAE | Test R² | CV R² Mean | CV R² Std | Best Params |
|------------------------------------|----------|-----------|----------|----------|------------|-----------|------------------------------------------------|
| **SVR (Tuning)** | 0.4576 | 0.6765 | 0.5412 | 0.9544 | 0.9563 | 0.0025 | {'model__kernel': 'linear', 'model__epsilon': ...} |
| **Linear Regression** | 0.4590 | 0.6775 | 0.5422 | 0.9542 | 0.9564 | 0.0024 | NaN |
| **XGBoost Regressor (Tuning)** | 0.5663 | 0.7525 | 0.6004 | 0.9435 | 0.9478 | 0.0038 | {'model__subsample': 0.6, 'model__n_estimators': ...} |
| **SVR (Default)** | 0.6140 | 0.7836 | 0.6252 | 0.9388 | 0.9381 | 0.0044 | NaN |
| **XGBoost Regressor (Default)** | 0.8443 | 0.9189 | 0.7312 | 0.9158 | 0.9205 | 0.0057 | NaN |
| **Random Forest Regressor (Tuning)** | 1.5021 | 1.2256 | 0.9661 | 0.8502 | 0.8674 | 0.0072 | {'model__n_estimators': 300, ...} |
| **Random Forest Regressor (Default)**| 1.5208 | 1.2332 | 0.9715 | 0.8484 | 0.8658 | 0.0075 | NaN |

**Analisis dan Insight:**

- **SVR (Tuning)** dan **Linear Regression** menunjukkan performa tertinggi (Test R² sekitar 0.954), dengan error terendah, serta cross-validation yang sangat konsisten.
- **XGBoost (Tuning)** memiliki performa yang cukup kuat (Test R² 0.9435) namun masih sedikit di bawah SVR dan LR.
- **Random Forest**, baik versi default maupun tuning, memiliki performa yang jauh lebih rendah, mengindikasikan bahwa algoritma ini kurang cocok untuk dataset ini.

### Perbandingan Hasil Evaluasi antar model

![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(14).png)

 📈 **1. R² Score Comparison (Akurasi pada data uji)**

- **SVR (Tuning)** dan **Linear Regression** memiliki nilai R² tertinggi (~0.954), menunjukkan kemampuan terbaik dalam menjelaskan variabilitas target.
- **XGBoost (Tuning)** dan **SVR (Default)** masih sangat baik (>0.93), tapi sedikit tertinggal.
- **Random Forest**, baik default maupun tuning, menunjukkan kinerja paling rendah (~0.85), mengindikasikan underperformance terhadap data uji.

✅ *Insight*: SVR (Tuning) dan Linear Regression paling akurat dan cocok untuk relasi yang cukup linear antar fitur.

---

📉 **2. Test MSE Comparison (Error kuadrat rata-rata)**
- **SVR (Tuning)** dan **Linear Regression** kembali unggul dengan MSE terkecil (~0.45), menunjukkan prediksi yang sangat dekat dengan nilai aktual.
- XGBoost (Tuning dan Default) menempati posisi tengah.
- **Random Forest**, baik tuning maupun default, memiliki error terbesar (>1.4), memperkuat bahwa model ini kurang cocok untuk dataset ini.
⚠️ *Insight*: MSE menunjukkan bahwa RF cenderung overfit atau tidak mampu menangkap pola dengan baik pada data ini.

  

---

  

📊 **3. Test MAE Comparison (Error absolut rata-rata)**
- **SVR (Tuning)** dan **Linear Regression** mencetak MAE terkecil (~0.54), artinya secara rata-rata kesalahan prediksi hanya sekitar 0.54 satuan.
- **XGBoost** menunjukkan performa menengah (~0.6–0.73).
- **Random Forest** memiliki MAE mendekati 1, menandakan deviasi prediksi yang cukup besar dari nilai sebenarnya.

📌 *Insight*: Konsistensi rendahnya MAE pada SVR dan Linear Regression mendukung keandalan mereka secara praktis dalam penggunaan nyata.

---

  

 🧪 **4. CV R² Mean Comparison (Akurasi rata-rata dari cross-validation)**

- **SVR (Tuning)** dan **Linear Regression** kembali menjadi yang terbaik (CV R² ~0.956), dengan stabilitas sangat tinggi (standar deviasi kecil).
- XGBoost menyusul di angka ~0.94.
- **Random Forest** menunjukkan hasil CV R² terendah (~0.86), artinya performa kurang stabil antar fold.
📊 *Insight*: Model terbaik bukan hanya akurat di data uji, tapi juga konsisten antar subset data (fold) dalam cross-validation.

---

###  🧠 **Kesimpulan**

| Aspek Utama | Model Terbaik | Model Terburuk | Catatan Penting |
|---------------------------|--------------------|-----------------------|----------------------------------------------------------------------------------|
|  **Akurasi (R²)**  | SVR (Tuning), LR | RF (Default & Tuned) | SVR (Tuning) sedikit unggul dari Linear Regression. |
|  **Kesalahan (MSE, MAE)**  | SVR (Tuning), LR | RF (Default & Tuned) | Error sangat kecil pada SVR dan Linear Regression. |
|  **Konsistensi (CV R²)**  | SVR (Tuning), LR | RF (Default & Tuned) | Linear Regression dan SVR menunjukkan generalisasi terbaik. |
---

### 🔝 **Top 10 Fitur Paling Berpengaruh (Positif)**
![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(16).png)
 

Artinya: jika nilai fitur meningkat (atau bernilai 1 untuk fitur biner), maka prediksi performa akademik akan **naik**.


| Fitur | Koefisien | Interpretasi |
|-------|-----------|--------------|
|  **Peer_Influence_Positive**  | +0.997 | Dukungan dari teman yang positif sangat kuat kaitannya dengan performa akademik tinggi.
|  **Internet_Access_Yes**  | +0.983 | Akses internet sangat menunjang pembelajaran modern, baik untuk eksplorasi maupun akses sumber belajar.
|  **Extracurricular_Activities_Yes**  | +0.529 | Kegiatan ekstrakurikuler memberikan dampak positif – mungkin karena menumbuhkan disiplin dan soft skills.
|  **Peer_Influence_Neutral**  | +0.506 | Bahkan pengaruh teman yang netral tetap lebih baik daripada negatif.
|  **Tutoring_Sessions**  | +0.505 | Bimbingan belajar efektif meningkatkan kemampuan siswa.
|  **Hours_Studied**  | +0.296 | Semakin banyak waktu belajar, semakin baik hasilnya – meskipun tidak sebesar pengaruh sosial.
|  **Physical_Activity**  | +0.223 | Aktivitas fisik tampaknya berkontribusi pada keseimbangan mental dan kebugaran siswa.
|  **Attendance**  | +0.201 | Kehadiran tinggi berkorelasi positif dengan kinerja belajar.
|  **Previous_Scores**  | +0.049 | Nilai sebelumnya tetap relevan, meskipun efeknya lebih kecil dibanding faktor lain.
|  **Sleep_Hours**  | +0.015 | Tidur punya dampak kecil, bisa jadi karena variasi kebutuhan tidur antar individu.

  

🎯 *Insight utama*:

Faktor **lingkungan sosial** (teman & akses internet) justru **lebih berdampak besar** dibanding waktu belajar atau prestasi sebelumnya. Ini menarik karena menegaskan pentingnya ekosistem positif.

  

---

  

### 🔻 **Top 10 Fitur Paling Berpengaruh (Negatif)**

![image](https://raw.githubusercontent.com/zulfikarsp27/cobarepo/refs/heads/main/download%20(15).png)

Artinya: jika nilai fitur meningkat (atau bernilai 1 untuk fitur biner), maka prediksi performa akademik akan **turun**.

  

| Fitur | Koefisien | Interpretasi |
|-------|-----------|--------------|
|  **Access_to_Resources_Low**  | -1.979 | Ketidaktersediaan sumber belajar sangat berdampak buruk pada performa.
|  **Parental_Involvement_Low**  | -1.970 | Minimnya keterlibatan orang tua sangat memengaruhi hasil belajar secara negatif.
|  **Parental_Involvement_Medium**  | -0.994 | Bahkan keterlibatan sedang dari orang tua tetap berdampak kurang baik dibanding tinggi.
|  **Motivation_Level_Low**  | -0.982 | Kurangnya motivasi sangat menurunkan performa.
|  **Learning_Disabilities_Yes**  | -0.972 | Gangguan belajar harus diperhatikan khusus agar tidak membuat siswa tertinggal.
|  **Access_to_Resources_Medium**  | -0.959 | Akses parsial terhadap sumber belajar masih tidak cukup.
|  **Family_Income_Low**  | -0.940 | Ekonomi keluarga memengaruhi akses, ketenangan belajar, dll.
|  **Motivation_Level_Medium**  | -0.493 | Motivasi sedang masih kurang bila dibandingkan motivasi tinggi.
|  **Family_Income_Medium**  | -0.442 | Sama seperti akses, pengaruh ekonomi keluarga terasa di berbagai aspek.
|  **School_Type_Public**  | -0.021 | Sekolah negeri sedikit lebih rendah dari swasta pada dataset ini, tapi pengaruhnya kecil.

  

🔍 *Insight utama*:

Faktor **akses, ekonomi, dan dukungan keluarga** menjadi **penghambat utama** performa akademik. Ini penting untuk intervensi kebijakan atau dukungan tambahan.

  

---

  

## 🧠 **Kesimpulan Proyek**

| Aspek Penting | Insight |
|---------------|---------|
| 🔧 **Faktor internal**  | Motivasi dan kehadiran penting, tapi tidak dominan jika lingkungan sosial atau dukungan rendah. |
| 🌐 **Faktor eksternal**  | Dukungan teman, akses internet, dan keterlibatan orang tua menjadi pengungkit performa utama. |
| ⚠️ **Faktor risiko**  | Akses rendah terhadap sumber daya dan keterlibatan rendah dari orang tua adalah indikator risiko performa rendah. |
| 📊 **Model Linear Regression**  | Sederhana namun mampu memberi insight kuat dan bisa dijadikan dasar rekomendasi kebijakan atau intervensi pendidikan. |
---

**Penjelasan Formula Metrik dan Cara Kerjanya**

1.  **Mean Squared Error (MSE)**
    
       $$
   MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat y_i)^2
   $$
    
    -   **Penjelasan:** Menghitung rata‑rata kuadrat selisih antara nilai aktual yiy_i dan prediksi y^i\hat y_i.
        
    -   **Karakteristik:**
        
        -   Lebih **sensitif** terhadap outlier (karena kuadrat error).
            
        -   Unitnya kuadrat satuan target, sehingga besarannya bisa sulit diinterpretasi langsung.
            
2.  **Root Mean Squared Error (RMSE)**
    
      $$
   RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat y_i)^2}
   $$
    -   **Penjelasan:** Akar dari MSE, mengembalikan unit ke satuan target asli.
        
    -   **Karakteristik:**
        
        -   Lebih mudah diinterpretasi karena skala sama dengan variabel target.
            
        -   Masih sensitif pada outlier, mirip MSE.
            
3.  **Mean Absolute Error (MAE)**
    
       $$
   MAE = \frac{1}{n}\sum_{i=1}^{n}\lvert y_i - \hat y_i\rvert
   $$
    -   **Penjelasan:** Rata‑rata nilai absolut selisih antara prediksi dan aktual.
        
    -   **Karakteristik:**
        
        -   **Tidak** memperbesar efek outlier (tidak dikuadratkan).
            
        -   Memberi gambaran kesalahan rata‑rata dalam satuan target.
            
4.  **R² Score (Koefisien Determinasi)**
    
       $$
   R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat y_i)^2}{\sum_{i=1}^n (y_i - \bar y)^2}
   $$

    -   **Penjelasan:** Mengukur **proporsi** variansi target yy yang dapat dijelaskan oleh model.
        
        -   Pembilang  $$ (∑(yi−y^i)2\sum (y_i - \hat y_i)^2)  $$ adalah **Residual Sum of Squares (RSS)**.
            
        -   Penyebut  $$ (∑(yi−yˉ)2\sum (y_i - \bar y)^2)  $$ adalah **Total Sum of Squares (TSS)**.
            
    -   **Karakteristik:**
        
        -   Nilai antara −∞-\infty hingga 1.
            
        -   Semakin mendekati 1, semakin baik model menjelaskan variasi data.
            
5.  **Cross‑Validation R² (CV R² Mean & Std)**
    
    -   **CV R² Mean:** Rata‑rata skor R2R^2 dari beberapa lipatan (fold) validasi silang.
        
    -   **CV R² Std:** Standar deviasi dari skor‑skor tersebut—mengukur **kestabilan** model di berbagai subset data.
        
    -   **Penjelasan:**
        
        -   Memastikan bahwa performa model tidak hanya baik pada satu pembagian data, tetapi konsisten di beberapa skenario.
            

----------
