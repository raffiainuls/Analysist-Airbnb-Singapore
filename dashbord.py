from Project_Airbnb_dqlab import plot_top_10_review, data_profit_minimum_top_host_name_fix, top_minimum_profit, plot_dis_price, plot_dis_price_ng, plot_map_dis_central, plot_map_dis_east, plot_map_dis_north, plot_map_dis_north_east, plot_map_dis_west, plot_price_room_type_ng,plot_top_review_room_ng, plot_pie_review_ng_central, plot_pie_review_ng_east, plot_pie_review_ng_north, plot_pie_review_ng_west,pplot_pie_review_ng_north_east, pie_before_after_covid,plot_date_review,plot_type_review,plot_distance_cost
import streamlit as st


st.markdown("<h1 style = 'text-align : center; color : black; font_size : 40 px; font-family : Arial'><b>Analisis Penyewaan Pada Airbnb Singapore<b></h1>", unsafe_allow_html= True)
st.markdown("------")
st.markdown("Created by [Raffi Ainul Afif](linkedin.com/in/raffi-ainul-afif-9811a411b/)")

paragraf1 = """<p style = 'font-size: 14px; font-family : Arial; '> Airbnb dalah sebuah platform online yang memungkinkan penggunanya untuk 
menyewa atau menyewakan akomodasi seperti rumah, apartemen, atau villa untuk jangka pendek Di singapura Airbnb telah menjadi salah satu 
pilihan utama bagi parawisatawan yang mencari tempat menginap yang nyaman,ekonomis, dan berlokasi strategis. Dilihat dari hal tersebut 
tentunya juga menguntungkan untuk orang yang ingin menyewakan tempat tinggalnya di Airbnb singapura karena kemungkinan besar akan mendapatkan 
keuntungan yang bagus. Sekarang mari kita lihat grafik peyewa yang memiliki review/ kunjungan paling banyak dari data Airbnb singapura 
tahun 2018 - 2022.</p>"""
st.markdown(paragraf1, unsafe_allow_html= True)
st.plotly_chart(plot_top_10_review )

paragraf2 = """ <p style = 'font-size: 14px; font_family : Arial; '> Dilihat dari grafik diatas, 10 penyewa dengan total kunjungan terbanyak,
memiliki jumlah kunjungan yang paling dikit 525 reviews yaitu penyewa dengna nama kym, sedangkan penyewa dengan total kunjungan paling banyak adalah
Bryce [RentRadise] yang total review atau kunjungannya sebesar 5073. Diantara ribuan penyewa yang menyewakan akomodasi di Airbnb Singapura 10 penyewa 
yang ada pada grafik dapat menempati urutan teratas dalam hal kunjungan. Tentu saja ada yang faktor yang membuat penyewa tersebut menperoleh posisi tersebut.
kita dapat menganalisa hal tersebut dari data yang ada.  </p>
"""
st.markdown(paragraf2, unsafe_allow_html= True)
kalimat1= ''' <p style = 'font-size: 14px; font-family: Arial;'> <strong>Namun sebelum kita analisa lebih lanjut, kita lihat terlebih dahulu kira-kira 
peyewa atau host name mana yang mendapatkan minimum profit?, apakah sama seperti penyewa dengan kunjungan terbanyak?<strong> </p>'''
st.markdown(kalimat1, unsafe_allow_html= True)
st.plotly_chart(top_minimum_profit)

paragraf3 = '''<p style = 'font-size : 14px; font-family: Arial;'> Jika kita liat pada grafik di atas, menarik sekali bukan, ternyata data host name
dengan review terbanyak berbeda dengan data total minimum profit, dimana justru host name Edie yang sebelumnya berada pada posisi 9 untuk data kunjungan 
terbanyak, ternyata merupakan host_name dengan minimum profit paling tinggi. Kira kira mengapa hal itu bisa terjadi ya?. Mari kita telusuri lebih lanjut 
dengan melihat data table yang lebih lengkap mengenai hal tersebut.</p>
'''
st.markdown(paragraf3, unsafe_allow_html= True)


