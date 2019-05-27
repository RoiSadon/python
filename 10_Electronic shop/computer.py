from electronicItems import ElectronicItems

class Computer(ElectronicItems):
    def __init__(self,is_portable,price,vat,warranty_years,charge_minutes):
        super().__init__(price,vat,warranty_years,charge_minutes)      
        self.is_portable = is_portable

    def print_info(self):
        return super().print_info()+" is_portable: {}".format(self.is_portable)