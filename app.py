import streamlit as st
import random

st.set_page_config(page_title="Perguntas pra você 💖", page_icon="💌", layout="centered")

# Fundo personalizado com CSS
st.markdown("""
    <style>
        body {
            background-color: #fff0f5;
        }
        .big-title {
            font-size: 36px;
            color: #ff69b4;
            text-align: center;
        }
        .heart {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Coração animado (GIF online)
st.markdown('<div class="heart"><img src="https://media.tenor.com/4DYoNaJYZf8AAAAi/heart-love.gif" width="120"></div>', unsafe_allow_html=True)

# Título
st.markdown('<p class="big-title">Oi, linda! 💖</p>', unsafe_allow_html=True)

# Entrada do nome
nome = st.text_input("Qual das ficantes é voce, Digite o nome aqui embaixo imunda")

if nome:
    st.write(f"oi , {nome}! Responda essas pora aqui carai 👇")

    perguntas = [
        "Qual sua comida preferida?",
        "Qual sua bebida favorita?",
        "Qual sua sobremesa dos sonhos?",
        "Se você pudesse comer uma coisa agora, o que seria?",
        "Qual seu restaurante favorito?",
        "Qual sabor de pizza você mais ama?",
        "Qual o seu prato favorito feito pela sua mãe?"
    ]

    respostas = {}
    perguntas_sorteadas = random.sample(perguntas, 3)

    for pergunta in perguntas_sorteadas:
        resposta = st.text_input(pergunta)
        if resposta:
            respostas[pergunta] = resposta

    if len(respostas) == 3:
        st.success("Obrigaaado por responder meu anjo 🥰")
        st.markdown(f"**{nome}**, sabia que eu te amo sabia :D 💕")
        st.markdown("Te amo viu chata imunda, TE AMOOOOO ❤️")
        st.balloons()