# МОДУЛЬ ПРЕДНАЗНАЧЕН ДЛЯ ЗАПИСИ, ЧТЕНИЯ И СОХРАНЕНИЯ ДАННЫХ В ФАЙЛ В ФОРМАТЕ SCV.

import csv
from .task import Task
from .notebook import Notebook


class FileRecorder:

    def __init__(self, path: str):                                             # КОНСТРУКТОР КЛАССА.
        self.path = path

    def file_write(self, notebook: Notebook):                                  # МЕТОД ЗАПИСИ ДАННЫХ В ФАЙЛ.
        with open(self.path, 'w', encoding='1251', newline='') as data:
            writer = csv.writer(data, delimiter=';')
            writer.writerow(['№', 'Задача', 'Перечень мероприятий', 'Срок выполнения', 'Дата и время создания',
                             'Дата и время изменения'])
            for i, note in enumerate(notebook.get_notes(), start=1):
                writer.writerow([i, note.get_task(), note.get_note(), note.get_deadline(),
                                 note.get_creation_data(), note.get_changes_data()])

    def file_read(self, notebook: Notebook):                                   # МЕТОД ЧТЕНИЯ И СОХРАНЕНИЯ ДАННЫХ.
        try:
            with open(self.path, 'r', encoding='1251') as data:
                reader = csv.reader(data, delimiter=';')
                for i, note_list in enumerate(reader):
                    if i:
                        notebook.get_notes().append(Task(note_list[1], note_list[2], note_list[3],
                                                         note_list[4], note_list[5]))
        except FileNotFoundError:
            pass
        return notebook