#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-


# In[3]:


pip install plotly


# In[1]:


# Importing the modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


# Load a dataset as a pandas dataframe
df= pd.read_csv('Highest Holywood Grossing Movies.csv')
df


# In[3]:


#Data Validation#


# In[4]:


df.info()


# In[5]:


#Finding and removing duplicate rows


# In[29]:


df.duplicated(keep=False)


# In[30]:


df.drop_duplicates(inplace = True)


# In[8]:


#Load and View the dataset
data_=pd.read_csv('percentage.csv')
data_['Proportion of domestic sales(%)']=round((data_['Domestic Sales (in $)']/data_['World Sales (in $)'])*100,2).astype(int)
data_


# In[9]:


#Define#
a=0
b=0
c=0
d=0
proportion=data_['Proportion of domestic sales(%)']


# In[10]:


proportion


# In[11]:


proportion0=[]


# In[12]:


#Count the number of intervals for each percentage#

for i in range(0,len(proportion)):
        proportion0.append(int(proportion[i]))


# In[13]:


a,d,c,d=0,0,0,0


# In[14]:


for i in proportion0:
    if i>70:
        a=a+1
    elif i> 50:
        b=b+1
    elif i> 30:
        c=c+1
    else:
        d=d+1


# In[15]:


d


# In[16]:


proportion=[a,b,c,d] 


# In[17]:


#Drawing pie charts
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


sizes=[a,b,c,d]
labels=['>70%','70%-51%','31%-50%','≤30%']
colors = ['lightskyblue', 'lightgray', 'royalblue', 'green']
explode = (0.1, 0.1, 0.1, 0.1)
shadow=True
ax1 = plt.subplots()
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle = 90)
plt.title('Proportion distribution of domestic sales of Highest Holywood Grossing Movies')
plt.show()


# In[19]:


plt.show()


# In[20]:


#Drawing scatter plot
x=df['Release Date']
y=df['World Sales (in $)']


# In[26]:


plt.scatter(x, y, c=y, cmap='Spectral')
plt.colorbar()
plt.xticks(np.arange(1970,2022,3))
plt.rcParams.update({'figure.figsize':(10,4), 'figure.dpi':100})
plt.xlabel('Year of release')
plt.ylabel('Total sales(in $)')
plt.show()


# In[22]:


plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
sns.lmplot(x='Release Date'，y='World Sales (in $)', data=df)
plt.title("Scatter Plot with Linear fit");


# In[34]:


#List of all Genre
Genre= []
for i in df[df.shape[0]]:
    Genre.extend(df.loc[i,'Genre'])
Genre= pd.Series(Genre).unique()
Genre


# In[23]:


df['Genre_Action'] = ''
df['Genre_Adventure'] = ''
df['Genre_Sci-Fi'] = ''
df['Genre_Drama'] = ''
df['Genre_Fantasy'] = ''
df['Genre_Crime'] = ''
df['Genre_Comedy'] = ''
df['Genre_Romance'] = ''
df['Genre_Animation'] = ''
df['Genre_Thriller'] = ''
df['Genre_Musical'] = ''
df['Genre_Biography'] = ''
df['Genre_Horror'] = ''
df['Genre_Mystery'] = ''
df['Genre_Family'] = ''


# In[24]:


for i in range(len(df['Genre'])):
    if df['Genre'][i].__contains__("Action"):
        df['Genre_Action'][i]="Action"
        
    if df['Genre'][i].__contains__("Adventure"):
        df['Genre_Adventure'][i]="Adventure"
        
    if df['Genre'][i].__contains__("Sci-Fi"):
        df['Genre_Sci-Fi'][i]="Sci-Fi"
        
    if df['Genre'][i].__contains__("Drama"):
        df['Genre_Drama'][i]="Drama"
    
    if df['Genre'][i].__contains__("Fantasy"):
        df['Genre_Fantasy'][i]="Fantasy"
    
    if df['Genre'][i].__contains__("Crime"):
        df['Genre_Crime'][i]="Crime"
    
    if df['Genre'][i].__contains__("Comedy"):
        df['Genre_Comedy'][i]="Comedy"
    
    if df['Genre'][i].__contains__("Romance"):
        df['Genre_Romance'][i]="Romance"
    
    if df['Genre'][i].__contains__("Animation"):
        df['Genre_Animation'][i]="Animation"
    
    if df['Genre'][i].__contains__("Thriller"):
        df['Genre_Thriller'][i]="Thriller"
        
    if df['Genre'][i].__contains__("Musical"):
        df['Genre_Musical'][i]="Musical"
        
    if df['Genre'][i].__contains__("Biography"):
        df['Genre_Biography'][i]="Biography"
        
    if df['Genre'][i].__contains__("Horror"):
        df['Genre_Horror'][i]="Horror"
        
    if df['Genre'][i].__contains__("Mystery"):
        df['Genre_Mystery'][i]="Mystery"
        
    if df['Genre'][i].__contains__("Family"):
        df['Genre_Family'][i]="Family"
        


# In[25]:


df_1 = df.drop(columns = ['Genre'])


# In[35]:


df_sale = df.groupby(by = ["Genre"])['World Sales (in $)'].sum().reset_index()
df_count = df.groupby(by = ["Genre"])['World Sales (in $)'].count().reset_index()
df_ave = (df_sale["World Sales (in $)"] / df_count["World Sales (in $)"]).reset_index()
df_ave['Genre'] = df_count["Genre"]
px.bar(df_ave
      ,x ="Genre"
       , y = "World Sales (in $)"
       ,labels = {"World Sales (in $)":"Average Sale For Each Genre"}
      , title = "Average of sale for films which contain each genre")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




