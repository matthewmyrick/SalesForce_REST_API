from simple_salesforce import Salesforce, SFType, SalesforceLogin
import pandas as pd
import random
import datetime
import json
from faker import Faker
import names

fake = Faker()

today = datetime.datetime.now()

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

USERNAME = "andzelika19adelmann@gmail.com"
PASSWORD = "Adelmann1"
TOKEN = "BZtiiMplSJPYEjLJIN58FzKq"
DOMAIN = 'login'

sessionID, instance = SalesforceLogin(
    username=USERNAME,
    password=PASSWORD,
    security_token=TOKEN,
    domain=DOMAIN
)
sf = Salesforce(instance=instance, session_id=sessionID)

# sf = Salesforce(
#     username=USERNAME,
#     password=PASSWORD,
#     security_token=TOKEN
# )

# MEMBER__c = SFType('MEMBER__c', sessionID, instance)
#
# today = datetime.datetime.now()
# data = {
#     'Address__c': "869 buchser way",
#     'City__c': "San Jose",
#     'FirstName__c': 'Matthew',
#     'LastName__c': 'Myrick',
#     'State__c': 'CA',
#     'RegistrationDate__c': (today + datetime.timedelta(days=45)).isoformat() + 'Z',
#     'Zip__c': '95125'
# }
#
# response = MEMBER__c.create(data)
# print(type(response.get('id')))
# a045Y00000mQxDVQA0

#

# SP__c = SFType('EMPLOYEE__c', sessionID, instance)
# SALE__c = SFType('SALE__c', sessionID, instance)
# PRODUCT__c = SFType('PRODUCT__c', sessionID, instance)
#
# saleID = SALE__c.get('Id')
# print(saleID)
#
# productID = PRODUCT__c.get('Id')
# print(productID)

'''
get student id
'''
# querySOQL = "SELECT Id, Name, FirstName__c, LastName__c FROM Student__c"
# response = sf.query(querySOQL)
# sf_data = response.get('records')
#
# sf_df = pd.DataFrame(sf_data)
# print(sf_df)
# urls = sf_df['attributes'].tolist()
# ids = sf_df['Name'].tolist()
# realIDs = sf_df['Id'].tolist()
# firstName = sf_df['FirstName__c'].tolist()
# lastName = sf_df['LastName__c'].tolist()
# randNum = random.randint(0, len(urls)-1)
# url = str(urls[randNum]['url'])
# id = str(ids[randNum])
# realID = str(realIDs[randNum])
# firstName = str(firstName[randNum])
# lastName = str(lastName[randNum])
#
# print(firstName, lastName, realID)

'''
get staff id
'''
# querySOQL = "SELECT Id, Name FROM Staff__c"
# response_event = sf.query(querySOQL)
# sf_data_event = response_event.get('records')
#
# sf_df_s = pd.DataFrame(sf_data_event)
# print(sf_df_s)
# urls = sf_df_s['attributes'].tolist()
# ids = sf_df_s['Name'].tolist()
# realIDs = sf_df_s['Id'].tolist()
# randNumStaff = random.randint(0, len(urls) - 1)
# urlEvent = str(urls[randNumStaff]['url'])
# idEvent = str(ids[randNumStaff])
# realID = str(realIDs[randNumStaff])
# print(realID)

'''
add donors
'''
companyNames = []
file = open("companyNames.txt", "r")
for line in file:
    values = line.splitlines()
    companyNames.append(values[0])
file.close()
Donor__c = SFType('Donor__c', sessionID, instance)
for i in range(500):

    # randNum = random.randint(0, len(urls) - 1)
    # url = str(urls[randNum]['url'])
    # id = str(ids[randNum])
    # realID = str(realIDs[randNum])

    randDay = random.randint(6570, 8395)
    data = {
        'Address__c': str(fake.address().splitlines()[0]),
        'City__c': str(fake.city()),
        'Company__c': companyNames[i],
        'Email__c': str(names.get_first_name()) + str(names.get_last_name()) + "@gmail.com",
        'FirstName__c': str(names.get_first_name()),
        'LastName__c': str(names.get_last_name()),
        'Phone__c': str(random.randint(1000000000, 9999999999)),
        'State__c': states[random.randint(0, 50)],
        'Zip__c': str(random.randint(43298, 99999))
    }
    Donor__c.create(data)
    print("Donor Added.")
print("Finished")

