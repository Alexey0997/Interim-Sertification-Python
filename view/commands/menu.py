# МОДУЛЬ РЕАЛИЗУЕТ КЛАСС MENU

from .task_add import TaskAdd
from .task_change import TaskChange
from .program_exit import ProgramExit
from .task_filter import TaskFilter
from .notebook_open import NotebookOpen
from .task_remove import TaskRemove
from .task_save import TaskSave
from .tasks_show import TasksShow


class Menu:                                                  # КЛАСС ФОРМИРУЕТ МЕНЮ И ЗАПУСКАЕТ МЕТОДЫ РЕАЛИЗАЦИИ КОМАНД
    def __init__(self, console):
        self.commands = []
        self.commands.append(NotebookOpen(console))          # ОТКРЫТЬ ЕЖЕДНЕВНИК
        self.commands.append(TasksShow(console))             # ВЫВЕСТИ ДАННЫЕ О ЗАПИСЯХ
        self.commands.append(TaskFilter(console))            # ВЫВЕСТИ ЗАПИСИ, ОТФИЛЬТРОВАННЫЕ ПО ДАТЕ
        self.commands.append(TaskAdd(console))               # ДОБАВИТЬ НОВУЮ ЗАПИСЬ
        self.commands.append(TaskChange(console))            # ИЗМЕНИТЬ ЗАПИСЬ ПО ИНДЕКСУ
        self.commands.append(TaskRemove(console))            # УДАЛИТЬ ЗАПИСЬ ПО ИНДЕКСУ
        self.commands.append(TaskSave(console))              # СОХРАНИТЬ ИЗМЕНЕНИЯ
        self.commands.append(ProgramExit(console))           # ВЫЙТИ ИЗ ПРОГРАММЫ

    def __str__(self):                                       # МЕТОД ВОЗВРАЩАЕТ СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ МЕНЮ
        menu_string = "\n\tГЛАВНОЕ МЕНЮ:\n"
        for i, cmd in enumerate(self.commands, start=1):
            menu_string += f"\t{cmd.description()} - нажмите {i}\n"
        return menu_string

    def get_size_menu(self):                                 # МЕТОД ВОЗВРАЩАЕТ ДЛИНУ СПИСКА МЕНЮ
        return len(self.commands)

    def execute(self, index):                                # МЕТОД ЗАПУСКАЕТ КОМАНДУ, ВЫБРАННУЮ ПОЛЬЗОВАТЕЛЕМ
        option = self.commands[index]
        option.execute()