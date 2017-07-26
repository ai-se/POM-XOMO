class Decision:
    """ Representation of a decision """

    def __init__(self, name, low, up):
        """
        :param name: Name of the decision 
        :param low: Lower bound of the decision
        :param up: Upper bound of the decision
        """
        self.name = name
        self.low = low
        self.up = up
