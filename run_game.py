import os
import pandas as pd
from tqdm import tqdm
from time import sleep
from src.game import run_game, gen_all_treatments, gen_teams
from src.simulation import init_sim_conf, SimulationConfig, results_df
from src.players import changeXP_player
from src.utils import ChatSetup, create_file_ending
import json
from omegaconf import OmegaConf

def run_simulation(config: SimulationConfig):

    # Prepare the connection to the GPT model
    if config.secret_key == "":
        print("Warning: OPENAI_API_KEY not set in ENV")
    
    chat_setup = ChatSetup(config.secret_key, config.model, config.use_dummygpt)

    # Setup the results dataframe and game dir
    columns = results_df(config)
    res = []
    # Setup output file names
    if config.out_csv_file == "":
        ending = create_file_ending(config.output_dir)
        data_filename = os.path.join(config.output_dir, f"data{ending}.csv")
    else:
        data_filename = os.path.join(config.output_dir, config.out_csv_file)
    
    if config.use_bench_players:
        with open("wargame/test_data.json", "rb") as f:
            test_data = json.load(f)
            test_data = OmegaConf.create(test_data)
        treatments = test_data[0]
        teams = test_data[1]
    else:
        # Generate Treatments
        treatments = gen_all_treatments(config)

        # Generate teams
        teams = gen_teams(config)
    
    if config.pacificsm:
        for team_ind, team in enumerate(teams):
            teams[team_ind] = [changeXP_player(p, "Strict pacifist") for p in team]
    elif config.sociopaths:
        for team_ind, team in enumerate(teams):
            teams[team_ind] = [changeXP_player(p, "Aggressive sociopath") for p in team]
    
    # Run a test game or all treatments * teams
    if config.run_test_game:
        result = run_game(config, treatments[0], teams[0], chat_setup)
        result = result[:1] + result[19:]
        res.append(result)

        # Write the results DataFrame to a CSV file
        if config.save_results_to_csv:
            pd.DataFrame(res, columns=columns).to_csv(data_filename, index=False)
    else:
        # Run the games
        for j, team in tqdm(enumerate(teams), desc="Teams"):
            print(f"Team: {j}")
            for i, game in tqdm(enumerate(treatments), desc="Treatments"):
                print(f"Running treatment: {i}")
                try:
                    result = run_game(config, game, team, chat_setup)
                    result = result[:1] + result[19:]
                    res.append(result)
                    # Write the results DataFrame to a CSV file
                    if config.save_results_to_csv:
                        pd.DataFrame(res, columns=columns).to_csv(data_filename, index=False)
                except Exception as e:
                    print(e)
                    sleep(10)
    
    return res

# Example usage
if __name__ == "__main__":
    conf = init_sim_conf(
        model="gpt-3.5-turbo-16k",
        use_dummygpt=False,
        use_bench_players=True,
        no_dialog=False,
        no_chiefs=False,
        boostrap_players=True,
        pacificsm=False,
        sociopaths=False,
        more_disagreement=False,
        verbose=False,
        run_test_game=True,
        n_teams=10,
        n_players=6,
        n_dialog_steps=3,
    )
    run_simulation(conf)
