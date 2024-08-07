from dataclasses import dataclass, field
from typing import List
import pandas as pd
import os

@dataclass
class SimulationConfig:
    model: str = "gpt-3.5-turbo-16k"
    secret_key: str = os.environ.get("OPENAI_API_KEY")
    wargame_dir: str = "wargame/"
    output_dir: str = "results/"
    out_csv_file: str = ""
    use_dummygpt: bool = False
    use_bench_players: bool = False
    no_dialog: bool = False 
    no_chiefs: bool = False 
    boostrap_players: bool = True
    pacificsm: bool = False
    sociopaths: bool = False
    more_disagreement: bool = False
    verbose: bool = False
    save_results_to_csv: bool = True
    run_test_game: bool = False
    n_teams: int = 10
    n_players: int = 6
    n_dialog_steps: int = 3

def init_sim_conf(**kwargs):
    # Create a default instance
    default_conf = SimulationConfig()

    # Convert the default instance to a dict
    default_conf_dict = default_conf.__dict__

    # Merge the default values with the provided keyword arguments
    merged_kwargs = {**default_conf_dict, **kwargs}

    # Create a new SimulationConfig instance with the merged keyword arguments
    return SimulationConfig(**merged_kwargs)

# remove secret_key from logging and output data
def get_pars4store(fil_fields=["secret_key"]):
    fields = SimulationConfig.__dataclass_fields__.keys()
    store_fields = [f for f in fields if f not in fil_fields]
    store_names = [f for f in store_fields]

    assert len(store_fields) == len(store_names), f"Length mismatch for stored fields {len(store_fields)}, {len(store_names)}"

    return store_fields, store_names

def results_df(cnf: SimulationConfig):
    columns = get_pars4store()[1] + [
        "AI Accuracy", "AI System Training", "China Status",
        "Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6"
    ] + [f"Dialogue 1-{i}" for i in range(1, cnf.n_dialog_steps + 1)] + [
        "Move 1 Question 1", "Move 1 Question 2"
    ] + move_1_2_options_desc() + [
        "Move 1 to Move 2 Transition Response"
    ] + [f"Dialogue 2-{i}" for i in range(1, cnf.n_dialog_steps + 1)] + [
        "Move 2 Question 1", "Move 2 Question 2"
    ] + move_2_2_options_desc() + [
        "Move 2 Question 3"
    ]
    
    return columns

def move_1_2_options_desc():
    # Placeholder function to return the list of option descriptions
    return ["Option 1 Description", "Option 2 Description"]

def move_2_2_options_desc():
    # Placeholder function to return the list of option descriptions
    return ["Option 3 Description", "Option 4 Description"]
