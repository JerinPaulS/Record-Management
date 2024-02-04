class individual:

    def __init__(self, individual_id, family_id, relationship, full_name, dob, gender, occupation, mobile_number, email, fathers_name, spouse_name,
        place_of_birth, date_of_baptism, place_of_baptism, date_of_confirmation, place_of_confirmation, date_of_wedding, details, membership_status):        
        self.individual_id = individual_id
        self.family_id = family_id
        self.relationship = relationship
        self.full_name = full_name
        self.dob = dob
        self.gender = gender
        self.occupation = occupation
        self.mobile_number = mobile_number
        self.email = email
        self.fathers_name = fathers_name
        self.spouse_name = spouse_name
        self.place_of_birth = place_of_birth
        self.date_of_baptism = date_of_baptism
        self.place_of_baptism = place_of_baptism
        self.date_of_confirmation = date_of_confirmation
        self.place_of_confirmation = place_of_confirmation
        self.date_of_wedding = date_of_wedding
        self.details = details
        self.membership_status = membership_status

    def get_individual_id(self):
        return str(self.individual_id)

    def set_individual_id(self, individual_id):
        self.individual_id = str(individual_id)

    def get_family_id(self):
        return str(self.family_id)
    
    def set_family_id(self, family_id):
        self.family_id = str(family_id)

    def get_relationship(self):
        return self.relationship
    
    def set_relationship(self, relationship):
        self.relationship = relationship

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_dob(self):
        return self.dob.strftime("%d-%m-%Y")
    
    def set_dob(self, dob):
        self.dob = dob.strftime("%d-%m-%Y")

    def get_gender(self):
        return self.gender
    
    def set_gender(self, gender):
        self.gender = gender

    def get_occupation(self):
        return self.occupation
    
    def set_occupation(self, occupation):
        self.occupation = occupation

    def get_mobile_number(self):
        return str(self.mobile_number)
    
    def set_mobile_number(self, mobile_number):
        self.mobile_number = str(mobile_number)

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_fathers_name(self):
        return self.fathers_name
    
    def set_fathers_name(self, fathers_name):
        self.fathers_name = fathers_name

    def get_spouse_name(self):
        return self.spouse_name
    
    def set_spouse_name(self, spouse_name):
        self.spouse_name = spouse_name
        
    def get_place_of_birth(self):
        return self.place_of_birth
    
    def set_place_of_birth(self, place_of_birth):
        self.place_of_birth = place_of_birth

    def get_date_of_baptism(self):
        return self.date_of_baptism.strftime("%d-%m-%Y")
    
    def set_date_of_baptism(self, date_of_baptism):
        self.date_of_baptism = date_of_baptism.strftime("%d-%m-%Y")
    
    def get_place_of_baptism(self):
        return self.place_of_baptism
    
    def set_place_of_baptism(self, place_of_baptism):
        self.place_of_baptism = place_of_baptism
    
    def get_date_of_confirmation(self):
        return self.date_of_confirmation.strftime("%d-%m-%Y")
    
    def set_date_of_confirmation(self, date_of_confirmation):
        self.date_of_confirmation = date_of_confirmation.strftime("%d-%m-%Y")
    
    def get_place_of_confirmation(self):
        return self.place_of_confirmation
    
    def set_place_of_confirmation(self, place_of_confirmation):
        self.place_of_confirmation = place_of_confirmation
        
    def get_date_of_wedding(self):
        return self.date_of_wedding.strftime("%d-%m-%Y")
    
    def set_date_of_wedding(self, date_of_wedding):
        self.date_of_wedding = date_of_wedding.strftime("%d-%m-%Y")

    def get_details(self):
        return self.details
    
    def set_details(self, details):
        self.details = details

    def get_membership_status(self):
        return self.membership_status
    
    def set_membership_status(self, membership_status):
        self.membership_status = membership_status