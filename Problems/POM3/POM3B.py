from Problems.Helper.Objective import Objective
from Problems.Helper.Decision import Decision
from Problems.Helper.Problem import Problem
from Problems.POM3.Helper.pom3 import pom3


class POM3B(Problem):
    """ POM3B """
    def __init__(self):
        Problem.__init__(self)
        self.name = "POM3B"
        names = ["Culture", "Criticality", "Criticality Modifier", "Initial Known", "Inter-Dependency", "Dynamism", "Size", "Plan", "Team Size"]
        lows = [0.10, 0.82, 80, 0.40, 0,   1, 0, 0, 1]
        ups  = [0.90, 1.26, 95, 0.70, 100, 50, 2, 5, 20]
        self.decisions = [Decision(names[i], lows[i], ups[i]) for i in range(len(names))]
        self.objectives = [Objective("Cost", True), Objective("Score", True), Objective("Idle", True)]
        self.p3 = pom3()

    def evaluate(self, decisions):
        return self.p3.simulate(decisions)
