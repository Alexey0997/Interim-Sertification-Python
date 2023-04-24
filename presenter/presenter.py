# МОДУЛЬ РЕАЛИЗУЕТ КЛАСС PRESENTER
from model.file_recorder import FileRecorder


class Presenter:                                                    # КЛАСС РЕАЛИЗУЕТ ВЗАИМОДЕЙСТВИЕ МЕЖДУ MODEL И VIEW
    def __init__(self, view, notebook, path):                       # КОНСТРУКТОР КЛАССА
        self.__view = view
        self.__notebook = notebook
        self.__view.set_presenter(self)
        self.file = FileRecorder(path)

    def open_file(self):                                            # МЕТОД ОТКРЫТИЯ И ЧТЕНИЯ ДАННЫХ ИЗ ФАЙЛА
        self.__notebook = self.file.file_read(self.__notebook)

    def get_date_filter(self, date):                            # МЕТОД ВЫВОДА ЗАПИСЕЙ, ОТФИЛЬТРОВАННЫХ ПО ДАТЕ
        return self.__notebook.date_filter(date)

    def add_note(self, task_text, note_text, deadline_text):        # МЕТОД ДОБАВЛЕНИЯ НОВОЙ ЗАПИСИ В ЕЖЕДНЕВНИК
        self.__notebook.add_note(task_text, note_text, deadline_text)

    def change_note(self, index, update_task, update_note, update_deadline):   # МЕТОД ИЗМЕНЕНИЯ ЗАПИСИ
        self.__notebook.change_note(index, update_task, update_note, update_deadline)

    def remove_note(self, index):                                   # МЕТОД УДАЛЕНИЯ ЗАПИСИ ИЗ ЕЖЕДНЕВНИКА
        self.__notebook.remove_note(index)

    def save(self):                                                 # МЕТОД СОХРАНЕНИЯ ИЗМЕНЕНИЙ В ЕЖЕДНЕВНИКЕ
        self.file.file_write(self.__notebook)

    def is_full(self):                                              # МЕТОД ПРОВЕРКИ НАЛИЧИЯ ЗАПИСЕЙ В ЕЖЕДНЕВНИКЕ
        return self.__notebook.is_full()

    def get_size_notebook(self):                                    # МЕТОД ВОЗВРАТА ДЛИНЫ ЗАПИСЕЙ
        return self.__notebook.size()

    def get_table_notebook(self):                                   # МЕТОД ЗАПИСИ ДАННЫХ В ТАБЛИЦУ
        return self.__notebook.table_creation