from electronicItems import ElectronicItems

class Phone(ElectronicItems):
    def __init__(self,is_smartphone,phone_number,price,vat,warranty_years,charge_minutes):
        super().__init__(price,vat,warranty_years,charge_minutes)      
        self.is_smartphone = is_smartphone
        self.phone_number=phone_number

    def print_info(self):
        return super().print_info()+", is_smartphone: {}, phone_number; {}".format(self.is_smartphone,self.phone_number)

    def sms(self,msg,phone_num):
        return "From: {} sms: {}, TO: {}".format(self.phone_number, msg,phone_num)
