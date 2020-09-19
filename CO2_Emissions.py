import pandas as pd
import numpy as np

import json
from geojson import dump
import datetime

import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go

excel_file_path_plant1_weather = 'CO2_Emissions.csv'

data = pd.read_csv('CO2_Emissions.csv')
print(data)


sns.heatmap(data.corr(), annot = True, cmap = 'coolwarm', center = 0)
data.hist(figsize= (10, 3))


fig = px.scatter(data, x="Year", y="Entity", color="Year", size='Year', hover_data=['Annual CO₂ emissions (tonnes )', 'Code'], title = "CO2 Emissions")
#fig.show()
plotly.offline.plot(fig, filename='CO2 Emissions.html')


fig2 = go.Figure(data=go.Scatter(y = data['Entity'], mode='markers', marker=dict(size=16, color=data['Year'], #set color equal to a variable colorscale='Viridis', # one of plotly colorscales
        showscale=True)))
#fig2.show()
plotly.offline.plot(fig2, filename='CO2 Emissions.html')


data = data.rename(columns={'Entity':'Country', 'Annual CO₂ emissions (tonnes )':'value'})
data.head()
world_data = data.query("Country == 'World'")

fig3 = px.line(world_data,x='Year', y='value')
fig3.update_layout(title='<b>Evolution of CO2 emissions per year in the world</b>',xaxis_title='', yaxis_title='')
#fig3.show()
plotly.offline.plot(fig3, filename='CO2 Evolution of CO2 Emissions Per Year in the World.html')



europe_data = data.query("Country == ['France','United Kingdom','Spain','Italy','Germany', 'Russia']")

fig4 = px.line(europe_data,x='Year', y='value', color='Country')
fig4.update_layout(title='<b>Evolution of CO2 emissions per year in Europe</b>',xaxis_title='', yaxis_title='')
#fig4.show()
plotly.offline.plot(fig4, filename='Evolution of CO2 emissions per year in Europe.html')


asia_data = data.query("Country == ['China','Japan','India','Iran','Mongolia']")

fig5= px.line(asia_data,x='Year', y='value', color='Country')
fig5.update_layout(title='<b>Evolution of CO2 emissions per year in Asia</b>',xaxis_title='', yaxis_title='')
#fig5.show()
plotly.offline.plot(fig5, filename='Evolution of CO2 emissions per year in Asia.html')



america_data = data.query("Country == ['United States','Canada','Brazil','Mexico','Argentina']")

fig6 = px.line(america_data,x='Year', y='value', color='Country')
fig6.update_layout(title='<b>Evolution of CO2 emissions per year in America</b>',xaxis_title='', yaxis_title='')
#fig6.show()
plotly.offline.plot(fig6, filename='Evolution of CO2 emissions per year in America.html')


other_data = data.query("Country == ['United States','France','China','United Kingdom']")

fig7 = px.line(other_data,x='Year', y='value', color='Country')
fig7.update_layout(title='<b>Evolution of CO2 emissions per year</b>',xaxis_title='', yaxis_title='')
#fig7.show()
plotly.offline.plot(fig7, filename='Evolution of CO2 emissions per year.html')

data_2017 = data.query("Country != 'World' and Year=='2017'")
data_2017 = data_2017[~pd.isna(data_2017['Code'])]


fig8 = px.choropleth(data_2017, locations="Code",
                    color="value",
                    hover_name="Country",
                    color_continuous_scale='burgyl',
                   title='<b>CO2 Emission map by country in 2017</b>')
#fig8.show()
plotly.offline.plot(fig8, filename='CO2 Emission map by country in 2017.html')
