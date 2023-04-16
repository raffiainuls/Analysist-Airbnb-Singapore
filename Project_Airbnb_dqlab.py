#!/usr/bin/env python
# coding: utf-8

# # Preparation Data

# In[72]:


from haversine import haversine, Unit
import matplotlib.pyplot as plt
import pandas as pd
import pandasql as ps
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from scipy.stats import gaussian_kde
from datetime import datetime
import math
import mysql.connector
from mysql.connector import Error
import pandas as pd
import streamlit as st


# In[3]:


data_listings = pd.read_csv("DQLab_listings(22Sep2022) (1).csv")
data_reviews = pd.read_csv("DQLab_reviews(22Sep2022).csv")
data_neighbourhood= pd.read_csv("DQLab_nieghbourhood(22Sep2022).csv")



# In[4]:


data_listings


# In[9]:


data_neighbourhood


# In[10]:


data_reviews


# # Exploratory  Data

# Join Data Menggunakan SQL

# Membuat Dabase 

# In[9]:


import sqlite3 
#membuat koneksi ke database 
conn = sqlite3.connect('database_airbnb')

#connect dataframe ke dalam tabel database
data_listings.to_sql('data_listings', conn, if_exists='replace', index = False)
data_reviews.to_sql('data_reviews', conn, if_exists='replace', index = False)
data_neighbourhood.to_sql('data_neighbourhood', conn , if_exists='replace', index = False)


# In[10]:


query = ''' 
        select dl.id, dl.name, dl.host_id, dl.host_name, dl.neighbourhood, dl.latitude, dl.longitude, 
        dl.room_type, dl.price, dl.minimum_nights, dl.availability_365, dn.neighbourhood_group,  
        dr.date as review_date
        from data_listings as dl
        left join data_neighbourhood as dn on dl.neighbourhood= dn.neighbourhood
        left join data_reviews as dr on dl.id = dr.listing_id 
        order by dl.host_id
'''
dataset = pd.read_sql_query(query,conn)
dataset  = dataset.dropna()
dataset.to_sql('dataset', conn , if_exists='replace', index = False)
dataset


# Menambahkan Column last_review dan total review

# In[11]:


data= """ select dl.id, dl.name, dl.host_id, dl.host_name, dl.neighbourhood, dl.latitude, dl.longitude,dl.room_type, dl.price, dl.minimum_nights, dl.availability_365, dn.neighbourhood_group,  MAX(dr.date) as last_review, count(dr.listing_id) as total_review
                        from data_listings as dl
                        left join data_neighbourhood as dn on dl.neighbourhood = dn.neighbourhood
                        left join data_reviews as dr on dl.id = dr.listing_id 
                        group by dl.id
                        order by dl.price desc
                        
                        """

data = pd.read_sql_query(data, conn)
data = data.dropna()
data.to_sql('data', conn , if_exists='replace', index = False)
data


# ## Statistik Deskriptif
# 

# In[12]:


data.info()


# In[13]:


data.describe()


# In[14]:


data.hist(bins=50, figsize=(20,15))
#plt.show()


# In[15]:


''''plt.figure(figsize=(12, 6))
sns.kdeplot(data.price, shade=True)
sns.rugplot(data.price, color='r')
plt.title('Distribusi Harga Listing Airbnb di Singapura', fontsize=16)
plt.xlabel('Harga per malam (SGD)', fontsize=14)
plt.ylabel('Kepadatan', fontsize=14)
plt.xlim(0, 800)
plt.show()
'''


# Outlier pada data

# In[16]:

'''
sns.set(style ="whitegrid")
plt.figure(figsize = (10,6))
sns.boxplot(x=data['price'])
plt.title("Boxplot of Airbnb Listing Prices in Singapore")
plt.xlabel("Price")
plt.show() '''


# Menghapus Outlier pada data

# In[17]:


Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (0.4 * IQR)

df = data[(data['price'] > lower_bound) & (data['price'] < upper_bound)]
df


# In[26]:


df.sort_values(by= "price")
df.to_sql('df', conn , if_exists='replace', index = False)


# In[19]:

'''
sns.set(style ="whitegrid")
plt.figure(figsize = (10,6))
sns.boxplot(x=df['price'])
plt.title("Boxplot of Airbnb Listing Prices in Singapore")
plt.xlabel("Price")
plt.show() '''


# ## Top Host Name

# In[27]:


