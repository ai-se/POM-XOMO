from Problems.POM3.POM3A import POM3A
from Problems.POM3.POM3B import POM3B
from Problems.POM3.POM3C import POM3C
from Problems.POM3.POM3D import POM3D

from Problems.XOMO.XOMO_all import XOMO_all
from Problems.XOMO.XOMO_flight import XOMO_flight
from Problems.XOMO.XOMO_ground import XOMO_ground
from Problems.XOMO.XOMO_osp import XOMO_osp
from Problems.XOMO.XOMO_osp2 import XOMO_osp2

# Number of candidates to be generated
no_of_population = 100

# Problems
problems = [
    POM3A(),
    POM3B(),
    POM3C(),
    POM3D(),
    XOMO_all(),
    XOMO_flight(),
    XOMO_ground(),
    XOMO_osp(),
    XOMO_osp2()
]

solution_folder = "Solutions/"
for problem in problems:
    solutions = [problem.create_header()]
    for _ in xrange(no_of_population):
        independent = problem.generate_input()
        dependent = problem.evaluate(independent)
        solutions.append(independent + dependent)

    # Saving the solutions
    f = open(solution_folder + problem.name + '.csv',  'w')
    for solution in solutions:
        f.write(','.join(map(str, solution)) + '\n')
    f.close()
