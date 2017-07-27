class Objective:
    """representation of an objective"""

    def __init__(self, name, minimize):
        """
        :param name: Name of the objective 
        :param minimize: If the objective needs to be minimized
        """
        self.name = name
        self.minimize = minimize
