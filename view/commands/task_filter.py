# МОДУЛЬ ВЫВОДА ЗАПИСЕЙ, ОТФИЛЬТРОВАННЫХ ПО ДАТЕ

from .commands import Command


class TaskFilter(Command):                     # КЛАСС ВЫВОДА ДАННЫХ ЕЖЕДНЕВНИКА, ОТФИЛЬТРОВАННЫХ ПО ДАТЕ

    def description(self):                     # МЕТОД ВЫВОДА НАИМЕНОВАНИЯ КОМАНДЫ
        return "Вывод задач по дате  "

    def execute(self):                         # МЕТОД ФИЛЬТРАЦИИ ЗАМЕТОК ПО ДАТЕ, ВЫБРАННОЙ ПОЛЬЗОВАТЕЛЕМ
        self.console.show_date_filter()