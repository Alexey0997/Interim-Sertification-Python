# МОДУЛЬ ПРЕДНАЗНАЧЕН ДЛЯ РЕАЛИЗАЦИИ КЛАССА "ЕЖЕДНЕВНИК" И РАБОТЫ С ЗАПИСЯМИ

from datetime import datetime
from tabulate import tabulate
from .task import Task


class Notebook:
    def __init__(self):  # КОНСТРУКТОР КЛАССА
        self.__notes = []

    def size(self):  # МЕТОД ВОЗВРАТА ДЛИНЫ ЗАПИСЕЙ
        return len(self.__notes)

    def add_note(self, task, note, deadline):  # МЕТОД ДОБАВЛЕНИЯ НОВОЙ ЗАПИСИ В ЕЖЕДНЕВНИК
        note = Task(task, note, deadline, datetime.today().strftime('%d.%m.%Y %H:%M'), )
        self.__notes.append(note)

    def remove_note(self, index):  # МЕТОД УДАЛЕНИЯ ЗАПИСИ ИЗ ЕЖЕДНЕВНИКА
        del self.__notes[index]

    def change_note(self, index, task, update_text, update_deadline):  # МЕТОД РЕДАКТИРОВАНИЯ ЗАПИСИ В ЕЖЕДНЕВНИКЕ
        self.__notes[index].change(task, update_text, update_deadline)

    def is_full(self):  # МЕТОД ПРОВЕРКИ НАЛИЧИЯ ЗАПИСЕЙ В ЕЖЕДНЕВНИКЕ
        return bool(self.__notes)

    def get_notes(self):  # МЕТОД ВЫВОДА СПИСКА ЗАПИСЕЙ ЕЖЕДНЕВНИКА
        return self.__notes

    @property
    def table_creation(self):  # МЕТОД ЗАПИСИ ДАННЫХ В ТАБЛИЦУ FANCY-OUTLINE
        headers = ['№', 'Задача', 'Перечень мероприятий', 'Срок выполнения', 'Дата и время записи',
                   'Дата и время изменения']
        table = [[i, note.get_task(), note.get_note(), note.get_deadline(),
                  note.get_creation_data(), note.get_changes_data()]
                 for i, note in enumerate(self.__notes, start=1)]
        return tabulate(table, headers=headers, tablefmt="fancy_outline", stralign='left')

    def date_filter(self, date):  # МЕТОД ВЫВОДА ДАННЫХ ПО ДАТЕ СОЗДАНИЯ ЗАМЕТКИ
        headers = ['№', 'Задача', 'Перечень мероприятий', 'Срок выполнения', 'Дата и время записи',
                   'Дата и время изменения']
        table = [[i, note.get_task(), note.get_note(), note.get_deadline(), note.get_creation_data(),
                  note.get_changes_data()] for i, note in enumerate(self.__notes, start=1)
                 if date in note.get_creation_data() or date in note.get_changes_data()]
        return tabulate(table, headers=headers, tablefmt="fancy_outline", stralign='left')