st.table(data_profit_minimum_top_host_name_fix)

paragraf4= '''<p style = 'font-size: 14px; font-family: Arial;'> Nah jika kita lihat lagi di datanya ada beberapa faktor yang mempengaruhi minimum profit 
yang diperoloeh oleh penyewa yaitu jumlah akomodasi yang ditawarkan di Airbnb, harga dari akomodasi yang ditawarkan, minimal malam yang dapat dipesan, 
kemudian kunjungan dari masing-masing akomodasi. Jika dilihat lagi host name eddie justru tidak memiliki jumlah akomodasi yang ditawarkan sebanyak 
Bryce[RentRadise] dan Heritage, jumlah akomodasi yang ditawarkan Ediie justru kenderung kecil dan hal tersebut juga berpengaruh ke total review yang 
juga tidak sebesar penyewa top total review lainnya.</p>
'''
st.markdown(paragraf4,unsafe_allow_html= True)

paragraf5= '''<p style = 'font-size: 14px; font-family: Arial;'> Eddie bisa menempati posisi atas dari total minimum profit dikarenakan  avg minimum nights yang eddie 
pakai terhitung besar yaitu 92 dan dengan rata rata harga 65.000 membuatnya menjujuki posisi atas dalam hal minimum total profit meskipun 
hanya memiliki akomodasi dan total review tidak sebanyak pesaingnya.</p>
'''
st.markdown(paragraf5,unsafe_allow_html= True)

paragraf6= '''<p style = 'font-size: 14px; font-family: Arial;'> Menarik bukan dengna total listing yang tidak banyak dan total review 
yang tidak sebanyak pesaingnya justru Eddie menempati posisi atas, dan sekarang yang menjadi pertanyaan mengapa seseorang mau dan tertarik untuk menyewa
diakomodasi yang dimiliki Eddie secara jika dilihat minimum malam yang harus dipesan juga termasuk tinggi bukan. Tentu hal ini bisa jadi merupakan 
strategi dari eddie melihat pasar dan kebutuhan customer yang ingin menyewa di sekitar daerah akomodasinya, bisa jadi didaerah sekitar akomodasi
Eddie memang membutuhkan tempat akomodasi menginap dalam jangka waktu yang cukup lama. Dari sini bisa disimpulkan ada beberapa hal yang 
dapat menunjang suksesnya melakukan penyewaan di Airbnb Singapura dan <strong>mari kita analisis lebih lanjut supaya ketika kita ingin menyewakan 
akomodasi kita di Airbnb Singapura dapat berjalan dengan lancar.<strong></p>
'''
st.markdown(paragraf6,unsafe_allow_html= True)


kalimat2 = '''<p style = 'font-size: 14px; font-family: Arial;'> <strong> <i> Disclemer total minimum profit bukan merupakan pendapatan murni 
yang didapatkan oleh setiap host name, karena kita dari data yang ada kita tidak tahu dari setiap review berapa malam yang dipesan oleh pengunjung, mangkanya 
disebut minimum karena kita bisa lihat setidaknya 1 review atau kunjungan akan memesan minimum nights yang sudah ditentukan oleh setiap hostname. <strong> <i></p>
'''
st.write(kalimat2, unsafe_allow_html= True)
st.markdown("<h1 style = 'text-align : left; color : black; font-size : 20px; font-family : Arial'> <b>Distribusi Harga Airbnb Singapura<b></h1>", unsafe_allow_html= True)

paragraf7 = ''' <p style = 'font-size: 14; font-family: Arial;'> Tentunya harga menjadi salah satu faktor penting untuk menunjang supaya pengunjung teraktir menyewa 
akomodasi yang kita sewakan, maka dari itu menentukan harga yang pas untuk akomodasi kita sangat penting. kira kira ada dirange berpakah harga akomodasi di Airbnb Singapura?</p>
'''
st.markdown(paragraf7,unsafe_allow_html= True)

st.plotly_chart(plot_dis_price, use_container_width= True)