data_top_host_name_10 = """ select host_id, host_name, count(id) as total_listing, sum(total_review) as total_review
                                  from df
                                  group by host_id
                                  order by total_review desc
                                  limit 10
                            """

data_top_host_name = """ select host_id, host_name, count(id) as total_listing, sum(total_review) as total_review
                                  from df
                                  group by host_id
                                  order by total_review desc
                                  
                            """

data_top_host_name = pd.read_sql_query(data_top_host_name, conn)
data_top_host_name_10 = pd.read_sql_query(data_top_host_name_10, conn)
data_top_host_name_10.to_sql('data_top_host_name_10', conn , if_exists='replace', index = False)


# Visualisasi Top Host Name

# In[28]:



colors = ["#FFACAC","#FFBFA9","#FFBFA9","#FFBFA9","#FFBFA9","#FFBFA9","#FFBFA9","#FFBFA9","#FFBFA9","#FFBFA9"]


plot_top_10_review = px.bar(data_top_host_name_10, x="host_name", y="total_review", color="host_name", color_discrete_sequence=colors, template="ggplot2")



# modify Title
#plot_top_10_review.update_layout(title = "<b>Top 10 Host Name According Total Review<b>", 
#                                 title_font= dict(size = 18, color= "black", family = "arial"),title_x=0.3,
#                                 showlegend=False)
plot_top_10_review.update_layout(showlegend=False)

#update label x dan y
plot_top_10_review.update_xaxes(title= "<b> Host name <b>", title_font= dict(size = 12, color="black", family = "arial"))
plot_top_10_review.update_yaxes(title = "<b> Total Reviews", title_font= dict(size = 12, color = "black", family = "arial"))

# update xtick dan ytick
plot_top_10_review.update_xaxes(tickfont=dict(size=12, family="arial", color = "black"),tickangle=10)






# In[24]:


m, c = np.polyfit(data_top_host_name['total_listing'], data_top_host_name['total_review'], 1)
print(m, c)
print(data_top_host_name['total_review'].corr(data_top_host_name['total_listing']))

X1 = 0
X2 = 217
y1 = m * X1 + c
y2 = m * X2 + c
'''
# Melihat scatter plot
plt.scatter(data_top_host_name['total_listing'], data_top_host_name['total_review'])

## PENAMBAHAN GARIS REGRESI ##
plt.plot([X1, X2], [y1, y2], 'k--')

plt.show()
'''
# ## Mencari Top Minimum Profit

# In[30]:


data_profit_minimum_top_host_name = """ select id, name, host_id, host_name, count(id) as Total_Listing, price, minimum_nights, sum(total_review) total_reviews, (price * minimum_nights * total_review) as minimum_profit
                                                 from data
                                                 WHERE host_name IN ('Bryce [RentRadise]', 'Havona', 'UHA Management', 'Heritage', 'Robin & Louise', 'Advante Homes', 'Keith Kok', 'Welcome Home Decor & Management', 'Eddie', 'Kym')
                                                 group by id
                                                 order by minimum_profit desc                                           
                                            
                                            """


data_profit_minimum_top_host_name = pd.read_sql_query(data_profit_minimum_top_host_name, conn)
data_profit_minimum_top_host_name.to_sql('data_profit_minimum_top_host_name', conn , if_exists='replace', index = False)
data_profit_minimum_top_host_name


# In[31]:


data_profit_minimum_top_host_name_fix= """ select host_name, sum(Total_Listing) as total_listing, avg(price), avg(minimum_nights), sum(total_reviews) as total_reviews, sum(minimum_profit) as total_profit
                                                from data_profit_minimum_top_host_name
                                                group by host_name
                                                order by total_profit desc
                                                limit 3


                                          """
data_profit_minimum_top_host_name_fix = pd.read_sql_query(data_profit_minimum_top_host_name_fix, conn)
data_profit_minimum_top_host_name_fix.to_sql('data_profit_minimum_top_host_name_fix', conn, if_exists='replace', index = False)
data_profit_minimum_top_host_name_fix



# Visualisasi Top 3 Minimum

# In[32]:


top_minimum_profit = px.bar(data_profit_minimum_top_host_name_fix,x = "host_name", y="total_profit",template= "ggplot2")

# modify title
#top_minimum_profit.update_layout(title ="<b> Top 3 Minimum Profit", title_font = dict(size = 20, color = "black", family = "arial"), title_x = 0.35,
#                                 legend = dict(font = dict(size = 10)))

# Update label x dan y

