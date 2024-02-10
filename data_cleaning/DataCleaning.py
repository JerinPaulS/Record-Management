import pandas as pd
import numpy as np

class data_cleaning:

    def renameColumns(df):        

        df.rename(columns = {"S.No.":"individual_id", "family #":"family_id", "Head of family/ dependent":"relationship", "Full Name":"full_name", 
                                "Date of birth":"dob", "Gender":"gender", "Profession/ Occupation":"occupation", "Mobile #":"mobile_number", "Email ID":"email",
                                "Fathers name":"fathers_name", "Spouse name":"spouse_name", "Place of birth":"place_of_birth", "Date of baptism":"date_of_baptism", 
                                "Place of baptism":"place_of_baptism", "Date of confirmation":"date_of_conformation", "Place of confirmation":"place_of_confirmation", 
                                "Date of wedding":"date_of_wedding", "Date of reception":"date_of_reception", "BMC/ WMC congregation":"congregation", 
                                "Age group":"age_group", "Recommended Church Fellowship":"church_fellowship", "Recommended Area Fellowship":"area_fellowship", 
                                "Prescribed membership":"membership_type", "Date of PC Approval":"date_of_approval", "Membership form available":"membership_form_available", 
                                "Printed in book":"printed_in_book", "Residential Address":"family_address"}, inplace = True)
        
        pd.to_datetime(df["date_of_reception"], format='%Y-%m-%d')
        pd.to_datetime(df["dob"], format='%Y-%m-%d')
        # pd.to_datetime(df["date_of_approval"], format='%Y-%m-%d')
        pd.to_datetime(df["date_of_baptism"], format='%Y-%m-%d')
        pd.to_datetime(df["date_of_conformation"], format='%Y-%m-%d')
        pd.to_datetime(df["date_of_wedding"], format='%Y-%m-%d')

        df["date_of_reception"] = df["date_of_reception"].dt.strftime('%Y-%m-%d')
        df["dob"] = df["dob"].dt.strftime('%Y-%m-%d')
        # df["date_of_approval"] = df["date_of_approval"].dt.strftime('%Y-%m-%d')
        df["date_of_baptism"] = df["date_of_baptism"].dt.strftime('%Y-%m-%d')
        df["date_of_conformation"] = df["date_of_conformation"].dt.strftime('%Y-%m-%d')
        df["date_of_wedding"] = df["date_of_wedding"].dt.strftime('%Y-%m-%d')

        df['individual_id'] = df['individual_id'].astype("string")
        df['family_id'] = df['family_id'].astype("string")
        df['mobile_number'] = df['mobile_number'].astype("string")
        df['age_group'] = df['age_group'].astype("string")

        df = df.replace({np.nan: None})

        return df