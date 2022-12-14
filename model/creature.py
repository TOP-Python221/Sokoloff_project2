from abc import ABC
from datetime import datetime as dt


# Все равно ругается pycharm
from utils.constans import KindActions

__all__ = {
    'CreatureFactory',
    'Creature', }



class Body:
    """
    Изначальные физиоолгические параметры
    """

    def __init__(self,

                 health: int,
                 stamina: int,
                 hunger: int,
                 thirst: int):
        self.health = health
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst

    def tick_changes(self, parameters: 'KindActions') -> dict:
        """Собирает изменения за тик"""
        return {'health': 2, 'stamina': -3, 'hunger': 4, 'thirst': 2}


class Mind:
    """
    Психологические параметры
    """
    def __init__(self,
                 joy: int,
                 anger: int):
        self.joy = joy
        self.anger = anger

    @property
    def pattern(self):
        pass


class Creature(ABC):
    """
    Создание существа
    """
    def __init__(self,
                 kind_parameters: 'KindActions',
                 body: Body,
                 mind: Mind):
        self.__kind = kind_parameters
        self.body = body
        self.mind = mind

    # ДОБАВИТЬ: документацию свойства
    @property
    def age(self):
        """"""
        return
        # ДОБАВИТЬ: реализацию свойства

    def apply_tick_changes(self):
        # ДОБАВИТЬ: документацию метода
        """"""
        for state in (self.body, self.mind):
            for attr, delta in state.tick_changes(self.__kind).items():
                new_value = getattr(self.body, attr) + delta
                setattr(self.body, attr, new_value)

        # tired()
        # sleep()

    def mainloop(self):
        """"""

class State:
    def __init__(self, timestamp: dt,
                 health: int,
                 stamina: int,
                 hunger: int,
                 thirst:int,
                 joy: int,
                 activity: float,
                 anger: int,
                 anxiety: float):
        self.timestamp = timestamp
        self.health = health
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst
        self.joy = joy
        self.activity = activity
        self.anger = anger
        self.anxiety = anxiety

    @property

    def body(self) -> dict:
        """"""
        pass

    def mind(self) -> dict:
        """"""
        pass

    def dict(self) -> dict:
        """"""
        pass




class CreatureActions(Creature):
    """
    Хранит состояние активностей существа
    """

    def get_fried(self):
        """"""

    def seek_for_honey(self):
        """"""

    def get_warm_on_sun(self):
        """"""


class Cat(Creature):
    pass


class Dog(Creature):
    pass


class Fox(Creature):
    pass


class Bear(Creature):
    pass


