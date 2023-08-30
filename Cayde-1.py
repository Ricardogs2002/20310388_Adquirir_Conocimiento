# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 08:12:30 2023

@author: Fam Gomez Sanchez
"""
import time
from nltk.chat.util import Chat, reflections

def cargar_pares_desde_archivo(nombre_archivo):
    pares = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split('|')
            patron = partes[0].strip()
            respuestas = [respuesta.strip() for respuesta in partes[1:]]
            pares.append([patron, respuestas])
    return pares

def chatear():
    print("Hola soy Cayde, escribe algo para comenzar")
    
    pares = cargar_pares_desde_archivo("conocimiento.txt")
    chat = Chat(pares, reflections)
    
    while True:
        mensaje_usuario = input("Tú: ")
        if mensaje_usuario.lower() == "finalizar":
            print("Cayde: Chao")
            break
        
        respuesta = chat.respond(mensaje_usuario)
        if respuesta is None:
            print("Cayde: No sé que responder a esto aún, ¿Te parece si me enseñas?.")
            nueva_pregunta = mensaje_usuario.lower()
            time.sleep(1)
            nueva_respuesta = input("Cayde: ¿Y cuál sería la respuesta adecuada a esa pregunta? ")
            pares.append([nueva_pregunta, [nueva_respuesta]])
            with open("conocimiento.txt", "a", encoding='utf-8') as archivo:
                archivo.write(f"\n{nueva_pregunta} | {nueva_respuesta}")
                time.sleep(2)
            print("Cayde: Entendido, he añadido ese conocimiento a mi base de datos.")
            pares = cargar_pares_desde_archivo("conocimiento.txt")
            chat = Chat(pares, reflections)
        else:
            print("Cayde:", respuesta)

if __name__ == "__main__":
    chatear()
