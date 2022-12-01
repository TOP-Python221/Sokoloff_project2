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
    def __init__(self, patterns: dict,
                 joy: int,
                 anger: int):
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
        self.brithdate = birthdate
        self.body = body
        self.mind = mind


        #tired()
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





class BodyState:
    def __init__(self, timestamp: dt,
                 health:int,
                 stamina:int,
                 hunger: int,
                 thirst: int):
        self.timestamp = timestamp
        self.stamina = stamina
        self.health = health
        self.hunger = hunger
        self.thirst = thirst

class MindState:
    def __init__(self, timestamp: dt,
                 joy: int,
                 anger: int,
                 pattern):
        self.timestamp = timestamp
        self.joy = joy
        self.anger = anger
        self.pattern = pattern


class StatesManger:
    def __init__(self, body_history: list[BodyState],
                 mind_last: MindState):
        self.body_history = body_history
        self.mind_last = mind_last