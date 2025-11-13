import cmath

from task1.equation_solver import EquationSolver
from task1.quadratic_solver import QuadraticSolver


class CubicSolver(EquationSolver):
    """Решает кубические уравнения вида ax^3 + bx^2 + cx + d = 0."""

    def solve(self, coeffs):
        a, b, c, d = [complex(coef) for coef in coeffs]

        B, C, D = b / a, c / a, d / a

        p = C - (B ** 2) / 3
        q = D + (2 * B ** 3) / 27 - (B * C) / 3

        delta = (q / 2) ** 2 + (p / 3) ** 3
        sqrt_delta = cmath.sqrt(delta)

        u_cubed = -q / 2 + sqrt_delta
        v_cubed = -q / 2 - sqrt_delta

        u = u_cubed ** (1 / 3) if abs(u_cubed) > abs(v_cubed) else ((-p / 3) ** 3 / v_cubed) ** (1 / 3)
        if abs(u) < 1e-9:
            v = v_cubed ** (1 / 3)
        else:
            v = -p / (3 * u)

        y1 = u + v
        root1 = y1 - B / 3

        a_quad = a
        b_quad = b + a * root1
        c_quad = c + b_quad * root1

        quadratic_solver = QuadraticSolver()
        other_roots = quadratic_solver.solve([a_quad, b_quad, c_quad])

        return [root1] + other_roots
