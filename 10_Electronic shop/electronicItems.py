
class ElectronicItems:
    def __init__(self,price,vat,warranty_years,charge_minutes):
        self.price=price
        self.vat=vat
        self.warranty_years=warranty_years
        self.charge_minutes=charge_minutes


    # price valid: 
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        if price >0:
            self.__price=price
        else:
            self.__price=0


    # vat valid:
    @property
    def vat(self):
        return self.__vat

    @vat.setter
    def vat(self,vat):
        if (vat%100)==0:
            self.__vat=vat
        else:
            self.__vat=0

    # warranty_years valid:
    @property
    def warranty_years(self):
        return self.__warranty_years

    @warranty_years.setter
    def warranty_years(self,warranty_years):
        if warranty_years>0 and warranty_years<10:
            self.__warranty_years=warranty_years
        else:
            self.__warranty_years=0


    # warranty_years valid:
    @property
    def charge_minutes(self):
        return self.__charge_minutes

    @charge_minutes.setter
    def charge_minutes(self,charge_minutes):
        if charge_minutes>0:
            self.__charge_minutes=charge_minutes
        else:
            self.__charge_minutess=0

    # methods:
    def end_of_charge(self):
        print("Minutes of charge: ",self.charge_minutes)

    def print_info(self):
        return "price: {}, vat: {},warranty_years: {} ,charge_minutes: {}".format(self.price,self.vat,self.warranty_years,self.charge_minutes)