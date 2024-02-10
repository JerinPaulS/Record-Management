class father:

    def __init__(self, name, dob, country, membershipRecordNo, dateOfMarriage, placeOfMarriage):
        self.name = name
        self.dob = dob
        self.country = country
        self.membershipRecordNo = membershipRecordNo
        self.dateOfMarriage = dateOfMarriage
        self.placeOfMarriage = placeOfMarriage


    def setName(self, name):
        self.name = name
        
    def setDob(self, dob):    
        self.dob = dob

    def setDob(self, country):    
        self.country = country

    def setDob(self, membershipRecordNo):
        self.membershipRecordNo = membershipRecordNo

    def setDob(self, dateOfMarriage):
        self.dateOfMarriage = dateOfMarriage

    def setDob(self, placeOfMarriage):
        self.placeOfMarriage = placeOfMarriage

    def getName(self):
        return self.name
        
    def getDob(self):    
        return self.dob

    def getDob(self):    
        return self.country

    def getDob(self):
        return self.membershipRecordNo

    def getDob(self):
        return self.dateOfMarriage

    def getDob(self):
        return self.placeOfMarriage