import json

data_base_of_tables = {
    "Single table": {
        1: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        2: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        3: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        4: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        5: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
    },
    "Double table": {
        6: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        7: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        8: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        9: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        10: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
    },
    "Family table": {
        11: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        12: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        13: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        14: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
        15: {
            "Status": "availible",
            "Name": "",
            "Time": "",
        },
    },
}

with open("tables.json", "w") as file:
    json.dump(data_base_of_tables, file, indent=2)
