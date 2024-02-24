import bpy
import os

for id_data in bpy.data.objects:
    bpy.data.objects.remove(id_data)
        
bpy.ops.object.text_add()

font_path = 'C:\\Users\\YunSeong\\Desktop\\사각사각.ttf'
bpy.context.object.data.font = bpy.data.fonts.load(font_path)
bpy.context.object.data.body = "한글"
bpy.context.object.data.extrude = 0.1

bpy.ops.object.convert(target='MESH')
bpy.ops.object.modifier_add(type='DECIMATE')
bpy.context.object.modifiers["Decimate"].ratio = 0.2
bpy.ops.object.modifier_apply(modifier="Decimate")

file_path = 'C:\\Users\\YunSeong\\Desktop\\example.fbx'
bpy.ops.export_scene.fbx(filepath=file_path)