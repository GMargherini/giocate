from nicegui import ui
from data.game import Game

def games_page(giocate: list[Game]):
    with ui.row().classes('w-full'):
        ui.space()
        ui.button(icon='add', on_click= lambda: ui.navigate.to('/new'))
    columns = [
        {'headerName': 'Data', 'field': 'date', 'filter': 'agTextColumnFilter', 'flex': 2, 'suppressMovable': True},
        {'headerName': 'Spesa', 'field': 'cost', 'flex': 1, 'suppressMovable': True},
        {'headerName': 'Vincita', 'field': 'win', 'flex': 1, 'suppressMovable': True},
        {'headerName': 'Totale', 'field': 'result', 'flex': 1, 'suppressMovable': True, 'cellClassRules': {
            'bg-red-300': 'x < 0',
            'bg-green-300': 'x > 0',
        }}
    ]
    table = ui.aggrid({'columnDefs': columns, 'rowData': giocate}, theme='quartz').classes('w-full h-[80vh]')
