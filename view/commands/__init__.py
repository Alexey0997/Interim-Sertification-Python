# _init_.py - предназначен для иницилизации пакета commands и обеспечения импорта данных.

from .commands import Command
from .notebook_open import NotebookOpen
from .tasks_show import TasksShow
from .task_filter import TaskFilter
from .task_add import TaskAdd
from .task_change import TaskChange
from .task_remove import TaskRemove
from .task_save import TaskSave
from .program_exit import ProgramExit
from .menu import Menu