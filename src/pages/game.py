from nicegui import ui
import csv

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

def new_game_page(giocate):        
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
