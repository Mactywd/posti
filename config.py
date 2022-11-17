import pygame
import sys
import os
import json

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

w = 800; h = 650
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Randomizer Posti")
pygame.display.set_icon(pygame.image.load(resource_path('dependencies/icon.png')))
phase = 'main_menu' # Part of the application
ppl = json.loads(open(resource_path("dependencies/ppl.json")).read()) # List of peaple
rows = 5; cols = 6
sound = True
