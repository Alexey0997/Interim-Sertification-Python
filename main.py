# МОДУЛЬ ЗАПУСКА ПРОГРАММЫ

from model.notebook import Notebook
from presenter.presenter import Presenter
from view.console import Console

if __name__ == '__main__':
    model = Notebook()
    view = Console()
    presenter = Presenter(view, model, 'notebook.csv')
    view.start()