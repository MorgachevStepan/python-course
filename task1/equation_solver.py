from abc import ABC, abstractmethod


class EquationSolver(ABC):
    """Абстрактный базовый класс для решателей уравнений."""

    @abstractmethod
    def solve(self, coefficients):
        """
        Основной метод, который должен быть реализован в каждом решателе.
        Принимает список коэффициентов [a, b, c, ...].
        Возвращает список корней.
        """
        pass
