# МОДУЛЬ ВЫВОДА СОДЕРЖАНИЯ ЕЖЕДНЕВНИКА НА КОНСОЛЬ

from .commands import Command


class TasksShow(Command):                     # КЛАСС ВЫВОДА ВСЕХ ЗАПИСЕЙ НА КОНСОЛЬ

    def description(self):                    # МЕТОД ВЫВОДА НАИМЕНОВАНИЯ КОМАНДЫ
        return "Показать список задач"

    def execute(self):                        # МЕТОД ВЫВОДА ЗАПИСЕЙ НА КОНСОЛЬ
        self.console.show_all()