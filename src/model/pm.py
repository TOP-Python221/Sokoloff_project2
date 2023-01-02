from pathlib import Path
from sys import path
from json import load as jload, dump as jdump
from datetime import datetime as dt

from .states import StatesManager,KindParamrters
# ИСПРАВИТЬ: следите за именами, что вы импортируете — ваш файл называется constans.py
from src.utils.constans import pathlike

__all__ = [
    'PersistenceManager',
]


def jload(filein):
    pass


class PersistenceManager:
    """
    """
    default_states_path = Path(path[0]) / 'model/states.json'
    default_ranges_path = Path(path[0]) / 'model/ranges.json'

    @classmethod
    def read_ranges(cls, kind: Kind, parameters_path: pathlike = None) -> KindParamrters:
        """"""
        if not parameters_path:
            parameters_path = cls.default_parameters_path
            
        with open(parameters_path, encoding='utf -8') as filein:
            data = jload(filein)[kind.value]

        return KindParamrters(
            data['title'],
            data['maturation'],
            **data['ranges']
        )

    @classmethod
    def read_states(cls, states_path: pathlike = None) -> StatesManager:
        """"""
        if not states_path:
            states_path = cls.default_states_path

        with open(states_path,encoding='utf-8') as filein:
            data = jload(filein)

        data['kind'] = Kind(data['kind'])
        data['birthdate'] = dt.strptime(data['birthdate'], '%Y-%m-%d %H:%M:%S')
        for bs in data['body_states'] + [data['mind_state']]:
            bs['timestamp'] = dt.strptime(bs['timestamp'], '%Y-%m-%d %H:%M:%S')

        return StatesManager(**data)
    @classmethod
    def write_states(cls, data: dict,states_path: pathlike = None):
        """"""
        if not states_path:
            states_path = cls.default_states_path

        with open(states_path, 'w', encoding='utf-8') as fileout:
            jdump(data,fileout)

