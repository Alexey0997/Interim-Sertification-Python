# МОДУЛЬ РЕАЛИЗУЕТ КЛАСС ЗАВЕРШЕНИЯ РАБОТЫ ПРОГРАММЫ

from .commands import Command


class ProgramExit(Command):                     # КЛАСС ЗАВЕРШЕНИЯ РАБОТЫ ПРОГРАММЫ

    def description(self):                      # МЕТОД ВЫВОДА НА ПЕЧАТЬ КОМАНДЫ ВЫХОДА ИЗ ПРОГРАММЫ
        return "Выйти из программы   "

    def execute(self):                          # МЕТОД ЗАВЕРШЕНИЯ РАБОТЫ ПРОГРАММЫ
        self.console.finish()