paragraf8 = '''<p style = 'font-size: 14px; color : black; font-family: Arial;'> Nah dilihat dari plot diatas dapat kita distribusi harga akomodasi yang ada di Airbnb Singapura. kita dapat
simpulkan bahwa ternyata banyak akomodasi yang range harganya berada pada range 45 - 59 USD, hal tersebut dapat menjadi patokan untuk kita dalam menetapkan harga jika kita ingin 
menyewakan akomodasi kita di Airbnb Singapura. Namun kita juga perlu tahu range harga untuk tiap Daerahnya bukan karna pasti untuk tiap darerah memiliki ciri khas harga yang 
berbeda-beda juga, oke sekarang coba kita lihat distribusi harga untuk tiap Neighbourhood Group.</p>
'''
st.markdown(paragraf8, unsafe_allow_html=True)
st.plotly_chart(plot_dis_price_ng, use_container_width = True)

paragraf_distribusi_price_ng = '''<p style = 'font-size : 14px; color : black; font-family: Arial;'> OKe, ternyata benar distribusi tiap wilayah berbeda-beda bisa dilihat pada box plot diatas,
bahwa wilayah Central region memiliki distribusi harga yang paling luas dan jika kita amati lebih detail Nort region merupakan wilayah yang distribusi harga minimumnya paling kecil dibandinkan
dengan daerah lainnya. Nah dari sini kita bisa tahu bahwa jika kita menyewakan akomodasi kita kita juga harus melihat dimana kita menyewakan akomodasi. Kita harus mengikuti trend harga dari daerah 
yang dari akomodasi yang ingin kita sewakan, karena kita juga harus tahu trend harga pasar di wilayah kita karna hal ini sangat berpengaruh terhadap ketertarikan pengunjung ke akomodasi kita. Jika 
kita sudah mengetahui distribusi harganya tentunya ini bisa jadi strategi kita untuk menarik pengunjung dengan memasang harga dibawah pasar mungkin. Nah sekarang kita udah mengatahui distribusi harga
tiap Neighbourhood Group atau tiap wilahyah ini, tetapi tentunya di dalam Neighbourhood group juga terdapat beberapa region kan. Supaya kita bisa tahu distribusi yang lebih rinci lagi mari kita lihat 
pada gambar dibawah ini </p> 
'''
st.markdown(paragraf_distribusi_price_ng, unsafe_allow_html= True)



options = ['Central Region', 'East Region', 'West Region', 'North Region', 'North-east Region']

neighbourdhood_group = st.radio("Wilayah mana yang ingin anda lihat?", options, key="neighbourhood_group")

if neighbourdhood_group == 'Central Region':
    st.plotly_chart(plot_map_dis_central)
elif neighbourdhood_group == 'West Region':
    st.plotly_chart(plot_map_dis_west)
elif neighbourdhood_group == 'East Region':
    st.plotly_chart(plot_map_dis_east)
elif neighbourdhood_group == 'North Region':
    st.plotly_chart(plot_map_dis_north)
elif neighbourdhood_group == 'North-east Region':
    st.plotly_chart(plot_map_dis_north_east)

