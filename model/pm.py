from pathlib import Path
from sys import path

from .states import StatesManager
# ИСПРАВИТЬ: следите за именами, что вы импортируете — ваш файл называется constans.py
from utils.constants import pathlike

__all__ = [
    'PersistenceManager',
]



class PersistenceManager:
    """
    """
    default_states_path = Path(path[0]) / 'model/states.json'
    default_ranges_path = Path(path[0]) / 'model/ranges.json'

    @classmethod
    def read_ranges(cls, kind_name: str, ranges_path: pathlike = None):
        """"""
        # ДОБАВИТЬ: реализацию метода

    @classmethod
    def read_states(cls, states_path: pathlike = None) -> StatesManager:
        """"""
        if not states_path:
            states_path = cls.default_states_path
        # ДОБАВИТЬ: реализацию метода

    @classmethod
    def write_states(cls):
        """"""
        # ДОБАВИТЬ: реализацию метода

