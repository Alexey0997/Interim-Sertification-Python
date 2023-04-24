# МОДУЛЬ РЕАЛИЗУЕТ АБСТРАКТНЫЙ КЛАСС COMMAND

from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, console):                                 # КОНСТРУКТОР КЛАССА
        self.console = console

    @abstractmethod
    def description(self):
        """Aбстрактный метод, возвращающий содержание команд."""

    @abstractmethod
    def execute(self):
        """Aбстрактный метод, выполняющий последовательность действий по реализации команды."""