paragraf_map_price ='''<p style = 'font-size : 14px; color : black; font-family: Arial;'> Dari Plot Map diatas kita dapat mengetahui secara pasti distribusi harga dari setiap wilayah dan bahkan dapat
dilihat pula harga dari setiap akomodasi yang tersedit. Nah dari map itu kita bisa menentukan harga yang pas untuk akomodasi yang ingin kita sewakan dengan melihat pesaing disekitar lokasi akomodasi kita.
Namun belum berakhir disitu saja dari tentunya harga dari suatu akomodasi juga berasal dari jenis akomodasi yang ditawarkan atau Room type yang disewakan oleh masing - masing host name,<strong> apakah benar harga akomodasi
dipengaruhi oleh Room typenya?, mari kita bahas <strong>.</p>
'''
st.markdown("<h1 style = 'text-align : left; color : black; font-size : 20px; font-family : Arial'> <b>Korelasi Antara Harga dengan Room Type<b></h1>", unsafe_allow_html= True)
paragraf_cor_price_room = ''' <p style = 'font-size : 14px; color : black; font-family: Arial;'> Jika dilihat dari jenis room type yang ada di Airbnb Singapura yaitu Shared Room, Private Room, Hotel Room, Entire Home/apt
dimana ternyata Shared room merupakan tipe room dengan rata-rata termurah di Airbnb Singapura kemudian posisi kedua ada Private room, selanjutnya Hotel room, dan yang memiliki rata rata termahal adalah Entire Home/apt. Entire Home/apt
merupakan Room type termahal tentunya tipe ini mempunyai fasilitas yang lebih baik dari tipe room type lainnya. Jadi kita harus menyesuai kan harga dengan jenis akomodasi yang kita akan sewakan ya. Untuk Plot room type dan harga dapat
dilihat pada plot dibawah ini.</p>
'''
st.markdown(paragraf_cor_price_room, unsafe_allow_html= True)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.plotly_chart(plot_price_room_type_ng, theme= 'streamlit' )

st.markdown("<h1 style = 'text-align : left; color: black; font-size: 20px; font-family : Arial'> <b>Analisa Penyewa akomodasi di Airbnb Singapura<b></h1>", unsafe_allow_html= True)
paragraf_total_reviews = ''' Sekarang waktunya kita menganalisa jumlah pengunjung atau penyewa di Airbnb Singapura. Tentunya hal ini sangat penting supaya kita dapat mengetahui sebenarnya daerah mana yang paling 
strategis atau paling sering didatangi oleh pengunjung, dan juga type room seperti apa yang biasanya disewa. nah untuk mengetahui lebih lanjut kita lihat dulu grafik di bawah ini yang merupakan distribusi jumlah pengunjung
tiap wilayah berdasarkan tipe room masing-masing.
'''
st.markdown(paragraf_total_reviews,unsafe_allow_html=True)
st.plotly_chart(plot_top_review_room_ng)

paragraf_total_reviews2 = '''<p style = 'font-size :14px; color : black; font-family : Arial;'>Setelah melihat dan mengamati grafik diatas, ternyata North region memiliki total kunjungan yang paling banyak, dan dari total kunjungan itu pengunjung lebih didominasi oleh kunjungan dengan akomodasi
tipe Entire Home/apt. Wah ternyata banyak pengunjung yang lebih senang untuk memesan tipe room Entire Home/apt ya, padahal tipe room ini adalah yang termahal dari yang lainnya. Kita bisa simpulkan bahwa sebenarnya harga pengunjung yang ingin 
menyewa akomodasi kita tidak melulu melihat tentang harga saja tetapi juga fasilitas yang diberikan, terbukti bahwa untuk wilayah Nort Region ini sangat banyak sekali pengunjung yang memesan untuk akomodasi tipe Entire Hotel/apt.</p>
'''
paragraf_total_review3 = '''<p style = 'font-size : 14px; color : black; font-family : Arial;' > Selain itu dari grafik diatas kita juga mendapatkan informasi bahwa sebenarnya tidak semua tipe kamar tersedia dibeberapa wilayah misal tipe hotel yang tidak ada di East region, West region, dan North-east region,
dan tipe Shared room yang hanya ada di wilayah Central Region. Kemudian dari grafik tersebut kita juga bisa tahu bahwa East region dan North east region merupakan wilayah yang paling sedikit dikunjungi. Sebagai tambahan supaya kita bisa lebih mengetahui lebih detail lagi tempat yang paling strategi dibawah ini tersedia
grafik presentasi pengunjung untuk tiap wilayah masing - masing. </p>
'''
st.markdown(paragraf_total_reviews2, unsafe_allow_html= True)
st.markdown(paragraf_total_review3, unsafe_allow_html=True)
options = ['Central Region', 'East Region', 'West Region', 'North Region', 'North-east Region']


neighbourdhood_group_pie = st.radio("Select a neighbourhood group", options, key="neighbourhood_group_pie")



