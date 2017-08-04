import pandas as pd
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta


class Athletes:

    rio_date = date(2016, 8, 5)

    def load(self, csv):
        with open(csv, 'r') as f:
            dataframe = pd.read_csv(f, parse_dates=[4])
        return dataframe

    def gymnasts(self):
        gymnasts = self.data[self.data["sport"] == "gymnastics"]
        return gymnasts

    def __init__(self, csv):
        self.data = self.load(csv)
        self.gymnasts = self.gymnasts()
        self.data["age"] = self.rio_date - self.data["date_of_birth"]
    
    def age(self):
        for dob in self.data["date_of_birth"]:
            if not pd.isnull(dob):
                age = relativedelta(self.rio_date, dob)
                yield age
            else:
                yield None
        
      

    
if __name__ == "__main__":
    athletes = Athletes('athletes.csv')
