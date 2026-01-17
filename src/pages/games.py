from nicegui import ui
import csv

def games_page():
    with open("giocate.csv", "rw") as giocate:
        
        with ui.row().classes('w-full'):
            ui.space()
            ui.button(icon='add', on_click= lambda: ui.navigate.to(f'/giocate/new'))
        columns = [
            {'headerName': 'Data', 'field': 'date', 'filter': 'agTextColumnFilter'},
            {'headerName': 'Spesa', 'field': 'cost', 'filter': "agSetColumnFilter"},
            {'headerName': 'Vincita', 'field': 'win', 'filter': "agSetColumnFilter"}
        ]
        table = ui.aggrid({'columnDefs': columns, 'rowData': giocate}, theme='quartz') \
            .classes('w-full h-[80vh]')
