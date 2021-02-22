import phonenumbers

#Enter the number for which you want to work on here below
number = "+91XXXXXXXX"

#from text import number

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

