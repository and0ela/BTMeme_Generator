import streamlit as st
import subprocess
from PIL import Image
import math
import os




def call_blender(word,rgb):
    print("calling")
    with open("in_word.txt","w") as file1:
        file1.write(word)
    with open("rgb.txt","w") as file2:
        file2.write(rgb)
    subprocess.run(["python","BTMeme.py"])
    
    


def hex_to_dec(number,check):
  numberRev = (number)[::-1]
  bases = ['a','b','c','d','e','f']
  basesConv = [10,11,12,13,14,15]
  total = 0
  v = -1
  n = 1
  for i in range(0,len(number)):
    if numberRev[i] in bases:
      total = total + (((basesConv[bases.index(numberRev[i])]))*n)
    else:
      total = total + (int(numberRev[i])*n)
    v = v - 1
    n = n*16
  if check ==1:
    print(number, ' (base 16) in base ten is equal to ',total,sep = '')
  else:
    print(total)
    return(round(total/255,3))
  


st.title("Big Text Meme Generator")

col1, col2 = st.columns(2)

with col1:
  word = st.text_input("Input the words you want. Separate words with spaces and lines with '_'! " )
  word.upper()
  st.subheader("Pick the floor color!")
  color = st.color_picker("")


r = hex_to_dec(color[1:3],0)
g = hex_to_dec(color[3:5],0)
b = hex_to_dec(color[5:7],0)
print("r: ",color[1:3])
print("g: ",color[3:5])
print("b: ",color[5:7])

rgb = (str(r)+ " " + str(b) + " " + str(g))



st.write( "(R,G,B):", rgb)

if st.button("Click to render!"):
   call_blender(word,rgb)
   with col2:
    st.image(Image.open('./renders/.png'))







