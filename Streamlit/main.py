import streamlit as st
import pandas as pd
import numpy as np

# Headings and Subheadings
st.title("Demo app")
st.header("header")
st.subheader("subheader")

# Input
x = st.text_input("Enter your name")
if(x!=""):
    st.write(f"Your name is {x}")

# MARKDWON IN STREAMLIT
st.write("## Markdown in streamlit")
st.markdown("Streamlit is *really* **cool**.")
st.markdown(
    """
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text."""
)
st.markdown(
    "Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:"
)

multi = """If you end a line with two spaces,  
a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# """
st.markdown(multi)

# LATEX
st.latex(r"\begin{pmatrix}a & b\\ c & d\end{pmatrix}")

# Data Manipulation
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data