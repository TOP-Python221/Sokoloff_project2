from datetime import datetime as dt

__all__ = [
    'StatesCalculator'
]


class BodyState:
    def __init__(self,
                 timestamp: dt,
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
    def __init__(self,
                 timestamp: dt,
                 joy: int,
                 anger: int,
                 pattern):
        self.timestamp = timestamp
        self.joy = joy
        self.anger = anger
        self.pattern = pattern


class StatesManager:
    def __init__(self,
                 body_history: list[BodyState],
                 mind_last: MindState):
        self.body_history = body_history
        self.mind_last = mind_last


class StatesCalculator:
    pass

