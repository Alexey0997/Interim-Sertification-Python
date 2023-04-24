# МОДУЛЬ УДАЛЕНИЯ ЗАПИСЕЙ ИЗ ЕЖЕДНЕВНИКА

from .commands import Command


class TaskRemove(Command):                # КЛАСС РЕАЛИЗУЕТ УДАЛЕНИЕ ЗАПИСИ

    def description(self):                # МЕТОД ВЫВОДА НАИМЕНОВАНИЯ КОМАНДЫ
        return "Удалить задачу       "

    def execute(self):                    # МЕТОД УДАЛЕНИЯ ЗАПИСИ ПО ИНДЕКСУ, ВЫБРАННОМУ ПОЛЬЗОВАТЕЛЕМ
        self.console.remove_note()