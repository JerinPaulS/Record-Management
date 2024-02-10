from repository.repository import repository
from model.family_model import family
from model.father_model import father
from model.mother_model import mother
from model.child_model import child
from difflib import SequenceMatcher

class family_record_template:

    def get_record(self, familyId):
        dbObject = repository()
        records = dbObject.get_family_record(familyId)
        record = self.parse_record(records, familyId)
        print(record)

    def parse_record(self, records, familyId):
        # 0individual_id, 1family_id, 2relationship, 3full_name, 4dob, 5gender, 6spouse_name, 7place_of_birth, 8date_of_baptism, 9place_of_baptism, 
        # 10date_of_confirmation, 11place_of_confirmation, 12date_of_wedding, 13membership_status
        family_record = None
        father_record = None
        mother_record = None
        spouse = None
        children = []
        for record in records:
            record_type = record[2]
            if record_type == "Head of family" and record[5] == "Male":
                father_record = father(record[3], record[4], record[8], record[1], record[12], "placeOfMarriage")
                spouse = record[6].split()[0]
            elif record_type == "Dependent" and (spouse in record[3] or SequenceMatcher(None, spouse, record[3]).ratio() >= 0.8):
                mother_record = mother(record[3], record[4], record[8], record[1], record[12], "placeOfMarriage")
            else:
                children.append(child(record[3], record[5], record[4], record[8], record[10], record[0], "", record[1]))
                
        record = family(familyId, father_record, mother_record, children)
        return record