'''
add d_event 
'''
# events = []
# file = open("events.txt", "r")
# for line in file:
#     values = line.splitlines()
#     events.append(values[0])
# file.close()
# print(events)
# descriptions = ['Food', 'Fruits', 'Clothes', 'Plants', 'Movie', 'Music']
#
# for _ in range(50):
#     descNum = random.randint(0, len(descriptions) - 1)
#     eventNum = random.randint(0, len(events) - 1)
#     randDay = random.randint(50, 500)
#     data = {
#         'Date__c': (today + datetime.timedelta(days=randDay)).isoformat() + 'Z',
#         'Description__c': descriptions[descNum],
#         'EventName__c': events[eventNum],
#         'Location__c': str(fake.city()),
#         'Staff__c': realID
#     }
#     D_Event__c = SFType('D_Event__c', sessionID, instance)
#     D_Event__c.create(data)
#     print("event added")
# print("finished")

'''
add staff
'''
# Staff__c = SFType('Staff__c', sessionID, instance)
# for _ in range(60):
#
#     # randNum = random.randint(0, len(urls) - 1)
#     # url = str(urls[randNum]['url'])
#     # id = str(ids[randNum])
#     # realID = str(realIDs[randNum])
#
#     randDay = random.randint(6570, 8395)
#     data = {
#         'Address__c': str(fake.address().splitlines()[0]),
#         'City__c': str(fake.city()),
#         'Email__c': str(names.get_first_name()) + str(names.get_last_name()) + "@gmail.com",
#         'FirstName__c': str(names.get_first_name()),
#         'LastName__c': str(names.get_last_name()),
#         'Phone__c': str(random.randint(1000000000, 9999999999)),
#         'States__c': states[random.randint(0, 50)],
#         'Zip__c': str(random.randint(43298, 99999))
#     }
#     Staff__c.create(data)
#     print("Staff Added.")
# print("Finished")


'''
add volunteers
'''
# Volunteer__c = SFType('Volunteer__c', sessionID, instance)
# for _ in range(75):
#
#     # randNum = random.randint(0, len(urls) - 1)
#     # url = str(urls[randNum]['url'])
#     # id = str(ids[randNum])
#     # realID = str(realIDs[randNum])
#
#     randDay = random.randint(6570, 8395)
#     data = {
#         'Address__c': str(fake.address().splitlines()[0]),
#         'City__c': str(fake.city()),
#         'Email__c': str(names.get_first_name()) + str(names.get_last_name()) + "@gmail.com",
#         'FirstName__c': str(names.get_first_name()),
#         'LastName__c': str(names.get_last_name()),
#         'PhoneNumber__c': str(random.randint(1000000000, 9999999999)),
#         'State__c': states[random.randint(0, 50)],
#         'Zip__c': str(random.randint(43298, 99999))
#     }
#     Volunteer__c.create(data)
#     print("Volunteer Added.")
# print("Finished")


'''
add events
'''
# for eventNum in range(35):
#     randDay = random.randint(50, 500)
#     standings = ["Senior", "Junior", "Sophmore", "Freshman", "Graduate Student"]
#     standingNum = random.randint(0, len(standings)-1)
#     descriptions = ["cooking", "bakery"]
#     descNum = random.randint(0, len(descriptions)-1)
#     locations = [
#         "Ball room",
#         "DS Tower",
#         "Rec Center",
#         "Cafeteria",
#         "Gymnasium",
#         "Grass Quad",
#         "Restaurant/Bar",
#         "Garden Area"
#     ]
#     locNum = random.randint(0, len(locations)-1)
#     data = {
#         "Class_Standing__c": standings[standingNum],
#         "Date__c": (today + datetime.timedelta(days=randDay)).isoformat() + 'Z',
#         "Description__c": descriptions[descNum],
#         "Location__c": locations[locNum],
#         "Name_of_Event__c": "FoodRight Event" + str(eventNum)
#     }
#     Educational_Event__c = SFType('Educational_Event__c', sessionID, instance)
#     Educational_Event__c.create(data)
#     print("Event created")
# print("Finished.")


