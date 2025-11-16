from task1.solver_factory import SolverFactory


def main():
    print("Введите коэффициенты уравнения через пробел (например, для x^2 - 3x + 2 = 0 введите 1 -3 2):")

    input_str = input("Коэффициенты: ")
    coeffs = [float(c) for c in input_str.split()]

    first_nonzero_index = 0
    while first_nonzero_index < len(coeffs) and coeffs[first_nonzero_index] == 0:
        first_nonzero_index += 1

    coeffs = coeffs[first_nonzero_index:]

    if not coeffs:
        print("Все коэффициенты - нули. Бесконечное количество решений.")
        return

    factory = SolverFactory()

    solver = factory.create_solver(coeffs)

    if solver:
        roots = solver.solve(coeffs)

        print("\nРезультат:")
        if not roots:
            print("Нет решений или бесконечное количество решений.")
        else:
            print(f"Степень уравнения: {len(coeffs) - 1}")
            print("Найденные корни:")
            for i, root in enumerate(roots):
                if abs(root.imag) < 1e-9:
                    print(f"  Корень {i + 1}: {root.real:.4f}")
                else:
                    print(f"  Корень {i + 1}: {root:.4f}")

    else:
        degree = len(coeffs) - 1
        print(f"Ошибка: Решение для уравнений степени {degree} не поддерживается.")

if __name__ == "__main__":
    main()
