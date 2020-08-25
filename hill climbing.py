import random as rd
import matplotlib.pyplot as plt


def qualidade(solution):
    q = sum([s ** 2 for s in solution])
    return q


def tweak(solution):
    tweak_min = -1
    tweak_max = 1
    new_solution = [s + rd.uniform(tweak_min, tweak_max) for s in solution]
    return new_solution


def hill_climbing():
    MAX_ITERATIONS = 1000
    DIMENSIONS = 30
    best_values = []
    solution = [rd.uniform(-5.12, 5.12) for _ in range(DIMENSIONS)]
    for i in range(MAX_ITERATIONS):
        new_solution = tweak(solution)
        if qualidade(solution) > qualidade(new_solution):
            solution = new_solution
        best_values.append(qualidade(solution))
    plt.plot(best_values)
    plt.show()
    return solution


hill_climbing()
