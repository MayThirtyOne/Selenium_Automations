import os
from PIL import Image, ImageOps, ImageDraw, ImageFont
import random
from PIL import ImageEnhance
import json


class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

        
directory='G:/Desktop/lordofthunder-pcmwars_website-fa77afacacfe/imgprocessing/old/'
directory_final='G:/Desktop/lordofthunder-pcmwars_website-fa77afacacfe/imgprocessing/new1/'

'''
for filename in os.listdir(directory):
    name=os.path.splitext(filename)[0]
    im = Image.open(directory+filename)
    im.save(directory+name+'.png', quality=100)
    print(filename +"done")
'''

name_dict=my_dictionary()

for filename in os.listdir(directory):
    
    name=os.path.splitext(filename)[0]
    im = Image.open(directory+filename)
    width, height = im.size
    scaling_options=[700,800,900,1100,1200,1300]
    scaling_factor=random.choice(scaling_options)
    scaling_factor_percentage=scaling_factor/1000
    new_width=int(width/scaling_factor_percentage)
    new_height=int(height/scaling_factor_percentage)
    resized_image=im.resize((new_width, new_height)).convert("RGBA")
    img_with_border = ImageOps.expand(resized_image,border=3,fill='#000000')
    #img_with_border.save(directory+filename,quality=100)
    enh_bri = ImageEnhance.Brightness(img_with_border)
    brightness = 0.9
    image_brightened = enh_bri.enhance(brightness)
    enh_col = ImageEnhance.Color(image_brightened)
    color = 0.10
    image_colored = enh_col.enhance(color)
    enh_con = ImageEnhance.Contrast(image_colored)
    contrast = 0.90
    image_contrasted = enh_con.enhance(contrast)
    enh_sha = ImageEnhance.Sharpness(image_contrasted)
    sharpness = 2.0
    image_sharped = enh_sha.enhance(sharpness)
    final_name="Sphere_Rank_img_"+str(random.randint(0,100000))+"_batch_"+str(random.randint(100000,200000))+"_module_"+str(random.randint(200000,300000))+".png"
    image_sharped.save(directory_final+final_name,quality=100)
    
    name_dict.add(filename,final_name)
    
    
    print(filename, "done")
    #print(new_width,new_height)
   
'''    
for filename in os.listdir(directory):
    name=os.path.splitext(filename)[0]
    photo = Image.open(directory+filename)
    w,h = photo.size
    #font = ImageFont.truetype("RobotoBlack.ttf", 68)
    drawing = ImageDraw.Draw(photo)
    text = "© " + "SphereRank.com" + "   "
    text_w, text_h = drawing.textsize(text)
    pos = w - text_w, (h - text_h) - 3
    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0,0), text, fill="#ffffff", )
    c_text.putalpha(100)
    photo.paste(c_text, pos, c_text)
    photo.save(directory+filename,quality=100)

'''

with open('result.json', 'w') as fp:
    json.dump(name_dict, fp,indent = 4)





print("All done")













    
