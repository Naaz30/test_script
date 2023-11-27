import random
import pandas as pd
import json

def generate_random_data(n):
    # Column names
    column_names = [
        "EmployeeID",
        "Name",
        "Salary",
        "DepartmentID",
        "DepartmentName",
        "Location"
    ]

    # Possible values for each column
    names  = list(pd.read_csv("Names.csv")['Name'])
    salaries = [str(random.randint(90000, 300000)) for _ in range(n)]
    department_df = pd.read_json("department_table.json" , orient='records')

    # Generate random data points
    data_points = []
    for _ in range(n):
        random_row = department_df.sample()
        data_point = [
            str(_),
            random.choice(names),
            random.choice(salaries),
            random_row['DepartmentID'].values[0],
            random_row['DepartmentName'].values[0],
            random_row['Location'].values[0]
        ]
        data_points.append(data_point)

    data_json = [dict(zip(column_names, row)) for row in data_points]

    return data_json


# Decide no of samples
NO_OF_SAMPLES = 1000

data_json = generate_random_data(NO_OF_SAMPLES)

with open("output.json", "w") as json_file:
    json.dump(data_json, json_file, indent=2)