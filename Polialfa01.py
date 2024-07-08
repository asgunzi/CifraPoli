# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 02:31:26 2024

@author: ASGUNZI
"""


import streamlit as st

from math import ceil

def cifrarPoli(mensagem, tamBloco, chaves):
    #Mensagem a ser cifrada
    #Tamanho do bloco (int)
    #Chaves como uma lista de inteiros

    #Transforma tudo em minúsculo
    msg2 = mensagem.lower()
    
    
    #Divide a mensagem em blocos
    nblocos = ceil(len(mensagem)/tamBloco)
    nchaves = len(chaves)

    msgOut =""
    
    for i in range(nblocos):
        ini = i*tamBloco
        fim = (i+1)*tamBloco
        msg1  = msg2[ini:fim]
        
        print(msg1)
        idx_chv = i % nchaves
        chv = chaves[idx_chv]
        
        msgOut += cifrarCesar(msg1, chv)
         
    
    return(msgOut)

def decifrarPoli(mensagem, tamBloco, chaves):
    #Mensagem a ser cifrada
    #Tamanho do bloco (int)
    #Chaves como uma lista de inteiros

    #Transforma tudo em minúsculo
    msg2 = mensagem.lower()
    
    
    #Divide a mensagem em blocos
    nblocos = ceil(len(mensagem)/tamBloco)
    nchaves = len(chaves)

    msgOut =""
    
    for i in range(nblocos):
        ini = i*tamBloco
        fim = (i+1)*tamBloco
        msg1  = msg2[ini:fim]
        
        idx_chv = i % nchaves
        chv = chaves[idx_chv]
        
        msgOut += decifrarCesar(msg1, chv)
         
    
    return(msgOut)
    


def cifrarCesar(mensagem, chave):
    
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
    alfnovo =alfabeto[chave:] + alfabeto[:chave]
    
    #Cria um dicionário
    dicAlfabeto ={}
    for k in range(len(alfabeto)):
        dicAlfabeto[alfabeto[k]] = alfnovo[k]
        
    
    #Só para conferir o alfabeto novo    
    #print(alfnovo)
    
    msgOut =""
    
    #Transforma tudo em minúsculo
    msg2 = mensagem.lower()
    
    for ch in msg2:
        if ch in alfabeto:
            msgOut += dicAlfabeto[ch]
        else:
            msgOut += ch
    
    return(msgOut)
    
    
def decifrarCesar(mensagem, chave):
    
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
    alfnovo =alfabeto[chave:] + alfabeto[:chave]
    
    #Cria um dicionário
    dicAlfabeto ={}
    for k in range(len(alfabeto)):
        dicAlfabeto[alfnovo[k]] = alfabeto[k]
    #Aqui a chave é oposta. Tenho alfnovo e quero o alfabeto original
    
    
    msgOut =""
    
    #Transforma tudo em minúsculo
    msg2 = mensagem.lower()
    
    for ch in msg2:
        if ch in alfnovo:
            msgOut += dicAlfabeto[ch]
        else:
            msgOut += ch
    
    return(msgOut)


#-------------------------------------
#Sidebar menu
st.sidebar.title("Menu")

st.sidebar.markdown("[Home](https://asgunzi.neocities.org)")

st.sidebar.markdown("[Cifra de César](https://cesarsimples.streamlit.app/)")
st.sidebar.markdown("[Cifra Polialfabética](https://polialfa01py-bdaxz4f6ehzi38ehcg8ndp.streamlit.app/)")
st.sidebar.markdown("[Cifra Transposição](https://cifratransposicao.streamlit.app/)")
#-------------------------------------




st.image("https://ideiasesquecidas.com/wp-content/uploads/2024/07/forgottenmath.png")
st.title("Exemplo - Cifra PoliAlfabética")

col1, col2, col3 = st.columns([1, 2, 2])

with col1:
    nbloco = int( st.text_input("Tamanho do bloco: ", value = 5))

with col2:
    inputChaves = st.text_input("Chaves (separar por vírgula): ", value = "1,2,3")

user_input = st.text_input("Entre texto a cifrar:")

# Check if the input is not empty
if user_input:
    # Cifrar mensagem
    chaves = inputChaves.split(",")
    lstChaves =[]
    for ch in chaves:
        lstChaves.append(int(ch))
    
    msgCifrada = cifrarPoli(user_input, nbloco, lstChaves)
    
    # Display the reversed text
    st.write("Mensagem cifrada:")
    st.write(msgCifrada)
    
#Marca separatória
st.markdown("---")

user_input2 = st.text_input("Entre texto a decifrar:")

# Check if the input is not empty
if user_input2:
    # Decifrar mensagem

    msgDecifrada= decifrarPoli(user_input2, nbloco, lstChaves)
    
    # Display the reversed text
    st.write("Mensagem decifrada:")
    st.write(msgDecifrada)
    
    
