import pygame
from os import walk

def import_folder(path):
    surface_list = []
    for _,__,img_files in walk(path):
        #print(f'img_files = {img_files}')
        for image in img_files:
            full_path = path + '/' + image
            #print(f'full path = {full_path}')
            image_surf = pygame.image.load(full_path).convert_alpha() 
            surface_list.append(image_surf)
    
    return surface_list




