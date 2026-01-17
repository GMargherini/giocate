from nicegui import ui
import matplotlib.pyplot as plt
from pages.games import games_page
from pages.game import new_game_page
from pages.dashboard import dashboard_page
import numpy as np
import sys
import os
import csv

global giocate

@ui.page("/list")
def games():
    navigation_bar("Lista")
    games_page(giocate)

@ui.page("/new")
def new_game():
    navigation_bar("Nuova")
    new_game_page(giocate)

@ui.page("/")
def dashboard():
    navigation_bar("Giocate")
    dashboard_page(giocate)
    
def navigation_bar(title: str = ''):
    ui.colors(primary='#FAB12F')
    ui.query('body').classes('bg-orange-50')
    links = 'align-middle w-full text-black text-lg p-2 m-0 hover:bg-orange-200 hover:cursor-pointer'
    icons = 'text-3xl p-1 w-[16dp] rounded hover:bg-orange-700 hover:cursor-pointer'
    with ui.header(elevated=True).classes('text-white bg-[#FA812F] items-center h-[60px] justify-between'):
        ui.label(title).classes('text-2xl truncate flex-[2] hover:cursor-default').tooltip(title)
        ui.icon('home').on('click', lambda: ui.navigate.to(f'/')).classes(icons).tooltip('Home')
        ui.icon('menu').on('click', lambda: ui.navigate.to(f'/list')).classes(icons).tooltip('Lista')

def main():
    global giocate
    with open("giocate.csv", "r") as csv_file:
        dict_reader = csv.DictReader(csv_file)
        giocate = []
        for giocata in dict_reader:
            giocate.append({
                "date": giocata['date'],
                "cost": float(giocata['cost']),
                "win": float(giocata['win']),
                "result": float(giocata['win']) - float(giocata['cost'])
            })

    ui.run(dashboard, title="Giocate", favicon='🎰', port=8080)

if __name__ in {"__main__", "__mp_main__"}:
    main()
