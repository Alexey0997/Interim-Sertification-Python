# МОДУЛЬ РЕАЛИЗУЕТ КЛАСС CONSOLE, ОТВЕЧАЮЩИЙ ЗА ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС

from .commands.menu import Menu
from .view_abc import View


class Console(View):                                                  # КЛАСС РЕАЛИЗУЕТ ВЗАИМОДЕЙСТВИЕ С ПОЛЬЗОВАТЕЛЕМ
    __working = False
    __save = True
    __open = False

    def __init__(self):                                               # КОНСТРУКТОР КЛАССА
        self.presenter = None

    def set_presenter(self, presenter):                               # ИНИЦИАЛИЗАЦИЯ ОБЪЕКТА PRESENTER В КОНСОЛИ
        self.presenter = presenter

    def start(self):                                                  # МЕТОД ЗАПУСКА ПРОГРАММЫ В КОНСОЛИ
        self.__working = True
        menu = Menu(self)
        while self.__working:
            print(menu)
            index = self.__get_index(menu.get_size_menu(), "\tВАШЕ РЕШЕНИЕ: ")
            menu.execute(index)

    def open_notebook(self):                                          # МЕТОД ОТКРЫТИЯ ЕЖЕДНЕВНИКА
        if not self.__open:
            self.presenter.open_file()
            self.__open = True
            if self.presenter.is_full():
                print("\n\tЕжедневник открыт.")
            else:
                print("\nВ ежедневнике нет записей.")
        else:
            print("\nЕжедневник открыт.")

    def show_all(self):                                                # МЕТОД ВЫВОДА ВСЕХ ЗАПИСЕЙ ЕЖЕДНЕВНИКА
        if self.presenter.is_full():
            print("\n                                                   С О Д Е Р Ж А Н И Е  Е Ж Е Д Н Е В Н И К А",
                  self.presenter.get_table_notebook(), sep='\n')
        else:
            print("\nЕжедневник закрыт или в нем нет записей.")

    def show_date_filter(self):                                     # МЕТОД ВЫВОДА ЗАДАЧ, ОТФИЛЬТРОВАННЫХ ПО ДАТЕ
        if self.presenter.is_full():
            date = input("Введите дату, для которой нужно напечатать заадчи (дд.мм.гггг): ")
            print(f"\n{date} В ЕЖЕДНЕВНИК БЫЛИ ВНЕСЕНЫ СЛЕДУЮЩИЕ ЗАПИСИ: ",
                  self.presenter.get_date_filter(date), sep='\n')
        else:
            print("\nЕжедневник закрыт или в нем нет записей.")

    def add_note(self):                                                  # МЕТОД ДОБАВЛЕНИЯ НОВОЙ ЗАПИСИ В ЕЖЕДНЕВНИК
        new_task = input("\nВведите наименование задачи: ")
        new_note = input("\nВведите перечень мероприятий для выполнения: ")
        new_deadline = input("\nВведите срок выполнения задачи: ")
        self.presenter.add_note(new_task, new_note, new_deadline)
        print("\nЗадача добавлена в ежедневник.\n")
        self.__save = False

    def change_note(self):                                                # МЕТОД ИЗМЕНЕНИЯ ЗАПИСИ ПО ЕЕ ИНДЕКСУ
        if self.presenter.is_full():
            print("\n                                                   С О Д Е Р Ж А Н И Е  Е Ж Е Д Н Е В Н И К А",
                  self.presenter.get_table_notebook(), sep='\n')
        else:
            print("\nЕжедневник закрыт или в нем нет записей.")
        if self.presenter.is_full():
            index = self.__get_index(self.presenter.get_size_notebook(),
                                     "\nВведите номер задачи, которую нужно изменить: ")
            update_task = input("\nОбновите наименование задачи или нажмите ввод: ")
            update_note = input("\nОбновите содержание мероприятий или нажмите ввод: ")
            update_deadline = input("\nОбновите срок выполнения задчи или нажмите ввод: ")
            self.presenter.change_note(index, update_task, update_note, update_deadline)
            self.__save = False
            print("\nЗапись изменена.\n")
        else:
            print("\nЕжедневник закрыт или в нем нет записей.")

    def remove_note(self):                                                # МЕТОД УДАЛЕНИЯ ЗАПИСИ ПО ЕЕ ИНДЕКСУ
        if self.presenter.is_full():
            print("\n                                                   С О Д Е Р Ж А Н И Е  Е Ж Е Д Н Е В Н И К А",
                  self.presenter.get_table_notebook(), sep='\n')
        else:
            print("\nЕжедневник закрыт или в нем нет записей.")
        if self.presenter.is_full():
            index = self.__get_index(self.presenter.get_size_notebook(),
                                     "\nВведите номер задачи, которую нужно удалить: ")
            self.presenter.remove_note(index)
            self.__save = False
            print("\nЗапись удалена.\n")
        else:
            print("\nЕжедневник закрыт или в нем нет записей.")

    def save_changes(self):                                            # МЕТОД СОХРАНЕНИЯ ИЗМЕНЕНИЙ
        if not self.__open:
            print("\nЕжедневник закрыт. В случае сохранения, предыдущие записи будут удалены.\n")
            answer = input("\nСохранить изменения? Введите 'да' или 'нет': ").lower()
            if answer == 'да':
                self.presenter.save()
                self.__save = True
                print("\nИзменения сохранены.")
        else:
            self.presenter.save()
            self.__save = True
            print("\nИзменения сохранены.")

    @staticmethod
    def __get_index(size, text):                                       # МЕТОД ВОЗВРАТА ИНДЕКСА ЗАМЕТКИ
        while True:
            user_input = input(text)
            if (user_input.isdigit() and
                    1 <= int(user_input) <= size):
                index = int(user_input) - 1
                return index
            print(f"\nВведите число от 1 до {size}")

    def finish(self):                                                   # МЕТОД ЗАВЕРШЕНИЯ РАБОТЫ ПРОГРАММЫ
        if self.__save:
            self.__working = False
            print("\nЗавершение работы.")
            return
        answer = input("\nСохранить изменения? Введите 'да' или 'нет': ").lower()
        if answer == 'да' and self.__open:
            self.presenter.save()
            self.__save = True
            print("\nИзменения сохранены.")
        elif answer == 'да' and not self.__open:
            print("\nЕжедневник закрыт. В случае сохранения, предыдущие записи будут удалены.\n")
            answer_2 = input("\nСохранить изменения? Введите 'да' или 'нет': ").lower()
            if answer_2 == 'да':
                self.presenter.save()
                self.__save = True
                print("\nИзменения сохранены.")
        self.__working = False
        print("\nЗавершение работы.")