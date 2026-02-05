from nicegui import ui
import datetime
import matplotlib.pyplot as plt
from data.game import Game

def dashboard_page(giocate: list[Game]):
    months = list(set([m["date"].split("-")[1] for m in giocate]))
    month_values = [sum(g["win"] for g in giocate if g["date"].split("-")[1] == m) for m in months]

    weekdays = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
    weekday_values = [sum(g["win"] for g in giocate if datetime.datetime.strptime(g["date"], "%Y-%m-%d").weekday() == wd) for wd in range(0,7)]
    weekdays_all = filter(lambda x: x[1] != 0,zip(weekdays, weekday_values))
    weekdays, weekday_values = zip(*weekdays_all)
    
    tot = sum([i["result"] for i in giocate])
    perc = sum([1 for i in giocate if i["result"] > 0]) / sum([1 for _ in giocate]) * 100
    wins = sum([i["win"] for i in giocate])
    costs = sum([i["cost"] for i in giocate])

    win_lose = [perc, 100 - perc]

    with ui.row().classes("w-full"):
        ui.space()
        ui.button(icon='add', on_click= lambda: ui.navigate.to('/new'))
    with ui.card().classes("w-full"):
        with ui.row(align_items="center").classes("flex-auto text-xl"):
            ui.label(f"Totale: {tot:.2f} €").classes("flex-auto")
            ui.label(f"Percentuale Vittorie: {perc:.2f} %").classes("flex-auto")
            ui.label(f"Vincite Totali: {wins:.2f} €").classes("flex-auto")
            ui.label(f"Uscite Totali: {costs:.2f} €").classes("flex-auto")
    with ui.card().classes("w-full"):
        with ui.row(align_items="center").classes("w-full"):
            with ui.matplotlib(figsize=(3, 2)).classes("flex-auto").figure as fig:
                ax = fig.gca()
                ax.set_title("Numero vittorie")
                ax.pie(win_lose, labels=["Vincite", "Perdite"], colors=["lightgreen", "#F67280"])
        with ui.row(align_items="center").classes("w-full"):

            with ui.matplotlib(figsize=(3, 2)).classes("flex-auto").figure as fig:
                ax = fig.gca()
                ax.set_title("Vittorie per mese")
                ax.pie(month_values, labels=months)

            with ui.matplotlib(figsize=(3, 2)).classes("flex-auto").figure as fig:
                ax = fig.gca()
                ax.set_title("Vittorie per giorno della settimana")
                ax.pie(weekday_values, labels=weekdays)
