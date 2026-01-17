from nicegui import ui
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import csv

global giocate

@ui.page("/list")
def games():
    global giocate
    navigation_bar("Lista")
    with ui.row().classes('w-full'):
        ui.space()
        ui.button(icon='add', on_click= lambda: ui.navigate.to(f'/new'))
    columns = [
        {'headerName': 'Data', 'field': 'date', 'filter': 'agTextColumnFilter'},
        {'headerName': 'Spesa', 'field': 'cost'},
        {'headerName': 'Vincita', 'field': 'win'},
        {'headerName': 'Totale', 'field': 'result', 'cellClassRules': {
            'bg-red-300': 'x < 0',
            'bg-green-300': 'x > 0',
        }}
    ]
    table = ui.aggrid({'columnDefs': columns, 'rowData': giocate}, theme='quartz') \
        .classes('w-full h-[80vh]')


@ui.page("/new")
def new_game():
    global giocate
    navigation_bar("Nuova")
    def add_game(date, cost, win):
        with open("giocate.csv", "w") as csv_file:
            fieldnames = ['date', 'cost', 'win', 'result']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            giocate.append({
                "date": date,
                "cost": cost,
                "win": win,
                "result": win - cost
            })
            for g in giocate:
                writer.writerow(g)
            
        ui.navigate.to("/")

        
    game = dict()
    with ui.card().classes('w-full'):
        with ui.row():
            ui.label("Data")
            ui.date_input().on_value_change(lambda e: game.update({"date": e.value}))
        with ui.row():
            ui.label("Costo")
            ui.number().on_value_change(lambda e: game.update({"cost": e.value}))
        with ui.row():
            ui.label("Vincita")
            ui.number().on_value_change(lambda e: game.update({"win": e.value}))
    with ui.row().classes('w-full'):
        ui.space()
        ui.button(icon='save', on_click= lambda: add_game(**game))


@ui.page("/")
def dashboard():
    navigation_bar("Giocate")
    with ui.card().classes("w-full"):
        with ui.row().classes("w-full"):
            tot = sum([i["result"] for i in giocate])
            perc = sum([i["win"] for i in giocate if i["win"] > 0]) / sum([1 for i in giocate])
            wins = sum([i["win"] for i in giocate])
            costs = sum([i["cost"] for i in giocate])
            ui.label(f"Totale: {tot:.2f} €")
            ui.label(f"Percentuale Vittorie: {perc:.2f} %")
            ui.label(f"Vincite Totali: {wins:.2f} €")
            ui.label(f"Uscite Totali: {costs:.2f} €")
        
    ui.space()
    ui.fab("add").on('click', lambda: ui.navigate.to('/new')).classes("mx-auto")

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
