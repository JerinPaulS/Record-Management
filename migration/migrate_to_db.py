import pandas as pd
from repository import repository
from model.individual import individual
import json
import numpy as np
from DataCleaning import data_cleaning

class migrate_to_db:

    def __init__(self):
        self.family_record = []
        
    def read_csv(self):
        df = pd.read_excel('Data/Membership details.xlsx')
        return df
    
    def persistToDb(self):
        df = self.read_csv()

        df.replace(np.nan, None, inplace=True)
        df = data_cleaning.renameColumns(df)
        
        dbObject = repository()
        dbObject.innit_connection()
        questions = dbObject.getQuestions()

        church_record_cols = ["family_id", "individual_id", "date_of_reception", "congregation", "age_group", "church_fellowship", 
                              "area_fellowship", "membership_type", "date_of_approval", "membership_form_available", "printed_in_book"]
        church_records = df[church_record_cols]
        df.replace("'", "''", inplace=False)
        dbObject.insertBulkRecords("church_records", church_records)

        for index, row in df.iterrows():
            individual_record = self.parseRow(row, questions)
            dbObject.insertIndividualRecords(individual_record)

        dbObject.insertFamilyRecords(self.family_record)
        self.family_record = None

        dbObject.close_connection()

    def parseRow(self, row, questions):
        details = {}

        for question in questions:
            details[question] = row[question]

        questionJsonObject = json.dumps(details)

        if row["place_of_baptism"]:
            row["place_of_baptism"] = str(row["place_of_baptism"]).replace("'", "''")
        if row["place_of_confirmation"]:
            row["place_of_confirmation"] = str(row["place_of_confirmation"]).replace("'", "''")

        individual_id = "\'{}\'".format(row["individual_id"]) if row["individual_id"] != None else "NULL"
        family_id = "\'{}\'".format(row["family_id"]) if row["family_id"] != None else "NULL"
        relationship = "\'{}\'".format(row["relationship"]) if row["relationship"] != None else "NULL"
        full_name = "\'{}\'".format(row["full_name"]) if row["full_name"] != None else "NULL"
        dob = "\'{}\'".format(row["dob"]) if row["dob"] != None else "NULL"
        gender = "\'{}\'".format(row["gender"]) if row["gender"] != None else "NULL"
        occupation = "\'{}\'".format(row["occupation"]) if row["occupation"] != None else "NULL"
        mobile_number = "\'{}\'".format(row["mobile_number"]) if row["mobile_number"] != None else "NULL"
        email = "\'{}\'".format(row["email"]) if row["email"] != None else "NULL"
        fathers_name = "\'{}\'".format(row["fathers_name"]) if row["fathers_name"] != None else "NULL"
        spouse_name = "\'{}\'".format(row["spouse_name"]) if row["spouse_name"] != None else "NULL"
        place_of_birth = "\'{}\'".format(row["place_of_birth"]) if row["place_of_birth"] != None else "NULL"
        date_of_baptism = "\'{}\'".format(row["date_of_baptism"]) if row["date_of_baptism"] != None else "NULL"
        place_of_baptism = "\'{}\'".format(row["place_of_baptism"]) if row["place_of_baptism"] != None else "NULL"
        date_of_confirmation = "\'{}\'".format(row["date_of_conformation"]) if row["date_of_conformation"] != None else "NULL"
        place_of_confirmation = "\'{}\'".format(row["place_of_confirmation"]) if row["place_of_confirmation"] != None else "NULL"
        date_of_wedding = "\'{}\'".format(row["date_of_wedding"]) if row["date_of_wedding"] != None else "NULL"
        details = "\'{}\'".format(questionJsonObject) if questionJsonObject != None else "NULL"
        membership_status = "\'{}\'".format("test")

        details = details.replace("God's", "God''s")

        individualRecord = individual(individual_id, family_id, relationship, full_name, dob, gender, occupation, mobile_number, email, fathers_name, spouse_name, 
                                      place_of_birth, date_of_baptism, place_of_baptism, date_of_confirmation, place_of_confirmation, date_of_wedding,
                                      details, membership_status)

        if row["relationship"] == "Head of family":
            self.family_record.append([row["family_id"], row["full_name"], row["family_address"]])

        return individualRecord 
    