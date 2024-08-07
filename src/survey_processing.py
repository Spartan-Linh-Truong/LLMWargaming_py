import csv
import os
import warnings
from players import Player, age_range_options, gender_options, experience_options, AI_familiarity_options, China_military_familiarity_options, US_military_familiarity_options
import pickle

# Import player survey data
survey_file = "wargame/Survey_October24.csv"

def read_survey(file_path):
    with open(file_path, newline='') as csvfile:
        survey = list(csv.DictReader(csvfile))
    return survey

survey = read_survey(survey_file)
c_names = survey[0].keys()

# Helper function
def check_attribute(input_value, options, label="att"):
    attribute = ""
    for att in options:
        # This links the description in players.py and survey answers for age
        if label == "age":
            att = f"{att} years old"
        if input_value == att:
            attribute = att
    if attribute == "":
        warnings.warn(f"Unknown {label} for row: {input_value}")

    return attribute

def create_player_data():
    # List of player data to fill
    player_data = []
    # Iterate over each player's information
    for row in survey[2:]:
        # Safety check for "Finished" category
        if row["Finished"] != "TRUE":
            print(f"Unfinished row: {row['Finished']}")
            continue

        # Get age
        age_range = check_attribute(row["Q2"], age_range_options(), "age")

        # Get gender
        gender = check_attribute(row["Q4"], gender_options(), "gender")

        # Get experience
        experience = check_attribute(row["Q24"], experience_options(), "XP")

        # Get AI familiarity
        AI_familiarity = check_attribute(row["Q15"], AI_familiarity_options(), "aifam")

        # Get China familiarity
        China_military_familiarity = check_attribute(row["Q16"], China_military_familiarity_options(), "chinafam")

        # Get US military familiarity
        US_military_familiarity = check_attribute(row["Q17"], US_military_familiarity_options(), "usfam")

        # Get professional background (one-hot encoding)
        given_back = row["Q23"].split(",")
        affil = 0
        government_affiliation = "Government" in given_back
        affil += int(government_affiliation)
        academic_affiliation = "Academic" in given_back
        affil += int(academic_affiliation)
        military_affiliation = "Military" in given_back
        affil += int(military_affiliation)
        private_industry_affiliation = "Private Industry" in given_back
        affil += int(private_industry_affiliation)
        non_governmental_organization_affiliation = "Non-Governmental Organization" in given_back
        affil += int(non_governmental_organization_affiliation)
        other_affiliation = "Other" if "Other" in given_back and affil <= 0 else ""
        if affil <= 0:
            print(f"UNKNOWN BACK {row}: {row['Q23']}")
            continue

        new_player = Player(
            age_range=age_range,
            gender=gender,
            government_affiliation=government_affiliation,
            academic_affiliation=academic_affiliation,
            military_affiliation=military_affiliation,
            private_industry_affiliation=private_industry_affiliation,
            non_governmental_organization_affiliation=non_governmental_organization_affiliation,
            other_affiliation=other_affiliation,
            experience=experience,
            AI_familiarity=AI_familiarity,
            China_military_familiarity=China_military_familiarity,
            US_military_familiarity=US_military_familiarity
        )
        player_data.append(new_player)

    return player_data

player_data = create_player_data()

# Serialize player data
with open("wargame/player_data.pkl", "wb") as f:
    pickle.dump(player_data, f)

# Deserialize player data
# with open("wargame/player_data.pkl", "rb") as f:
#     loaded_player_data = pickle.load(f)

# Randomly select a player from loaded data
# import random
# print(random.choice(loaded_player_data))
