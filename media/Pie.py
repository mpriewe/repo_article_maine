#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/mpriewe/repo_article_maine/main/script/Figure%202.csv")

fig = px.pie(df, names = "Country",
             values ="No. of newstories",
             title='Distribution of news reports on the Maine explosion by country',
             labels = {"names" :["Spain","USA","Germany","Mexico","Finland","UK","Netherlands"]})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