top_minimum_profit.update_xaxes(title = "Host Name", title_font = dict(size = 12, color = "black", family = "arial"))
top_minimum_profit.update_yaxes(title = "Minimum Profit (USD)", title_font= dict(size= 12, color = "black", family = "arial"))
#top_minimum_profit.show()


# ## Distribusi Harga Airbnb Singapore

# Distribusi Keseluruhan
# 

# In[53]:


# calculate kernel density estimation 
kde = gaussian_kde(df["price"])
x = np.linspace(df['price'].min(), df['price'].max())
y = kde(x)

# create histogram plot
plot_dis_price = px.histogram(x=df['price'], nbins = 50, template = "ggplot2", opacity = 0.5)

# add kde plot
plot_dis_price.add_trace(go.Scatter(x=x,
                                    y=y,
                                    name="Density",
                                    yaxis= "y2",
                                    line=dict(color= "red", width= 3)
                                    ))

# set title, axis labels and layout 
plot_dis_price.update_layout(#title= "<b>Distribusi Harga Airbnb Singapore<b>", 
                             #title_font = dict(size = 20, color = "black", family = "arial"), title_x = 0.3,
                             bargap = 0.05, 
                             bargroupgap = 0.2, 
                             legend = dict(x=1.05, y= 1), width = 1000)

# update xaxes 
plot_dis_price.update_xaxes(title = "Price", title_font = dict(size = 12, color = "black", family= "arial"))

# update yaxes
plot_dis_price.update_yaxes(title = "Count", title_font = dict(size = 12, color = "black", family = "arial"))

# set second yaxis scale for the kde plot
plot_dis_price.update_layout(yaxis2 = dict(title = "Density", 
                                           title_font = dict(size = 12,family = "arial"), 
                                           overlaying ='y', 
                                           side = 'right'))



# Distribusi Pada Neighbourhood Group

# In[34]:


plot_dis_price_ng = px.box(df, x= "neighbourhood_group", y ="price", points = "all", color = "neighbourhood_group", 
                           color_discrete_sequence=["#5D3891","#655DBB","#3E54AC","#146C94","#19A7CE"], 
                           template = "ggplot2")

#update layout 
#plot_dis_price_ng.update_layout(title = "<b>Distribusi Harga Setiap Neighbourhood Group<b>", title_font = dict(size = 20, color = "black", family = "arial"),
#                                legend = dict(font= dict(size = 10)), title_x = 0.2, width = 800)

plot_dis_price_ng.update_layout(showlegend = False)

#update xaxes dan yaxes
plot_dis_price_ng.update_xaxes(title = "Neighbourhood Group", title_font= dict(size = 12, color = "black", family = "arial"))
plot_dis_price_ng.update_yaxes(title = "Price", title_font = dict(size =12, color = "black",family = "arial"))

#plot_dis_price_ng.show()


# Distribusi Harga Pada Setiap Neighbourhood Group 

# In[35]:


# selection data with any neighbourhood_group and asign to new variabel
data_central = df[df['neighbourhood_group']== 'Central Region'].sort_values('price',ascending= False)
data_west = df[df['neighbourhood_group'] == 'West Region'].sort_values('price', ascending = False)
data_north = df[df['neighbourhood_group'] == 'North Region'].sort_values('price', ascending = False)
data_east = df[df['neighbourhood_group']== 'East Region'].sort_values('price', ascending = False)
data_north_east = df[df['neighbourhood_group'] == 'North-East Region'].sort_values('price', ascending = False)


# In[36]:



# In[37]:


# function for plot correlation distribution price neighbourhood in any neighbourhood_group
def plot_corr_price_neighbourhood(data):
  title = data.reset_index().at[0,'neighbourhood_group']
  corr = data[['neighbourhood', 'price']].groupby(['neighbourhood']).mean().sort_values('price')
  plt.figure(figsize = (15,15))
  ax = sns.heatmap(corr, annot = True, fmt = '.0f')
  font = dict(family = 'arial', size = 15)
  ax.set_xticks([])
  ax.tick_params(axis = 'y', labelsize = 15)
  ax.tick_params(axis = 'x', labelsize = 15)
  plt.title(f'Harga  Neighbourhood {title}', size = 20, pad= 30)
  plt.xlabel('Price', size = 18, labelpad = 20)
  plt.ylabel(' ')
  
  plt.show()


# In[38]:


