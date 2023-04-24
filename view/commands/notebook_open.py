# МОДУЛЬ РЕАЛИЗУЕТ КЛАСС COMMANDOPEN
from .commands import Command


class NotebookOpen(Command):         # КЛАСС РЕАЛИЗУЕТ ЗАПОЛНЕНИЕ ЕЖЕДНЕВНИКА ДАННЫМИ ИЗ ФАЙЛА

    def description(self):           # МЕТОД ВОЗВРАЩАЕТ ОПИСАНИЕ КОМАНДЫ
        return "Открыть ежедневник   "

    def execute(self):               # МЕТОД ОБЕСПЕЧИВАЕТ ЗАПОЛНЕНИЕ ЕЖЕДНЕВНИКА ДАННЫМИ ИЗ ФАЙЛА
        self.console.open_notebook()