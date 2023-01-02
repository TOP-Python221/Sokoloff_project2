from dataclasses import dataclass
from datetime import datetime as dt


from .creature import Body, Mind, Creature
from src.utils.constans import Kind, Matureness, MatureDays, RangesDict

__all__ = [
    'KindParamerters'
    'StatesManager',
    'StatesCalculator',
]








@dataclass
class BodyState:
    """
    """

    def to_dict(self) -> dict:
        return {}


@dataclass
class MindState:
    """
    """
    timestamp: dt
    joy: int
    anger:int


    def to_dict(self) -> dict:
        return {
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'joy': self.joy,
            'anger': self.anger
        }


class StatesManager:
    """
    """
    def __init__(self,
                 kind: Kind,
                 name: str,
                 birthdate: dt,
                 body_states: list[BodyState],
                 mind_state: MindState):
        self.kind = kind
        self.name = name
        self.birthdate = birthdate
        self.body_states = body_states
        self.mind_states = mind_state

    def to_dict(self) -> dict:
        return {}


class DictOfRanges:
    pass


class KindParamerters:
    """"""
    def __init__(self,
                 title: str,
                 maturity: tuple,
                 egg: Ranges,
                 cub: Ranges,
                 young: Ranges,
                 aduilt:Ranges,
                 elder:Ranges):
        self.title = title
        self.maturity = maturity
        self.egg = egg
        self.cub = cub
        self.young = young
        self.adult = aduilt
        self.elder = elder

    @property
    def age_ranges() -> Ranges:
        """"""
    class Ranges:
        """Перечисляет физические параметры существа"""
        def __init__(self,
                     health: DictOfRanges,
                     stamina: DictOfRanges,
                     hunger: DictOfRanges,
                     thirst:DictOfRanges,
                     insestense: DictOfRanges,
                     joy: ParamRange = (0,100),
                     joy_coeff: float,
                     activity: ParamRange,
                     anger: ParamRange = (0, 100),
                     anger_coeff: float,
                     anxienty: ParamRange):
            self.health = health
            self.stamina = stamina
            self.hunger = hunger
            self.thirst = thirst
            self.insestense = insestense
            self.joy = joy
            self.joy_coeff = joy_coeff
            self.activity = activity
            self.anger = anger
            self.anger_coeff = anger_coeff
            self.anxienty = anxienty

        def __int__(self,
                    kind_title: str,
                    maturation_days: MatureDays,
                    **mature_ranges: RangesDict):
            self.title = kind_title
            if len(maturation_days) == 3:
                self.maturation = Matureness.mammals()
            elif len(maturation_days) == 4:
                self.maturation = list(Matureness)
            else:
                raise Exception("'matiration_days' argument should be of 3 or 4 numbers lenght")
            self.mature_days = (0,) + tuple(maturation_days)
            for attr in  self.maturation:
                setattr(self, attr, self.__class__.Ranges(
                    mature_ranges[attr]['health'],
                    mature_ranges[attr]['stamina'],
                    mature_ranges[attr]['hunger'],
                    mature_ranges[attr]['thirst']
                ))
        def age_ranges(self, days: int):
            """"""
            for age, attr in zip(self.mature_days, self.maturation):
                if days % age:
                    return getattr(self,attr)



#__iter__()





class StatesCalculator:
    """
    """
    def __init__(self,
                 kind:KindParamerters,
                 last: StatesManager):
        self.__kind = kind
        self.last = last
    def _new_body(self) -> Body:
        """"""

    def _new_mind(self) -> Mind:
        """"""

    def new_creature(self) -> Creature:
        """"""