import phonenumbers
from phonenumbers import timezone,geocoder,carrier

phno = input(" Enter your number with +__ : ")
phone = phonenumbers.parse(phno) # it will give details about number (The .parse() function in the phonenumbers module in Python is used to parse a phone number from a string representation. It can intelligently interpret and parse the phone number, whether it is entered with or without the country code, with or without dashes or spaces. The parsed phone number object contains valuable information such as the country code, national number, extension, and more.)

time = timezone.time_zones_for_number(phone) #it will give number
cr = carrier.name_for_number(phone,"en" )# carrier find krne ke liye in en- english
reg = geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(cr)
print(reg)
