class Algorithm:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_parameters(self):
        return self.parameters