'''
add surveys
'''
# for _ in range(50):
#     randNum = random.randint(0, len(urls) - 1)
#     realID = str(realIDs[randNum])
#     randDay = random.randint(0, 365)
#     cabbage = str(random.randint(0, 10))
#     chickPeas = str(random.randint(0, 10))
#     cookingFreq = str(random.randint(0, 10))
#     greenOnion = str(random.randint(0, 10))
#     parsely = str(random.randint(0, 10))
#     parsleyConfidence = str(random.randint(0, 10))
#     popcorn = str(random.randint(0, 10))
#     recipeConfidence = str(random.randint(0, 10))
#     salesSummary = str(random.randint(0, 10))
#     tofu = str(random.randint(0, 10))
#     whiteBeans = str(random.randint(0, 10))
#     zucchini = str(random.randint(0, 10))
#
#     data = {
#         "Student_ID__c": realID,
#         # "Student_FirstName__c": firstName,
#         # "Student_LastName__c": lastName,
#         "Date__c": (today - datetime.timedelta(days=randDay)).isoformat() + 'Z',
#         "Cabbage__c": cabbage,
#         "ChickPeas__c": chickPeas,
#         "CookingFrequency__c": cookingFreq,
#         "GreenOnions__c": greenOnion,
#         "Parsley__c": parsely,
#         "ParsleyConfidence__c": parsleyConfidence,
#         "Popcorn__c": popcorn,
#         "RecipeConfidence__c": recipeConfidence,
#         "Sales_Summary__c": salesSummary,
#         "Tofu__c": tofu,
#         "White_Beans__c": whiteBeans,
#         "Zucchini__c": zucchini
#     }
#     Survey__c = SFType('Survey__c', sessionID, instance)
#     Survey__c.create(data)
#     print("Added record.")
# print("finished with success")


'''
add students
'''
# Student__c = SFType('Student__c', sessionID, instance)
# for _ in range(150):
#
#     randNum = random.randint(0, len(urls) - 1)
#     url = str(urls[randNum]['url'])
#     id = str(ids[randNum])
#     realID = str(realIDs[randNum])
#
#     randDay = random.randint(6570, 8395)
#     data = {
#         'Address__c': str(fake.address().splitlines()[0]),
#         'City__c': str(fake.city()),
#         'Date_of_Birth__c': (today - datetime.timedelta(days=randDay)).isoformat() + 'Z',
#         'FirstName__c': str(names.get_first_name()),
#         'LastName__c': str(names.get_last_name()),
#         'Phone__c': str(random.randint(1000000000, 9999999999)),
#         'School_ID__c': realID,
#         'States__c': states[random.randint(0, 50)],
#         'Zip__c': str(random.randint(43298, 99999))
#     }
#     Student__c.create(data)
#     print("Record Added.")
'''
added schools
'''
# School__c = SFType('School__c', sessionID, instance)
# with open('schoolNames.json') as f:
#     data = json.load(f)
# for dataDict in data:
#     School__c.create(dataDict)
# data = {
#     'Address__c': "869 buchser way",
#     'City__c': "San Jose",
#     'Name__c': 'Marquette',
#     'Phone_Number__c': "(217) 333-1000",
#     'States__c': 'CA',
#     'Zip__c': '95125',
#     'Email__c': 'Marquette@gmail.com'
# }
# School__c.create(data)


# prodIds = sf_df['Id'].tolist()
# randNum = random.randint(0, len(prodIds))
# productID = prodIds[randNum]
# print(productID)
#
# querySOQL = "SELECT Id, Name FROM PRODUCT__c"
# response = sf.query(querySOQL)
# sf_data = response.get('records')
#
# sf_df = pd.DataFrame(sf_data).drop(columns='attributes')
# prodIds = sf_df['Id'].tolist()
# randNum = random.randint(0, len(prodIds))
# saleID = prodIds[randNum]
# print(saleID)


# data = {
#     'Address__c': "869 buchser way",
#     'City__c': "San Jose",
#     'FirstName__c': 'Matthew',
#     'LastName__c': 'Myrick',
#     'PhoneNum__c': "4083905085",
#     'State__c': 'CA',
#     'Zip__c': '95125'
# }
# sf.EMPLOYEE.upsert()


# querySOQL = "SELECT Id, Name FROM PRODUCT__c"
# response = sf.query(querySOQL)
# sf_data = response.get('records')
#
# sf_df = pd.DataFrame(sf_data).drop(columns='attributes')
# prodIds = sf_df['Id'].tolist()
# randNum = random.randint(0, len(prodIds))
# saleID = prodIds[randNum]
# print(saleID)


# sf.MEMBER.update(data)
