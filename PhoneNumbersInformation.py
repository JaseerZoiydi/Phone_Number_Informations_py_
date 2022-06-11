#libraries
import phonenumbers

#Function_Location_Number
def location_number(number) :
    from phonenumbers import geocoder
    ch_nb = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_nb, "en"))

#Function_Carrier_Number
def carrier_number(number) :
    from phonenumbers import carrier
    service_number = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_number, "en"))

#Number_Information
numbers = open('numbers.txt','r')
number = numbers.readline()
location_number(number)
carrier_number(number)
while (numbers != "") :
    number = numbers.readline()
    location_number(number)
    carrier_number(number)
numbers.close()
