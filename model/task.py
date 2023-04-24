# МОДУЛЬ ПРЕДНАЗНАЧЕН ДЛЯ РЕАЛИЗАЦИИ КЛАССА TASK И РАБОТЫ С НИМ

from datetime import datetime


class Task:                                                                          # КЛАСС СОЗДАНИЯ ЗАПИСИ
    def __init__(self, task, text_note, deadline, creation_data, changes_data=''):   # КОНСТРУКТОР КЛАССА
        self.__task = task
        self.__text_note = text_note
        self.__deadline = deadline
        self.__creation_data = creation_data
        self.__changes_data = changes_data

    def get_task(self):                                          # МЕТОД ВОЗВРАТА НАИМЕНОВАНИЯ ЗАДАЧИ
        return self.__task

    def get_note(self):                                          # МЕТОД ВОЗВРАТА ПЕРЕЧНЯ МЕРОПРИЯТИЙ
        return self.__text_note

    def get_deadline(self):                                      # МЕТОД ВОЗВРАТА СРОКА ВЫПОЛНЕНИЯ ЗАДАЧИ
        return self.__deadline

    def get_creation_data(self):                                 # МЕТОД ВОЗВРАТА ДАТЫ И ВРЕМЕНИ СОЗДАНИЯ ЗАМЕТКИ
        return self.__creation_data

    def get_changes_data(self):                                  # МЕТОД ВОЗВРАТА ДАТЫ И ВРЕМЕНИ ИЗМЕНЕНИЯ ЗАМЕТКИ
        return self.__changes_data

    def change(self, task: str, new_text: str, deadline: str):   # МЕТОД ИЗМЕНЕНИЯ ЗАПИСИ:
        if task:
            self.__task = task                                           # НАИМЕНОВАНИЕ ЗАДАЧИ
        if new_text:
            self.__text_note = new_text                                  # ПЕРЕЧЕНЬ МЕРОПРИЯТИЙ
        if deadline:
            self.__deadline = deadline                                   # СРОК ВЫПОЛНЕНИЯ
        self.__changes_data = datetime.today().strftime('%d.%m.%Y %H:%M')