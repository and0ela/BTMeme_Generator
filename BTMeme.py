import bpy
import math
import os
import streamlit as st
from PIL import Image

def render():
    bpy.ops.wm.open_mainfile(filepath="BTMeme.blend")
    bpy.context.preferences.filepaths.font_directory = ".\impact-font"
    scene = bpy.context.scene
    objects = []
    with open(".\in_word.txt","r") as word_file:
        word = word_file.read()
    word_split = word.split('_')
    bottom_word = word_split[-1]
    word_split.reverse()
    word_split = word.split('_')
    bottom_word = word_split[-1]
    word_split.reverse()
    #Setup plane
    bpy.ops.mesh.primitive_plane_add(size=30, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(30, 30, 30))
    floor_mesh = bpy.context.active_object
    objects.append(floor_mesh)
    #set material
    try:
        mat = bpy.data.materials.get("floor")
    except:
        mat = bpy.data.materials.new("floor")
    floor_mesh.active_material = mat
    with open("E:\Comp Sci III\Blender App\\rgb.txt","r") as file_rgb:
        str_rgb = file_rgb.read()
        lst_rgb = str_rgb.split(" ")
    red = float(lst_rgb[0])
    green = float(lst_rgb[2])
    blue = float(lst_rgb[1])
    floor_mesh.active_material.diffuse_color = (red,green,blue,1)
    #setup light
    bpy.ops.object.light_add(type='SUN', align='WORLD', location=(0.817, -2.0997, 0.85807), scale=(1, 1, 1))
    bpy.context.object.data.energy = 75
    objects.append(bpy.context.active_object)
    #Setup all text, run backwards
    jump = 0
    x_size = 0
    cam_jump = 0
    cam_roty_jump = 0
    cam_rotz_jump = 0
    for w in word_split:
        bpy.ops.object.text_add(align = 'WORLD', location = (0,0,0))
        word = bpy.context.active_object
        objects.append(word)
        bpy.ops.font.open(filepath="//..\\BTMeme Generator\\impact-font\\unicode.impact.ttf", relative_path=True)
        #fnt = bpy.data.fonts.load("E:\Comp Sci III\BTMeme Generator\impact-font\impact.ttf")
        word.data.body = w
        word.data.font = bpy.data.fonts.get("Impact Regular")
        word.rotation_euler[0] = math.radians(90)
        word.data.extrude = 0.2
        bpy.ops.object.convert(target = "MESH")
        word.location.z += (1.35*jump)
        jump += word.dimensions.z
        if (word_split.index(w) == 0):
            x_size = word.dimensions.x
            print("Success!")
        word.dimensions.x = (x_size/word.dimensions.x)*word.dimensions.x
        word.dimensions.x = (x_size/word.dimensions.x)*word.dimensions.x
        #Adds dimensions for cam positioning later
        bpy.context.view_layer.update()
        cam_jump += 0.09

    bpy.ops.object.camera_add(location = (0.28279,-0.49618,0.161259), rotation = ( math.radians(114.656), 0, 0))
    cam = bpy.data.objects['Camera']
    objects.append(cam)
    cam.data.lens = 14
    cam.data.clip_start = 0.001
    cam.location.x += -1*cam_jump
    cam.location.y += -1*cam_jump
    cam = bpy.context.active_object
    scene.camera = cam
    rotation = (math.atan((0.4*(len(bottom_word) / (cam.location.y -0.263767 ))   )))
    #print(rotation)
    cam.rotation_euler.z = rotation
    """""
    A = null 
    B = 135
    C = null
    a = (bottom_word*0.4)
    b = null
    c = cam_jump*math.sqrt(2)"""""


    bpy.data.scenes["Scene"].render.filepath = "//..\\BTMeme Generator\\renders\\"
    bpy.ops.render.render(write_still = True)
    print("rendered!")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global = False)
    st.image(Image.open('./renders/.png'))
    bpy.ops.wm.save_as_mainfile(filepath="BTMeme.blend")

render()














