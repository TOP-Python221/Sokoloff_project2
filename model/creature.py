from abc import ABC

import self as self
from utils.constant import KindActions

__all__ = [
    'Creature',
    'Body',
    'Mind',
]

import patterns as patterns


class Body:
    """
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

    def tick_changes(self, parameters: 'KindParameters') -> dict:
        """Собирает изменения за тик"""
        return {'health': 2, 'stamina': -3, 'hunger': 4, 'thirst': 2}

class Mind:

    patterns = patterns

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

    """
    def __init__(self,
                 kind_parameters: 'Kindparameters',
                 body: Body,
                 mind: Mind):
        self.__kind = kind_parameters
        self.body = body
        self.mind = mind

    @property
    def age(self):
        pass

    def apply_tick_changes(self):
        """"""
        for state in (self.body, self.mind):
            for attr, delta in state.tick_changes(self.__kind).items():
                new_value = getattr(self.body, attr) + delta
                setattr(self.body, attr, new_value)


        # tired()
        # sleep()
    def mainloop(self):
        """"""

class CreatureActions(Creature):
    """

    """
    def run_at_night(self):
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



class CreatureActions(Creature):
    pass

