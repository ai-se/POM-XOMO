from Problems.Helper.Objective import Objective
from Problems.Helper.Decision import Decision
from Problems.Helper.Problem import Problem
from Problems.POM3.Helper.pom3 import pom3


class POM3D(Problem):
    "POM3D"

    def __init__(self):
        self.name = "POM3D"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism", "Size", "Plan", "Team Size"]
        lows = [0.10, 0.82, 2, 0.60, 80, 1, 0, 0, 10]
        ups = [0.20, 1.26, 8, 0.95, 100, 10, 2, 5, 20]
        self.decisions = [Decision(names[i], lows[i], ups[i]) for i in range(len(names))]
        self.objectives = [Objective("Cost", True), Objective("Score", True), Objective("Idle", True)]

    def evaluate(self, input=None):
        p3 = pom3()
        return p3.simulate(input)