if neighbourdhood_group_pie == 'Central Region':
    st.plotly_chart(plot_pie_review_ng_central)
elif neighbourdhood_group_pie == 'West Region':
    st.plotly_chart(plot_pie_review_ng_west)
elif neighbourdhood_group_pie == 'East Region':
    st.plotly_chart(plot_pie_review_ng_east)
elif neighbourdhood_group_pie == 'North Region':
    st.plotly_chart(plot_pie_review_ng_north)
elif neighbourdhood_group_pie == 'North-east Region':
    st.plotly_chart(pplot_pie_review_ng_north_east)

paragraf_simpulan = '''<p style = 'font-size : 14px; color : black; font-family: Arial;'> Dari Analisis - analisis diatas kita sebenarnya sudah dapat informasi banyak yang dapat membantu kita jika kita ingin menyewakan akomodasi kita di Airbnb Singapura, 
karena kita sudah mendapatkan informasi tentang tempat yang dapat dikatakan strategis dengan tipe room nya masing-masing dari banyaknya penyewa dan distribusi harga dari masing masing tempat tersebut. sebagai contoh kita dapat menyewakan akomodasi kita 
di daerah Woodlands yang termasuk wilayah North Region dan dengan tipe room Entire Hotel/apt. Pemilihan tersebut didasari dari wilayah paling stategis menurut data adalah North Region dengan tipe room Entire hotel/apt, dan untuk presentasi pengunjung paling banyak di
North Region ada di daerah Woodlands. Tetapi tentunya tidak semudah itu pastinya ada beberapa faktor lain yang menunjang penyewaan di Airbnb Singapura ini, maka dari itu mari kita coba analisis lebih dalam lagi. </p>
'''
st.markdown(paragraf_simpulan, unsafe_allow_html= True)


st.markdown("<h1 style = 'text-align : left; color : black; font-size : 20px; font-family : Arial'> <b>Presentasi Akomodasi Kamar yang masih aktif dan tidak aktif setelah Covid 19<b></h1>", unsafe_allow_html= True)

st.plotly_chart(pie_before_after_covid)
paragrafcovid = '''<p style = 'font-size : 14px; color : black; font-family: Arial;'> Pertama coba kita lihat presentase Akomodasi kamar yang masih aktif dan sudah tidak aktif lagi setelah pandemi Covid-19. Bisa dilihat
pada grafik pie chart diatas ternyata presentase akomodasi yang masih aktif setelah Pandemi Covid-19 masih sangat banyak, bahkan yang sudah tidak aktif lagi setelah covid hanya sekitar 5% saja. 
'''
st.markdown(paragrafcovid, unsafe_allow_html= True)
st.markdown("<h1 style = 'text-align : left; color : black; font-size : 20px; font-family: Arial;'> <b> Penyewaan dari tahun ke tahun<b></h1>", unsafe_allow_html= True)

st.plotly_chart(plot_date_review)

paragraf_kunjungan_per__tahun = '''<p style ='font-size : 14px; color : black; font-family: Arial;'> Dari grafik line chart diatas kita bisa lihat bahwa penurunan jumlah kunjungan yang cukup drastis pada Desember 2019 sampai april 2020. 
Tentunya terjadi karena adanya Covid-19, pandemi yang melanda dan membuat jumlah penyewaan pun ikut turun. Namun penlan - pelan jumlah penyewaan dikit demi dikit mulai naik kembali, hal itu selaras dengan penjelasan sebelumnya, masih banyak 
Akomodasi penyewaan di Airbnb Singapura yang masih aktif lagi setelah pandemi Covid-19. </p>
'''
paragraf_kunjungan_per__tahun2 = '''<p style = 'font-size :14px; color : black; font-family : Arial;'> Selain itu dari line chart diatas kita juga mendapat informasi setiap akhir tahun atau setiap bulan desember jumlah kunjungan akan meningkat. Kemudian Selain terjadinya
penurunan yang drastis akibar pandemi Covid-19, penyewaan di Airbnb juga mengalami kenaikan yang cukup tajam pada bulan Maret 2022 sampai dengan Mei 2022.
'''
st.markdown(paragraf_kunjungan_per__tahun, unsafe_allow_html= True)
st.markdown(paragraf_kunjungan_per__tahun2, unsafe_allow_html= True)

