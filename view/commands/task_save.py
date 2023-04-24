# МОДУЛЬ СОХРАНЕНИЯ ИЗМЕНЕНИЙ В ЕЖЕДНЕВНИКЕ

from .commands import Command


class TaskSave(Command):                  # КЛАСС СОХРАНЕНИЯ ИЗМЕНЕНИЙ В ФАЙЛЕ

    def description(self):                # МЕТОД ВЫВОДА НАИМЕНОВАНИЯ КОМАНДЫ
        return "Сохранить изменения  "

    def execute(self):                    # МЕТОД СОХРАНЕНИЯ ИЗМЕНЕНИЙ В ФАЙЛЕ
        self.console.save_changes()