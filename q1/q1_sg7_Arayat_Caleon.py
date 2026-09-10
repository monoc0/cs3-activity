from time import sleep

class Glassware:
    def __init__(self, id: str, size: int, shape: str, contents: set):
        self.id = id
        self.size = size
        self.shape = shape
        self.contents = contents

class Beaker(Glassware):
    def __init__(self, id: str, contents: set):
        super().__init__(id, 10, "Cylindrical", contents)
    def __str__(self):
        return f"{self.id}: {self.contents}"
    def add(self,content):
        self.contents.append(content)
        print(f"Beaker {self.id} had added {content}.")
    def drain(self, content):
        self.contents.remove(content)
        print(f"Beaker {self.id} is draining away {content}.")
    def __del__(self):
        for content in self.contents:
            self.drain(content)
        print(f"Drained contents of Beaker {self.id}, Beaker {self.id} Deleted.")

class Tray:
    def __init__(self, id: str):
        self.id = id
        self.beakers = [
            Beaker("aleph",["water","alcohol"]),
            Beaker("betha",["water","bleach"]),
            Beaker("century",["teaMix","water"]),
            Beaker("definition",["cookingOil","water"]),
            Beaker("mango",["dishwashing","cookingOil","water","alcohol"])
            ]
    def __str__(self):
        line = []
        for beaker in self.beakers:
            line.append(str(beaker))
        return f"{self.id}: "+", ".join(line)
    def selectiveAdd(self, content: str):
            for beaker in self.beakers:
                beaker.add(content)
            print(f"Filled beakers with {content}")
    def selectiveDrain(self, content: str):
        for beaker in self.beakers:
            beaker.drain(content)
        print(f"Drained beakers of {content}")
    def __del__(self):
        print("Deleting Beakers.")
        del self.beakers
        print(f"Beakers are deleted, deleted Tray {self.id}.")

tray1 = Tray("marion")
tray2 = Tray("arayat")
print("Created trays.")
sleep(2)
print(tray1)
print(tray2)
print("Printed tray contents.")
sleep(2)
tray1.selectiveDrain("water")
tray2.selectiveDrain("water")
print(tray1)
print(tray2)
print("Printed tray contents and drained water.")
sleep(2)
tray1.selectiveAdd("soda")
tray2.selectiveAdd("mercury")
print(tray1)
print(tray2)
print("Printed tray contents and added soda for T1 and mercury for T2.")
sleep(2)
del tray1
del tray2
print("All trays deleted. Ending program.")
sleep(3)