#showing plot
plot_dis_region_central = plot_corr_price_neighbourhood(data_central)
plot_dis_region_east = plot_corr_price_neighbourhood(data_east)
plot_dis_region_west = plot_corr_price_neighbourhood(data_west)
plot_dis_region_north =plot_corr_price_neighbourhood(data_north)
plot_dis_region_north_east =plot_corr_price_neighbourhood(data_north_east)


# In[39]:


# function mapbox distribution price


def plot_mapbox_price_neigbourhood(data):
  title = data.reset_index().at[0,'neighbourhood_group']
  fig = px.scatter_mapbox(data,lat = 'latitude', lon = 'longitude', hover_name= 'name',
                          hover_data= ['neighbourhood'], color = 'price',color_continuous_scale='Viridis_r', zoom = 12,
                          mapbox_style='carto-positron', template= 'ggplot2')
  #fig.update_layout(title = f"<b>Distribution Price {title}<b>", title_font =dict( size = 20, color = 'black', family = 'arial'), title_x = 0.25)
  return fig

# In[40]:


# showing plot
plot_map_dis_central =plot_mapbox_price_neigbourhood(data_central)
plot_map_dis_east =plot_mapbox_price_neigbourhood(data_east)
plot_map_dis_west =plot_mapbox_price_neigbourhood(data_west)
plot_map_dis_north =plot_mapbox_price_neigbourhood(data_north)
plot_map_dis_north_east =plot_mapbox_price_neigbourhood(data_north_east)


# ## Corelation Price and Room Type

# In[41]:


corr = df[['room_type', 'price']].groupby(['room_type']).mean().sort_values('price', ascending = False)

# membuat heatmap

corelation_room_price = plt.figure(figsize = (12,10))

ax =sns.heatmap(corr,annot=True)

font = {'family': 'Arial', 'size': 15}

ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='x', labelsize=15)
corelation_room_price = plt.show()


# In[42]:


harga_room_ng = df.groupby(['neighbourhood_group', 'room_type'])['price'].mean().reset_index()
harga_room_ng


# In[43]:


# Membuat contoh data frame
# Create the bar chart
harga_room_ng = harga_room_ng.sort_values('price')
plot_price_room_type_ng = px.bar(harga_room_ng, x="neighbourhood_group", y="price", barmode = 'group',color="room_type", template = 'ggplot2')

plot_price_room_type_ng.update_layout(#title = '<b>Harga Room Type Pada Neigbourhood Group<b>', title_font = dict(size = 20, family = 'arial', color = 'black'), 
                                      showlegend = False)

plot_price_room_type_ng.update_xaxes(title = "Room Type", title_font = dict(size = 12, color = "black", family = 'arial'))
plot_price_room_type_ng.update_yaxes(title = 'Price', title_font = dict(size = 12, color = 'black', family = 'arial'))

# Show the chart
#plot_price_room_type_ng.show()


# ## Distribusi Pengunjung

# 

# In[44]:


top_review_listing_room_ng = df.groupby(['neighbourhood_group', 'room_type'])['total_review'].sum().reset_index()
top_review_listing_room_ng.sort_values('total_review')

plot_top_review_room_ng = px.bar(top_review_listing_room_ng, x = 'neighbourhood_group', y = 'total_review', color = 'room_type', barmode = 'group', orientation = 'v', opacity = 1, template = 'ggplot2')

#plot_top_review_room_ng.update_layout(title = '<b> Distribusi Review Berdasarkan Room Type Pada setiap Neighbourhood Group<b>', title_font = dict(size = 20, color = 'black', family = 'arial'))
plot_top_review_room_ng.update_layout(showlegend = False)
plot_top_review_room_ng.update_xaxes(title = 'Neighbourhood Group', title_font = dict(size = 12, color = 'black', family = 'arial'))
plot_top_review_room_ng.update_yaxes(title = 'Jumlah Review', title_font = dict(size = 12, color = 'black', family = 'arial'))

#plot_top_review_room_ng.show()




# In[46]:


