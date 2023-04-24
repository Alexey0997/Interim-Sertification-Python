# МОДУЛЬ ДОБАВЛЕНИЯ НОВЫХ ЗАПИСЕЙ В ЕЖЕДНЕВНИК
from .commands import Command


class TaskAdd(Command):         # КЛАСС РЕАЛИЗУЮЩИЙ ДОБАВЛЕНИЕ ЗАПИСЕЙ В ЕЖЕДНЕВНИК

    def description(self):      # МЕТОД ВЫВОДА НА ПЕЧАТЬ КОМАНДЫ
        return "Добавить задачу      "

    def execute(self):          # МЕТОД ДОБАВЛЕНИЯ НОВОЙ ЗАПИСИ
        self.console.add_note()