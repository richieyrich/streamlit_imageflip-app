import streamlit as st
import time as t

#     FUNCTIONS


# add title
st.title('welcome there')

# add header
st.header('first header')

# sub header
st.subheader(" subheader")

# info
st.info(' this is info')

# warning
st.warning('warning message')

# error
st.error('error message')

# write data or code
st.write(range(50))
st.write('some writings')

# success message
st.success(' success')

# markdown

st.markdown('# this is markdown')
st.markdown('## this is markdown')
st.markdown('### this is markdown')
st.markdown(':smile: :moon: :cry:')

# text
st.text('this is some text')

# caption
st.caption(' our caption')

# display mathematical expressions
st.latex(r''' a+b x^2+c''')

# open image
st.image("a.jpg")

#   WIDGETS

# radio button
st.radio('ur gender',['male','female','other'])

# check box
st.checkbox('is it good')

# button
st.button('save')

# select box
st.selectbox('select a language', ['c','c++','python'])

# multiselect box
st.multiselect('select a car', [ 'bmw', 'benx', 'lambo','bugatti'])

# select slider
st.select_slider('ur performance',['bad','avg','good','excellent'])

# normal slider
st.slider('temperature',1,100)

# number input
st.number_input('pick a number',0,80)

# text input
st.text_input('email id')

# date and time input
st.date_input(' pick a date')
st.time_input('r time slot')

# text area
st.text_area('write ur findings')

# upload file
st.file_uploader('choose ur file')

# pick a color
st.color_picker(' ur color')

# progress
st.progress(80)

# 
# spinner
with st.spinner('loading'):
    t.sleep(1)


# ballons
st.balloons()

# sidebar
st.sidebar.title(' this our sidebar')
st.sidebar.text_input(' this our text')
st.sidebar.button(' save')

# data visualization

import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(10,2),columns=['x','y'])

# charts
st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)