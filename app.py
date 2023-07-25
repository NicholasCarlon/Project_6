# Introduction: this code creates a scatter plot and a histogram of a dataset of cars using Streamlit and Plotly Express.
# These plots include checkboxes to eliminate or show outliers in each visual

# import necessary packages

import streamlit as st
import pandas as pd
import plotly_express as px

# load sample data

df = pd.read_csv('new_car_data.csv')

st.header("""
The Market of Used Cars
""")

st.write("""
### This application helps us take a closer look at data surrounding new & used cars.
""")

# creating checkbox that allows the user to show or hide new cars within the application
st.write("""
###### Would you like to show or hide new cars?
""")
show_new_cars = st.checkbox('Show New Cars')

if not show_new_cars:
    df = df[df.condition!='new']


# creating a histogram with multiple data aspects, and the inclusion of a selectbox that the user can interact with
st.header('Price Analysis')

st.write("""
###### Use the dropdown to select different attributes. You will discover how each attribute affects the vehicle price.
""")

histogram_list = ['condition', 'type', 'transmission', 'paint_color']
histogram_choice = st.selectbox('Select Variable', histogram_list)

histogram_1 = px.histogram(df, 'price', color=histogram_choice,)

histogram_1.update_layout(
    title="<b> Breakdown of price by {}</b>".format(histogram_choice))

show_histogram_checkbox = st.checkbox('Show Outliers', value=False)

if show_histogram_checkbox:
    histogram_1.update_layout(xaxis_range=[0, 200000])
else:
    histogram_1.update_layout(xaxis_range=[0, 80000])

histogram_1.show()

st.plotly_chart(histogram_1)


# creating a scatter plot for price distribution

st.header('Distribution of Prices by Odometer Miles')

fig_scatter_new = px.scatter(df, x='price', y='odometer', color='condition',
                             color_discrete_map={
                                "new": "green",
                                "like new": "blue",
                                "excellent": "orange",
                                "good": "yellow",
                                "fair": "red",
                                "salvage": "black"
                             },
                             category_orders={'condition': ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']})

fig_scatter_new.update_layout(xaxis_title='Price', yaxis_title='Odometer')

# creating a checkbox to view outliers

show_outliers_scatter = st.checkbox('Show Me Outliers', value=False)

if show_outliers_scatter:
    fig_scatter_new.update_layout(xaxis_range=[0, 350000])
    fig_scatter_new.update_layout(yaxis_range=[0, 500000])
else:
    fig_scatter_new.update_layout(xaxis_range=[0, 100000])
    fig_scatter_new.update_layout(yaxis_range=[0, 350000])

# fig_scatter_new.show()

st.plotly_chart(fig_scatter_new)


# creating a histogram for price distribution

st.header('Distribution of Prices by Vehicle Condition')

fig_histo_new = px.histogram(df, x='price', color='condition', marginal='rug',
                             color_discrete_map={
                                "new": "green",
                                "like new": "blue",
                                "excellent": "orange",
                                "good": "yellow",
                                "fair": "red",
                                "salvage": "black"
                             },
                             category_orders={'condition': ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']}
                             )

fig_histo_new.update_layout(xaxis_title='Price', yaxis_title='Count')

# creating a checkbox to view outliers

show_outliers_histo = st.checkbox('Show The Outliers', value=False)

if show_outliers_histo:
    fig_histo_new.update_layout(xaxis_range=[0, 350000])
else:
    fig_histo_new.update_layout(xaxis_range=[0, 100000])

# fig_histo_new.show()

st.plotly_chart(fig_histo_new)


# Conclusion: This code successfully creates a scatter plot and a histogram of sample dataset of cars using Plotly Express and Streamlit.