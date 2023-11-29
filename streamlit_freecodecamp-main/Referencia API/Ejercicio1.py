import streamlit as st
import pandas as pd
my_data_frame = pd.read_excel("Melsol-test.xlsx", engine="openpyxl")
# Mostrar cualquier cosa
st.write("Hello, world!")
st.write(my_data_frame)
st.image("./Imagen1.png", caption="Descripcion de mi imagen")

st.markdown("Hello world!")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
#Emogis
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.markdown(r"$\acute{e}$")  # É
st.markdown(r"$\ddot{u}$")   # Ü
st.markdown(r"$\hat{o}$")    # Ô

st.markdown(r"$\left(\frac{a}{b}\right)$")     # Fracción con paréntesis grandes
st.markdown(r"$\sqrt{2}$")                       # Raíz cuadrada
st.markdown(r"$\sum_{i=1}^{n} x_i$")             # Sumatorio con límites

st.latex(r"\begin{aligned} x &= 2 \\ y &= 3 \end{aligned}")

# Sistema de ecuaciones

st.markdown(r"$\alpha \beta \gamma \delta$")     # Letras griegas
st.markdown(r"$\sin(x)$")                        # Función trigonométrica

st.latex(r"\begin{bmatrix} 2 & 3 \\ 3 & 4 \end{bmatrix}")
st.latex(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}")
st.latex(r"x = \begin{cases} a &\text{si } x = 0 \\ c &\text{si } x = 1 \end{cases}")
# Matriz 2x2
st.markdown(r"$\int_{a}^{b} f(x) \,dx$")        # Integral definida
st.markdown(r"$\lim_{{n \to \infty}}$")         # Límite

# Utilizando st.latex con \href
st.latex(r"\href{https://katex.org/}{\KaTeX}")

# Otra opción: usando Markdown
st.markdown("[KaTeX](https://katex.org/)")


md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)