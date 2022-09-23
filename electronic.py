class ElectronicDevice:

    def __init__(self, device_name, device_model, device_price):
        self.name = device_name
        self.model = device_model
        self.price = device_price

    def print_details(self):
        return f", Device Name: {self.name}, Model: {self.model}, Price: {self.price}, "

    @staticmethod
    def company_name(co_name):
        return f" - Brought to you by {co_name}"


class PocketGadget(ElectronicDevice):
    use_for = "Use for listening music"
    charger = "Charger: 2 A"


class Phone(PocketGadget):

    @classmethod
    def change_charger(cls, new_charger):
        cls.charger = new_charger
    @classmethod
    def change_use(cls,new_use):
        cls.use_for = new_use


music = PocketGadget("Air Dots", 2020, 1000)
print(music.use_for, music.print_details(), music.charger, music.company_name("Realme"))

p1 = Phone("Galaxy S22 Ultra", 2022, 105000)
p1.change_use("Use for making phone calls")
p1.change_charger("Charger: 3 A")
print(p1.use_for, p1.print_details(), p1.charger, p1.company_name("Samsung"))

p2 = Phone("iphone 13", 2021, 150000)
p2.change_charger("Charger: No")
print(p2.use_for, p2.print_details(), p2.charger, p2.company_name("Apple"))
