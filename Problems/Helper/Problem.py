from random import uniform


class Problem(object):
    """A representation of a problem """

    def __init__(self):
        self.name = ""
        self.decisions = []
        self.objectives = []

    def generate_input(self):
        "a way to generate decisions for this problem"
        while True:  # repeat if we don't meet constraints
            candidate = [round(uniform(decision.low, decision.up), 5) for decision in self.decisions]
            if self.validate(candidate) is True: break
        return candidate

    def create_header(self):
        return ['$'+d.name for d in self.decisions] + ['<$' + o.name for o in self.objectives]

    def validate(self, candidate):
        return True