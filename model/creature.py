# ИСПРАВИТЬ: внимательнее – здесь вы импортировали модуль и именем объекта модуля аннотировали параметры в методах, когда вам нужен объект класса из этого модуля
import datetime as dt

__all__ = [
    'Creature'
]


class Body:
    def __init__(self, health: int,
                 stamina: int,
                 hunger: int,
                 thirst: int):
        self.health = health
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst


class Mind:
    def __init__(self,
                 patterns: dict,
                 joy: int,
                 anger: int):
        # ИСПРАВИТЬ: это должно быть атрибутом класса, не экземпляра
        self.patterns = patterns
        self.joy = joy
        self.anger = anger

    @property
    def pattern(self):
        pass


class Creature:
    def __init__(self, name: str,
                 birthdate: dt,
                 body: Body,
                 mind: Mind):
        self.name = name
        self.birthdate = birthdate
        self.body = body
        self.mind = mind

        # tired()
        # sleep()



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

