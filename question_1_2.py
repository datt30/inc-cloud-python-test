class Instrument:
    def __init__(self, name, brand, model):
        self.name = name
        self.brand = brand
        self.model = model

    @classmethod
    def description(cls):
        pass

    def get_specification(self):
        pass

class Piano(Instrument):
    def __init__(self, name, brand, model, number_of_keys):
        super().__init__(name, brand, model)
        self.number_of_keys = number_of_keys

    @classmethod
    def description(cls):
        return "Piano is a funny stringed percussion instrument"

    def get_specification(self):
        return f"{self.name} which has {self.number_of_keys} keys, is available in {self.model} model"


base_instrument = Instrument("Guitar", "Fender", "2007")
piano = Piano("Grand Piano", "Casio", "2020", 88)

print(piano.description())
print(piano.get_specification())
