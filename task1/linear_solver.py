from task1.equation_solver import EquationSolver


class LinearSolver(EquationSolver):
    """Решает линейные уравнения вида ax + b = 0."""

    def solve(self, coefficients):
        a, b = coefficients

        if a == 0:
            return []

        root = -b / a
        return [root]
