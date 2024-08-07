import random
from dataclasses import dataclass, field
from typing import List
from scipy.stats import bernoulli

def age_range_options():
    return ["under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]

def gender_options():
    return ["Male", "Female", "Non-binary / third gender", "Prefer not to say"]

def experience_options():
    return ["Student", "Entry level professional (up to 5 years experience)", 
            "Mid-level professional (5-15 years experience)", "Senior professional (15+ years experience)"]

def AI_familiarity_options():
    return ["No familiarity", "Routine understanding of concepts behind artificial intelligence", 
            "Artificial intelligence policy expert", "Artificial intelligence technical expert", 
            "Artificial intelligence policy and technical expert"]

def China_military_familiarity_options():
    return ["No familiarity", "Routine understanding", "Policy expert", "Technical expert", 
            "Policy and technical expert"]

def US_military_familiarity_options():
    return ["No familiarity", "Routine understanding", "Policy expert", "Technical expert", 
            "Policy and technical expert"]

@dataclass
class Player:
    description: str = ""
    age_range: str = field(default_factory=lambda: random.choice(age_range_options()))
    gender: str = field(default_factory=lambda: random.choice(gender_options()))
    country_of_citizenship: str = "United States"
    government_affiliation: bool = field(default_factory=lambda: bernoulli.rvs(0.2))
    academic_affiliation: bool = field(default_factory=lambda: bernoulli.rvs(0.2))
    military_affiliation: bool = field(default_factory=lambda: bernoulli.rvs(0.2))
    private_industry_affiliation: bool = field(default_factory=lambda: bernoulli.rvs(0.2))
    non_governmental_organization_affiliation: bool = field(default_factory=lambda: bernoulli.rvs(0.2))
    other_affiliation: str = field(default_factory=lambda: "Other" if not any([
        bernoulli.rvs(0.2), bernoulli.rvs(0.2), bernoulli.rvs(0.2), bernoulli.rvs(0.2), bernoulli.rvs(0.2)
    ]) else "")
    experience: str = field(default_factory=lambda: random.choice(experience_options()))
    AI_familiarity: str = field(default_factory=lambda: random.choice(AI_familiarity_options()))
    China_military_familiarity: str = field(default_factory=lambda: random.choice(China_military_familiarity_options()))
    US_military_familiarity: str = field(default_factory=lambda: random.choice(US_military_familiarity_options()))

def changeXP_player(p: Player, new_XP: str) -> Player:
    return Player(
        description=p.description,
        age_range=p.age_range,
        gender=p.gender,
        country_of_citizenship=p.country_of_citizenship,
        government_affiliation=p.government_affiliation,
        academic_affiliation=p.academic_affiliation,
        military_affiliation=p.military_affiliation,
        private_industry_affiliation=p.private_industry_affiliation,
        non_governmental_organization_affiliation=p.non_governmental_organization_affiliation,
        other_affiliation=p.other_affiliation,
        experience=new_XP,
        AI_familiarity=p.AI_familiarity,
        China_military_familiarity=p.China_military_familiarity,
        US_military_familiarity=p.US_military_familiarity
    )

def player_description(p: Player) -> str:
    s = ""
    if p.description:
        s += f"Short Description: {p.description}\n"
    s += f"Age Range: {p.age_range}\n"
    s += f"Gender: {p.gender}\n"
    s += f"Country of Citizenship: {p.country_of_citizenship}\n"
    if p.government_affiliation:
        s += "Government Affiliation: Yes\n"
    if p.academic_affiliation:
        s += "Academic Affiliation: Yes\n"
    if p.military_affiliation:
        s += "Military Affiliation: Yes\n"
    if p.private_industry_affiliation:
        s += "Private Industry Affiliation: Yes\n"
    if p.non_governmental_organization_affiliation:
        s += "Non-Governmental Organization Affiliation: Yes\n"
    if p.other_affiliation:
        s += f"Other Affiliation: {p.other_affiliation}\n"
    s += f"Professional Experience: {p.experience}\n"
    s += f"AI Familiarity: {p.AI_familiarity}\n"
    s += f"China Military Familiarity: {p.China_military_familiarity}\n"
    s += f"US Military Familiarity: {p.US_military_familiarity}\n"
    return s

def team_description(team: List[Player]) -> str:
    s = f"The team consists of {len(team)} players. Each player answered an online questionnaire with the following information:\n\n"
    for i, p in enumerate(team):
        s += f"Player {i+1}: \n"
        s += player_description(p) + "\n"
    return s
