# %%
import pandas as pd
import string


sf_sal = pd.read_csv('Salaries.csv')

alphabet = string.ascii_uppercase
alphabet

index_list = []

for first in alphabet:
    for second in alphabet:
            index_list.append(first + second)

sf_sal["Id"] = index_list
sf_sal.set_index("Id", inplace=True)

sf_sal.head()

# %% Min Pay
sf_sal.loc["ZZ"]
#sf_sal['TotalPayBenefits'].idxmin()


# %% Info
 
# single bracket returns Series, with name/length/dtype info
# bear in mind these can be obtained explicitly with methods

#sf_sal["BasePay"]

# double bracket returns DataFrame

#sf_sal[["BasePay"]]


# %% Police

# define function to find 'police' first

def find_police(x):
    return "POLICE" in x


# use apply to search for it in JobTitle
# sf_sal["isPolice"] = sf_sal["JobTitle"].apply(find_police)

sf_sal["isPolice"] = sf_sal["JobTitle"].apply(lambda x : 'POLICE' in x)
# sf_sal.head()
# sum
# sf_sal["isPolice"].sum()


# %% Max Pay
#sf_sal[sf_sal["BasePay"] == max(sf_sal["BasePay"])]

sf_sal["BasePay"].max()


# %% Albert Pardini
#sf_sal[sf_sal["EmployeeName"] == "ALBERT PARDINI"][["EmployeeName", "TotalPayBenefits", "JobTitle", "BasePay"]]

sf_sal.loc["AC"][["JobTitle", "TotalPayBenefits", "BasePay", "EmployeeName"]]


# %% Fire to Police Ratio

#sf_sal[sf_sal["JobTitle"].apply(lambda x : "POLICE" in x)]  / sf_sal[sf_sal["JobTitle"].apply(lambda x : "FIRE" in x)] 

sf_sal["isPolice"] = sf_sal["JobTitle"].apply(lambda x : 'POLICE' in x)
sf_sal["isFire"] = sf_sal["JobTitle"].apply(lambda x : 'FIRE' in x)

sf_sal["isFire"].sum() / sf_sal["isPolice"].sum()

#sf_sal["FIRE" in sf_sal["JobTitle"]]


# %% Unique Jobs

#sf_sal["JobTitle"].unique()

#sf_sal.groupby("JobTitle").nunique().sum(axis=1)
len(sf_sal.groupby("JobTitle").nunique())

# %% John

sf_sal["John"] = sf_sal["EmployeeName"].apply(lambda x : 'JOHN' in x)
sf_sal["John"].sum()


# %% Surname, Name > 6

sf_sal["Surname"] = sf_sal["EmployeeName"].apply(lambda x: x.split()[1] if len(x.split()[0]) > 6 else " ")

sf_sal["Surname"].to_list()


# %% last_updated
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)

sf_sal["last_updated"] = current_time
sf_sal.head()


# %% Overtime Pay / Base Pay

sf_sal["Pay"] = sf_sal["OvertimePay"] / sf_sal["BasePay"]
sf_sal.head()


# %% 100k Salaries

sf_sal[sf_sal["BasePay"] > 100000][["EmployeeName", "TotalPay", "JobTitle"]]


# %% Pay minus Base (100k Salaries)

sf_sal["PayMinusBase"] = sf_sal["TotalPayBenefits"] - sf_sal["BasePay"]

sf_sal[sf_sal["BasePay"] > 100000][["EmployeeName", "TotalPay", "JobTitle", "PayMinusBase"]]


# %%
import numpy as np


new_employee = {
    "EmployeeName": "BROKE BETTY",
    "JobTitle": "CAPTAIN",
    "BasePay": 1,
    "OvertimePay": 0,
    "OtherPay": 100000,
    "Benefits": np.nan,
    "TotalPay": 100001,
    "TotalPayBenefits": 100001,
    "Year": 2011,
    "Notes": np.nan,
    "Agency": "San Francisco",
    "Status": np.nan
}

sf_sal.append(new_employee, ignore_index=True)
# %% Yaml

from yaml import load, SafeLoader


def yaml_to_df(yaml_file):
    with open(yaml_file) as yf:
        yf_contents = load(yf, Loader=SafeLoader)
    yaml_df = pd.json_normalize(yf_contents)
    return yaml_df

from os import getcwd, path 

yaml_file = path.join(getcwd(), "/Users/dan/documents/projects/recipe-app-api", "docker-compose.yml")
yaml_to_df(yaml_file) 