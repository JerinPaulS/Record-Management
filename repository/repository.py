import psycopg2
import pandas as pd
import datetime as dt

class repository:
    
    def __init__(self):
        self.conn = None

    def innit_connection(self):
        try:
            self.conn = psycopg2.connect(host='localhost', database='BMC', user='postgres', password='root')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close_connection(self):
        try:
            if self.conn:
                self.conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create():
        pass

    def update():
        pass

    def delete():
        pass

    def update():
        pass

    def insertBulkRecords(self, table, records):
        tuples = [tuple(x) for x in records.to_numpy()]
        cols = ','.join(list(records.columns))
        
        cursor = self.conn.cursor()

        try:
            query  = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)" % (table, cols)
            cursor.executemany(query, tuples)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.rollback()
            cursor.close()
            return
        print("Persist of church details into db completed!")
        cursor.close()

    def insertIndividualRecords(self, record):
        # cols = ["S.No.", "family #", "Head of family/ dependent", "Full Name", "Date of birth", "Gender", "Profession/ Occupation", "Mobile #", "Email ID", "Fathers name", 
                # "Spouse name", "Place of birth", "Date of baptism", "Place of baptism", "Date of confirmation", "Place of confirmation", "Date of wedding"]
        
        cursor = self.conn.cursor()
        try:
            query  = "INSERT INTO individual_details(individual_id, family_id, relationship, full_name, dob, gender, occupation, mobile_number, email, fathers_name, spouse_name, place_of_birth, date_of_baptism, place_of_baptism, date_of_confirmation, place_of_confirmation, date_of_wedding, details, membership_status) VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format( 
                        record.individual_id, record.family_id, record.relationship, record.full_name, record.dob, record.gender, record.occupation, record.mobile_number, 
                        record.email, record.fathers_name, record.spouse_name, record.place_of_birth, record.date_of_baptism, record.place_of_baptism, 
                        record.date_of_confirmation, record.place_of_confirmation, record.date_of_wedding, record.details, record.membership_status)
            cursor.execute(query)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.rollback()
            cursor.close()
            return
        print("Persist of individual details into db completed!")
        cursor.close()

    def getQuestions(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT questions FROM questions')
            results = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            if cursor:
                cursor.close()
            print(error)
            return

        cursor.close()
        results = [str(item[0]) for item in results]
        return results
    
    def insertFamilyRecords(self, records):
        cursor = self.conn.cursor()
        try:
            for record in records:
                query  = "INSERT INTO family_details(family_id, family_head, family_address) VALUES(\'{}\',\'{}\',\'{}\')".format(record[0], record[1], record[2])
                cursor.execute(query)
                self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.rollback()
            cursor.close()
        print("Persist of family details into db completed!")
        cursor.close()

    def get_family_record(self, familyId):
        self.innit_connection()
        cursor = self.conn.cursor()
        results = None
        
        try:
            query  = "SELECT individual_id, family_id, relationship, full_name, dob, gender, spouse_name, place_of_birth, date_of_baptism, place_of_baptism, date_of_confirmation, place_of_confirmation, date_of_wedding, membership_status FROM individual_details WHERE family_id=\'{}\';".format(str(familyId))
            cursor.execute(query)
            results = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.rollback()
            cursor.close()
        
        print("Fetched family records for family ID{}!".format(familyId))        
        
        cursor.close()
        self.close_connection()
        return results