def plot_pie_review_per_neighbourhood(data):
  title = data.reset_index().at[0,'neighbourhood_group']
  if data['neighbourhood'].nunique() > 3:
     # group data into neighbourhood and select 4 highhest total_reviews
     sum_review_neighbourhood = data.groupby('neighbourhood')['total_review'].sum().nlargest()
     # sum of top 4 total review
     top_review = sum_review_neighbourhood.sum()
     # find sum review for other top review
     other_sum_neighbourhood = data['total_review'].sum() - top_review
     
     # find count of variabel other total review (count for data['neighbourhood'] - count for variabel top 4 sum_review_neighbourhood)
     count_other = data['neighbourhood'].nunique() - sum_review_neighbourhood.nunique()
     
     # make data for other_sum_neighbourhood
     other_sum_neighbourhood = (other_sum_neighbourhood / count_other).astype(int)
     
     #add other_sum_neighbourhood to data sum_review_neighbourhood 
     sum_review_neighbourhood['other'] = other_sum_neighbourhood
     sum_review_neighbourhood.sort_values(ascending = True)
     
     # make pie plot 
     fig = px.pie(sum_review_neighbourhood,
               values = sum_review_neighbourhood,
               names = sum_review_neighbourhood.index,
               color = sum_review_neighbourhood.index, template='streamlit',
               hole = 0.5)
     
     fig.update_traces( textfont = dict(size = 15, color = 'black', family = 'arial'), textinfo = 'percent')
     fig.add_annotation(text = f"<b> {title} <b>", showarrow = False, font = dict(size = 12, color = 'black', family = 'arial'))
     
  
  else: 
    sum_review_neighbourhood = data.groupby('neighbourhood')['total_review'].sum().sort_values()

    fig = px.pie(sum_review_neighbourhood,
               values = sum_review_neighbourhood,
               names = sum_review_neighbourhood.index,
               color = sum_review_neighbourhood.index, template='streamlit',
               hole = 0.5)
    #fig.update_layout(title = "<b> Distribution Pengunjung Listing <br> Per Neighbourhood </b>", title_font = dict(size = 20, color = 'black', family = 'arial'))
    fig.update_traces(textfont = dict(size = 15, color = 'black', family = 'arial'), textinfo = 'percent')
    fig.add_annotation(text = f"<b> {title} <b>", showarrow = False, font = dict(size = 12, color = 'black', family = 'arial'))
  
  return fig






# In[47]:


plot_pie_review_ng_central =plot_pie_review_per_neighbourhood(data_central)
plot_pie_review_ng_east =plot_pie_review_per_neighbourhood(data_east)
plot_pie_review_ng_west =plot_pie_review_per_neighbourhood(data_west)
plot_pie_review_ng_north =plot_pie_review_per_neighbourhood(data_north)
pplot_pie_review_ng_north_east =plot_pie_review_per_neighbourhood(data_north_east)


# ## Total Review Dibawah dan diatas Rata-rata

# In[48]:


mean_total_review_ng = df.dropna().groupby('neighbourhood_group')['total_review'].mean().reset_index()

df['type_total_review'] = df.apply(lambda row: 'Above Mean' if row['total_review']> mean_total_review_ng.loc[mean_total_review_ng['neighbourhood_group'] == row ['neighbourhood_group'], 'total_review'].iloc[0] else  'Below Mean', axis = 1)

plot_mean_total_review = px.scatter(df, x= 'neighbourhood_group', y = 'total_review', color = 'type_total_review')
plot_mean_total_review.add_hline(y = mean_total_review_ng['total_review'].mean(), line_dash = 'dash', line_color = 'black',  annotation_text = "Mean Total Review")
#plot_mean_total_review.show()


# In[49]:


grouped_type_total_review_ng = df.dropna().groupby(['neighbourhood_group', 'type_total_review']).size().reset_index(name ='counts')

plot_type_review = px.bar(grouped_type_total_review_ng, x = 'neighbourhood_group',
                          y = 'counts', color = 'type_total_review', 
                          barmode = 'group', 
                          labels = {'type_total_review' : 'Status Review', 'counts' : 'Jumlah'}, template = 'streamlit')
#plot_type_review.update_layout(title = '<b>Jumlah Listing Dengan Kunjungan Di Bawah Rata-rata dan Di Atas Rata-rata<b>', title_font = dict(size = 20, color= 'black', family = 'arial'))
plot_type_review.update_layout(showlegend = False)
plot_type_review.update_xaxes(title = 'Neighbourhood Group', title_font= dict(size = 12, color = 'black', family = 'arial'))
plot_type_review.update_yaxes(title = 'Jumlah', title_font = dict(size = 12, color = 'black', family = 'arial'))

#plot_type_review.show()


# ## Listing After Covid 19

# In[50]:


df = df.dropna()
# mengubah tipe data kolom 'last_review' menjadi datetime
df['last_review'] = pd.to_datetime(df['last_review'])

