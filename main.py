import names
import csv
import random
import pandas as pd
from faker import Faker
import datetime

fake = Faker()

# staff data
staffData = {
    "firstNames__c": [],
    "lastNames__c": [],
    "phoneNumber__c": [],
    "address__c": [],
    "city__c": [],
    "state__c": []
}

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

for i in range(150):
    data = {
        'Address__c': str(fake.address().splitlines()),
        'City__c': str(fake.city()),
        'Date_of_Birth__c': ''
    }
    try:
        # add first name
        firstName = names.get_first_name()
        staffData["firstNames__c"].append(firstName)
    except IndexError:
        pass
    try:
        # add last name
        lastName = names.get_last_name()
        staffData["lastNames__c"].append(lastName)
    except IndexError:
        pass
    try:
        # add phone numbers
        phoneNum = str(random.randint(1000000000, 9999999999))
        staffData["phoneNumber__c"].append(phoneNum)
    except IndexError:
        pass
    try:
        # add address
        address = fake.address().splitlines()
        staffData["address__c"].append(address[0])
        # add city
        city = fake.city()
        staffData["city__c"].append(city)
        # add state
        state = states[random.randint(0, 50)]
        staffData["state__c"].append(state)
    except IndexError:
        pass
print(staffData)
df = pd.DataFrame(data=staffData)
print(df)
for i in df:
    print(i)
# df.to_csv(
#     r'C:\Users\matth\OneDrive\Documents\Marquette University\2021 Spring\Database Management Systems\Assingments\Final Project\staff_data.csv',
#     index=False
# )

donationID = {
    "donationID": [],
    "donorID": [],
    "staffID": [],
    "date": [],
    "amount": []
}
