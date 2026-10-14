from faker import Faker
import pandas as pd
import random 
from datetime import datetime


faker = Faker()    
doms = [ "@gmail.com",
        "@yahoo.com",
        "@outlook.com",
        "@hotmail.com",
        "@icloud.com",
        "@aol.com",
        "@protonmail.com",
        "@zoho.com",
        "@gmx.com",
        "@mail.com",
]

man = []
count = 0
while count < 100:
    man.append([faker.name(),
                faker.date_of_birth(minimum_age=18, maximum_age=65), 
                faker.email(), 
                faker.date_between_dates(date_start=datetime(2025,3,4), date_end= datetime(2026,8,6))
                ])
    count += 1


data = pd.DataFrame(man, columns=['Name',
                                  'Date of Birth', 
                                  'email', 
                                  'Date_visit'
                                  ])


data['Age'] = data['Date of Birth'].apply(lambda row: 2026 - int(row[:-6]))
data['domain'] = data['email'].apply(lambda row: str(row[-4:]))
data['email'] = data.apply(lambda row: row['Name'].replace(' ', '').lower() + random.choice(doms) + row['domain'], axis=1)
data['email'] = data['email'].apply(lambda x: x)

data.to_csv(r'C:\Users\acer\Documents\MEGA\Programming\ASPIRE\Python\python_basics_2026\pandas\__pycache__\medical_rec.csv', index= False) 