# membuat kolom baru dengan kondisi yang diinginkan
df['status_after_covid'] = df['last_review'].apply(lambda x: 'active' if x > pd.Timestamp(2019,1,23) else 'not active')


data_before_after = df.groupby('status_after_covid')['status_after_covid'].count()
data_before_after
pie_before_after_covid = px.pie(data_before_after, values = data_before_after, names = ['Active', 'Not Active'], template = 'ggplot2', color_discrete_sequence= ['#19A7CE', '#146C94'])

#pie_before_after_covid.update_layout(title = '<b>Perbandingan Listing Yang Aktif Sesudah dan Sebelum Covid 19<b>', title_font = dict(size = 20, color = 'black', family = 'arial'))
#pie_before_after_covid.show()


# In[51]:


data_line = dataset.dropna().sort_values('review_date')
data_line


# ## Kunjungan dari tahun ke tahun

# In[54]:


date_agg_data = ''' select  review_date, count(review_date) as total_review
                             from dataset
                             group by review_date
                             order by review_date
                          '''
date_agg_data = pd.read_sql_query(date_agg_data, conn)

date_agg_data['review_date'] = pd.to_datetime(date_agg_data['review_date'])
date_agg_data['date_month'] = date_agg_data['review_date'].apply(lambda x: datetime.strftime(x, '%Y-%m'))

date_agg_data.to_sql('date_agg_data', conn, if_exists= 'replace', index = False)

monthly_agg_data = date_agg_data.groupby('date_month')['total_review'].sum().reset_index()
monthly_agg_data


# In[55]:


plot_date_review = px.line(monthly_agg_data,x = 'date_month', y = 'total_review',template = 'streamlit', markers = True)

# plot_date_review.update_layout(title = '<b>Penyewaan Listing di Airbnb Singapore dari tahun 2018 - 2022<b>', title_font = dict(size = 20, color = 'black', family = 'arial'), title_x = 0.3, template = 'streamlit')
plot_date_review.update_xaxes(title = 'Date', title_font = dict(size = 12, color = 'black', family = 'arial'))
plot_date_review.update_yaxes(title = 'Jumlah', title_font = dict(size = 12, color = 'black', family = 'arial'))
plot_date_review.add_annotation(text = 'Terjadi Penurunan yang tajam dari Desember-April', x = '2020-03', y = '2000', showarrow = False, font = dict(size = 14, color = 'black', family = 'arial'))
plot_date_review.add_annotation(text = 'Terjadi Lonjakan yang <br>cukup tajam', x = '2022-05', y = '550', showarrow = False, font = dict(size = 14, color = ' black', family = 'arial'))
#plot_date_review.show()


# ## Jarak Listing Teraktif Ke Pesisir

# In[56]:


data_top_listing_10 = """ 
                                select id, name, host_name, sum(total_review) as total_review, room_type, price, latitude, longitude, neighbourhood, neighbourhood_group
                                from data
                                group by id
                                order by total_review desc
                                limit 10 
                                """
data_top_listing_10 = pd.read_sql_query(data_top_listing_10, conn)


# In[58]:


# define the coordinates of the Singapore coast

singapore_cost = (1.3008,103.9122 )
data_top_listing_10 = data_top_listing_10.sort_values('latitude')

dist_to_cost = []

for i in range(len(data_top_listing_10)):
  listing_data = (data_top_listing_10.loc[i, 'latitude'], data_top_listing_10.loc[i, 'longitude'])
  dist = haversine(singapore_cost, listing_data)
  dist_to_cost.append(dist)

data_top_listing_10['distance_to_coast'] = dist_to_cost
 

data_top_listing_10.to_sql('data_top_listing_10',conn, if_exists= 'replace', index = False)

data_top_listing_10


# In[68]:


plot_distance_cost = px.scatter(data_top_listing_10, x = 'name', y = 'total_review', size = 'distance_to_coast', color = 'distance_to_coast', size_max = 50, 
                                hover_data = ['price', 'room_type', 'neighbourhood', 'neighbourhood_group'], template = 'streamlit')

#plot_distance_cost.update_layout(title = '<b>Plot Grafik Informasi Jarak Ke Pesisir Listing Teraktif<b>', title_font = dict(size = 20, color = 'black', family = 'arial'), title_x =0.5)

plot_distance_cost.update_xaxes(showticklabels=False)
plot_distance_cost.update_yaxes(title = 'Jumlah Review', title_font = dict(size = 12, color = 'black', family = 'arial'))
#plot_distance_cost.show()

