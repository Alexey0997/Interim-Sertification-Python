# МОДУЛЬ РЕАЛИЗУЕТ АБСТРАКТНЫЙ КЛАСС VIEW

from abc import ABC, abstractmethod


class View(ABC):                                  # АБСТРАКТНЫЙ КЛАСС, РЕАЛИЗУЮЩИЙ ДВА АБСТРАКТНЫХ МЕТОДА

    @abstractmethod
    def set_presenter(self, presenter):
        """
        Aбстрактный метод, принимающий экземпляр класса-презентер в качестве аргумента.
        """

    @abstractmethod
    def start(self):
        """
        Aбстрактный метод, выполняющий настрокйку консольного приложени.
        """