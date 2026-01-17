from nicegui import ui
import csv

def add_game(date, cost, win):
    with open("giocate.csv", "w") as giocate:
        giocate.append({
            "date": date,
            "cost": cost,
            "win": win
        })

def new_game_page():
    game = {
        "date": "",
        "cost": None,
        "win": None
    }
    with ui.card().classes('w-full'):
        with ui.row():
            ui.label("Data")
            ui.date_input().on("update:model-value", lambda e: game.setattr("date", e))
        with ui.row():
            ui.label("Costo")
            ui.number().on("update:model-value", lambda e: game.setattr("cost", e))
        with ui.row():
            ui.label("Vincita")
            ui.number().on("update:model-value", lambda e: game.setattr("win", e))

    with ui.row().classes('w-full'):
        ui.space()
        ui.button(icon='save', on_click= lambda: add_game(**game))
