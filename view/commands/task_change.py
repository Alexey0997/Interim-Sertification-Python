# МОДУЛЬ ИЗМЕНЕНИЯ ЗАПИСЕЙ В ЕЖЕДНЕВНИКЕ

from .commands import Command


class TaskChange(Command):          # КЛАСС ИЗМЕНЕНИЯ ЗАПИСИ ПО ВЫБРАННОМУ ИНДЕКСУ

    def description(self):          # МЕТОД ОПИСАНИЯ КОМАНДЫ
        return "Изменить задачу      "

    def execute(self):              # МЕТОД ИЗМЕНЕНИЯ ЗАПИСИ
        self.console.change_note()