st.markdown("<h1 style = 'text-align : left; color : black; font-size : 20px; font-family : Arial'> <b>Akomodasi dengan total kunjungan diatas rata-rata<b></h1>", unsafe_allow_html= True)
st.plotly_chart(plot_type_review)
paragraf_mean_kunjungan = '''<p style = 'font-size : 14px; color : black; font-family : Arial;'> Jika kita perhatikan lagi dengan baik-baik pola grafik bar chart diatas hampir sama dengan grafik bar chart sebelum - sebelumnya
dimana yang menarik perhatian ada di wilayah Central region dan North Region. pada 2 wilayah ini memang paling banyak kunjungannya dan total kunjungan yang diatas rata-rata juga tidak terlalu sedikit meskipun jika dibandingkan dengan yang dibawah rata-rata juga masih sangat jauh. 
Tetapi dari sini kita bisa simpulkan wilayah Central dan North Region menjadi wilayah yang strategis untuk menyewakan akomodasi kita.</p>
'''
st.markdown(paragraf_mean_kunjungan, unsafe_allow_html= True)


st.markdown("<h1 style = 'text-align : left; color : black; font-size : 20px; font-family : Arial'> <b>Jarak Akomodasi teraktif ke pesisir<b></h1>", unsafe_allow_html= True)
st.plotly_chart(plot_distance_cost)
paragraf_dist_coast = ''' <p style  = 'font-size: 14px; color: black; font-family : Arial'> Dilihar dari plot diatas ternyata rata-rata jarak akomodasi teraktif dengan pesisir sekitar 20 km dan kita juga bisa lihat listing teraktif hampir semua berasal dari wilayah North Region,
yaitu  Woodlands dan semua akomodasi di Woodlands ini yang masuk jajaran akomodasi teraktif, tipe roomnya adalah Entire Home/apt. hal ini dapat menjadi pertimbangan lebih lanjut jika kita ingin menyewakan akomodasi di Airbnb Singapura. </p>
'''
st.markdown(paragraf_dist_coast, unsafe_allow_html= True)

paragraf_penutup = ''' <p style = 'font-size: 14px; color : black; font-family : Arial'> Akhirnya kita telah menganalisis data penyewaan akomodasi yan ada di Airbnb Singapura. dan dari hasil beberapa analisis, ada beberapa faktor yang mepengarui penyewaan di Airbnb Singapura ini
antara lain : harga, tipe room, dan tempat. Dari hasil analisis  harga bahwa harga berkaitan dengan tipe room, semakin baik tipenya menandakan fasilitas yang diberikan juga semakin bagus dan tentunya hal itu berpengaruh dengan harga dari akomodasi tersebut. Sebenarnya untuk harga 
sendiri di tiap daerah mempunyai trendnya sendiri-sendiri seperti contohnya pada  wilayah Central region dari analisis yang sudah dilakukan memiliki harga yang lebih mahal dibanding kan dengan wilayah-wilayah lainnya.</p>
'''
paragraf_penutup2= ''' <p style = 'font-size: 14px; color : black; font-family : Arial'>  Harga yang relatif rendah ada pada wilayah North Region dan East Region.
Untuk wilayah yang stategis atau wilayah yang paling banyak pengunjungnya sendiri berada di Central Region dan North Region. Jadi kita bisa simpulkan jika kita ingin memilih tempat kita bisa memilih Central region atau North region, jika kita memilih North Region akan membuat para calon pengunjung tertarik
karna harga di North region sendiri yang murah, tetapi kita juga bisa memilih Central Region jika kita ingin cepat mendapatkan pemasukan yang banyak karna harga di Central region relatif tinggi.</p>
'''
st.markdown(paragraf_penutup, unsafe_allow_html= True)
st.markdown(paragraf_penutup2, unsafe_allow_html= True)


