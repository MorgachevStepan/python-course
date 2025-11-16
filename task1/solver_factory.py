from task1.cubic_solver import CubicSolver
from task1.linear_solver import LinearSolver
from task1.quadratic_solver import QuadraticSolver
from task1.quartic_solver import QuarticSolver


class SolverFactory:
    """Фабрика для создания объектов-решателей."""

    @staticmethod
    def create_solver(coefficients):
        """
        Создает и возвращает экземпляр нужного решателя
        в зависимости от количества коэффициентов.
        """
        degree = len(coefficients) - 1

        if degree == 1:
            return LinearSolver()
        elif degree == 2:
            return QuadraticSolver()
        elif degree == 3:
            return CubicSolver()
        elif degree == 4:
            return QuarticSolver()
        else:
            return None
