from .creature import Body, Mind, Creature

__all__ = [
    'StatesManager',
    'StatesCalculator',
]


# ДОБАВИТЬ: объявления классов Ranges и KindParameters


# ДОБАВИТЬ: поля согласно модели (используйте декоратор dataclass)
class BodyState:
    """
    """

    def to_dict(self) -> dict:
        return {}


# ДОБАВИТЬ: поля согласно модели (используйте декоратор dataclass)
class MindState:
    """
    """
    def to_dict(self) -> dict:
        return {}


class StatesManager:
    """
    """
    # ДОБАВИТЬ: конструктор

    def to_dict(self) -> dict:
        return {}


class StatesCalculator:
    """
    """
    def _new_body(self) -> Body:
        """"""

    def _new_mind(self) -> Mind:
        """"""

    def new_creature(self) -> Creature:
        """"""