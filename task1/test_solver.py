import unittest

from task1.cubic_solver import CubicSolver
from task1.linear_solver import LinearSolver
from task1.quadratic_solver import QuadraticSolver
from task1.quartic_solver import QuarticSolver
from task1.solver_factory import SolverFactory


class TestEquationSolvers(unittest.TestCase):

    def assertRootsAlmostEqual(self, roots1, roots2, places=7):
        self.assertEqual(len(roots1), len(roots2))

        sorted_roots1 = sorted(roots1, key=lambda x: (x.real, x.imag))
        sorted_roots2 = sorted(roots2, key=lambda x: (x.real, x.imag))

        for r1, r2 in zip(sorted_roots1, sorted_roots2):
            self.assertAlmostEqual(r1.real, r2.real, places=places)
            self.assertAlmostEqual(r1.imag, r2.imag, places=places)

    # --- для LinearSolver ---
    def test_linear_simple(self):
        solver = LinearSolver()
        roots = solver.solve([2, 4])  # 2x + 4 = 0
        self.assertRootsAlmostEqual(roots, [-2])

    def test_linear_no_solution(self):
        solver = LinearSolver()
        roots = solver.solve([0, 5])  # 0x + 5 = 0
        self.assertEqual(roots, [])

    # --- для QuadraticSolver ---
    def test_quadratic_two_real_roots(self):
        solver = QuadraticSolver()
        roots = solver.solve([1, -3, 2])  # x^2 - 3x + 2 = 0
        self.assertRootsAlmostEqual(roots, [1, 2])

    def test_quadratic_one_real_root(self):
        solver = QuadraticSolver()
        roots = solver.solve([1, -2, 1])  # x^2 - 2x + 1 = 0
        self.assertRootsAlmostEqual(roots, [1, 1])

    def test_quadratic_complex_roots(self):
        solver = QuadraticSolver()
        roots = solver.solve([1, 0, 4])  # x^2 + 4 = 0
        expected = [complex(0, 2), complex(0, -2)]
        self.assertRootsAlmostEqual(roots, expected)

    # --- для CubicSolver ---
    def test_cubic_three_real_roots(self):
        solver = CubicSolver()
        roots = solver.solve([1, -6, 11, -6])  # x^3 - 6x^2 + 11x - 6 = 0
        self.assertRootsAlmostEqual(roots, [1, 2, 3])

    def test_cubic_one_real_two_complex(self):
        solver = CubicSolver()
        roots = solver.solve([1, -1, 1, -1])  # x^3 - x^2 + x - 1 = 0
        expected = [1, complex(0, 1), complex(0, -1)]
        self.assertRootsAlmostEqual(roots, expected)

    # ---  для QuarticSolver ---
    def test_quartic_four_real_roots(self):
        solver = QuarticSolver()
        roots = solver.solve([1, -10, 35, -50, 24])  # x^4 - 10x^3 + 35x^2 - 50x + 24 = 0
        self.assertRootsAlmostEqual(roots, [1, 2, 3, 4])

    def test_quartic_biquadratic_complex(self):
        solver = QuarticSolver()
        roots = solver.solve([1, 0, 5, 0, 4])  # x^4 + 5x^2 + 4 = 0
        expected = [complex(0, 1), complex(0, -1), complex(0, 2), complex(0, -2)]
        self.assertRootsAlmostEqual(roots, expected)

    def test_quartic_repeated_roots(self):
        solver = QuarticSolver()
        roots = solver.solve([1, -4, 6, -4, 1])  # (x-1)^4 = 0
        self.assertRootsAlmostEqual(roots, [1, 1, 1, 1])

    def test_quartic_mixed_roots(self):
        solver = QuarticSolver()
        roots = solver.solve([1, 0, 0, 0, -1])  # x^4 - 1 = 0
        expected = [1, -1, complex(0, 1), complex(0, -1)]
        self.assertRootsAlmostEqual(roots, expected)

    # --- для фабрики и логики в main ---
    def test_factory_with_leading_zeros(self):
        coefficients = [0, 0, 1, -3, 2]  # 0x^4 + 0x^3 + x^2 - 3x + 2 = 0

        effective_coefficients = coefficients[2:]  # -> [1, -3, 2]

        factory = SolverFactory()
        solver = factory.create_solver(effective_coefficients)

        self.assertIsInstance(solver, QuadraticSolver)

        roots = solver.solve(effective_coefficients)
        self.assertRootsAlmostEqual(roots, [1, 2])


if __name__ == '__main__':
    unittest.main()
