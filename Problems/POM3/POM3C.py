from Problems.Helper.Objective import Objective
from Problems.Helper.Decision import Decision
from Problems.Helper.Problem import Problem
from Problems.POM3.Helper.pom3 import pom3


class POM3C(Problem):
    """ POM3C """
    def __init__(self):
        Problem.__init__(self)
        self.name = "POM3C"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism", "Size", "Plan", "Team Size"]
        lows = [0.50, 0.82, 2, 0.20, 0, 40, 2, 0, 20]
        ups = [0.90, 1.26, 8, 0.50, 50, 50, 4, 5, 44]
        self.decisions = [Decision(names[i], lows[i], ups[i]) for i in range(len(names))]
        self.objectives = [Objective("Cost", True), Objective("Score", True), Objective("Idle", True)]
        self.p3 = pom3()

    def evaluate(self, decisions):
        return self.p3.simulate(decisions)
