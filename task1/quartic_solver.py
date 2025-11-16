import cmath

from task1.cubic_solver import CubicSolver
from task1.equation_solver import EquationSolver


class QuarticSolver(EquationSolver):
    """Решает уравнения четвертой степени вида ax^4 + bx^3 + cx^2 + dx + e = 0 (метод Феррари)."""

    def solve(self, coefficients):
        a, b, c, d, e = [complex(c) for c in coefficients]

        B = b / a
        C = c / a
        D = d / a
        E = e / a

        p = C - (3 * B ** 2) / 8
        q = D + (B ** 3) / 8 - (B * C) / 2
        r = E - (3 * B ** 4) / 256 + (B ** 2 * C) / 16 - (B * D) / 4

        if abs(q) < 1e-9:
            discriminant = p ** 2 - 4 * r
            z1 = (-p + cmath.sqrt(discriminant)) / 2
            z2 = (-p - cmath.sqrt(discriminant)) / 2

            y_roots = [
                cmath.sqrt(z1), -cmath.sqrt(z1),
                cmath.sqrt(z2), -cmath.sqrt(z2)
            ]
        else:
            cubic_solver = CubicSolver()
            m_roots = cubic_solver.solve([8, 8 * p, 2 * p ** 2 - 8 * r, -q ** 2])
            m = m_roots[0]

            alpha_sq = 2 * m + p
            alpha = cmath.sqrt(alpha_sq)
            beta_sq = -q / (2 * alpha) if alpha != 0 else -(m ** 2 + m * p + (m * p ** 2 - r * p - q ** 2 / 4) / (
                    2 * m + p))
            beta = cmath.sqrt(beta_sq) if alpha == 0 else -q / (2 * alpha)

            d1 = alpha ** 2 - 4 * (m + beta)
            y1 = (-alpha + cmath.sqrt(d1)) / 2
            y2 = (-alpha - cmath.sqrt(d1)) / 2

            d2 = alpha ** 2 - 4 * (m - beta)
            y3 = (alpha + cmath.sqrt(d2)) / 2
            y4 = (alpha - cmath.sqrt(d2)) / 2

            y_roots = [y1, y2, y3, y4]

        sub = B / 4
        roots = [y - sub for y in y_roots]

        return roots
