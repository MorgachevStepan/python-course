import cmath

from task1.equation_solver import EquationSolver


class QuadraticSolver(EquationSolver):
    """Решает квадратные уравнения вида ax^2 + bx + c = 0."""

    def solve(self, coeffs):
        a, b, c = coeffs

        discriminant = b ** 2 - 4 * a * c

        sqrt_discriminant = cmath.sqrt(discriminant)

        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

        return [root1, root2]
