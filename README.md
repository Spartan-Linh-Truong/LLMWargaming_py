# LLMWargaming_py

A sophisticated Python-based simulation framework that uses Large Language Models (LLMs) to conduct AI-powered wargaming scenarios, specifically focused on US-China crisis simulations for research and policy analysis.

## 🎯 Overview

**LLMWargaming_py** leverages OpenAI's GPT models to simulate human decision-making in complex geopolitical crisis scenarios. The framework enables researchers to study crisis escalation patterns, decision-making processes, and strategic interactions through AI-powered agents representing different players and roles.

### Key Features

- **🤖 LLM-Powered Simulation**: Uses GPT-3.5-turbo-16k to simulate realistic human decision-making
- **🌏 Crisis Scenario Framework**: Specialized for US-China crisis simulations with configurable parameters
- **👥 Multi-Agent System**: Supports teams with different player personalities and roles
- **⚙️ Flexible Configuration**: Extensive customization options for experimental design
- **📊 Research-Ready Output**: Automated results processing and CSV export for analysis

## 🏗️ Architecture

### Core Components

- **`src/game.py`** (11.8KB) - Main simulation engine and game logic
- **`src/players.py`** (4.7KB) - Player management and personality systems
- **`src/simulation.py`** (2.6KB) - Simulation configuration and setup
- **`src/utils.py`** (1.2KB) - Utility functions and chat setup
- **`src/survey_processing.py`** (4KB) - Results processing and analysis

### Game Assets (`wargame/` directory)

- **Scenario Files**: Crisis contexts, incidents, and theater maps
- **Role Definitions**: Player roles and team structures
- **Move Templates**: Decision options and transition logic
- **Pre-generated Data**: Bootstrap player data and test datasets (JSON format)
- **Configuration Files**: AI accuracy ranges, training levels, and strategic postures

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- OpenAI API key
- Required Python packages (see `requirements.txt`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Spartan-Linh-Truong/LLMWargaming_py.git
   cd LLMWargaming_py
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**
   ```bash
   export OPENAI_API_KEY='sk-your-api-key-here'
   ```

4. **Run simulation**
   ```bash
   python run_game.py
   ```

5. **View results**
   Results are automatically saved to the `results/` directory in CSV format.

## ⚙️ Configuration Options

### Simulation Parameters

The framework supports extensive configuration through the `SimulationConfig` class:

#### Crisis Scenario Variables
- **AI Accuracy Range**: `"70-85%"` vs `"95-99%"` - Simulates different AI system capabilities
- **AI System Training**: `"basic"` vs `"significant"` - Represents AI training levels
- **China's Strategic Posture**: `"revisionist"` vs `"status_quo"` - Different strategic orientations

#### Team and Player Settings
- **Number of Teams**: Configurable team count for statistical analysis
- **Players per Team**: Team size configuration (default: 6 players)
- **Dialog Steps**: Number of interaction rounds (default: 3)

#### Player Personality Variants
- **Standard Players**: Balanced decision-making profiles
- **Pacifists**: `pacificsm=True` - Conflict-averse decision patterns
- **Sociopaths**: `sociopaths=True` - Aggressive decision-making profiles

#### Operational Modes
- **Real GPT Mode**: `use_dummygpt=False` - Uses actual OpenAI API
- **Dummy GPT Mode**: `use_dummygpt=True` - For testing without API calls
- **Bootstrap Mode**: `boostrap_players=True` - Uses pre-generated player data
- **Dialog Options**: `no_dialog=True/False` - Controls interaction patterns

### Example Configuration

```python
conf = init_sim_conf(
    model="gpt-3.5-turbo-16k",
    use_dummygpt=False,           # Use real GPT
    use_bench_players=True,       # Use pre-generated players
    no_dialog=False,              # Enable dialog interactions
    boostrap_players=True,        # Use bootstrap data
    pacificsm=False,              # Standard personalities
    sociopaths=False,             # Standard personalities
    run_test_game=True,           # Run single test game
    n_teams=10,                   # Number of teams
    n_players=6,                  # Players per team
    n_dialog_steps=3,             # Interaction rounds
)
```

## 📊 Research Applications

This framework is designed for:

### Academic Research
- **Crisis Decision-Making Studies**: Analyze patterns in high-stakes decision scenarios
- **AI Behavior Research**: Study LLM decision-making in complex strategic contexts
- **International Relations**: Model diplomatic and military crisis interactions

### Policy Analysis
- **Scenario Planning**: Test different strategic approaches and their outcomes
- **Risk Assessment**: Evaluate escalation probabilities under various conditions
- **Strategic Communication**: Study the impact of different messaging strategies

### Training and Education
- **Wargaming Exercises**: Military and diplomatic training scenarios
- **Strategic Studies**: Educational simulations for policy students
- **Crisis Management**: Training for decision-makers in high-pressure situations

## 📈 Output and Analysis

### Results Format
- **CSV Export**: Structured data for statistical analysis
- **Configurable Columns**: Customizable output fields based on research needs
- **Automated Processing**: Built-in survey processing and data cleaning

### Data Structure
Results include:
- Treatment conditions (AI accuracy, training, China posture)
- Player decisions and reasoning
- Team dynamics and interactions
- Temporal progression of crisis scenarios
- Decision outcome metrics

## 🔬 Experimental Design

The framework supports factorial experimental designs with multiple treatment combinations:

- **2 AI Accuracy Levels** × **2 Training Levels** × **2 Strategic Postures** = **8 Treatment Conditions**
- **Configurable Team Sizes** for statistical power
- **Randomized Player Assignment** to reduce bias
- **Bootstrap Sampling** for reproducible results

## 🛠️ Development

### Dependencies
- **Core**: `scipy`, `pandas`, `tqdm` - Data analysis and progress tracking
- **AI Integration**: `openai` - LLM API integration
- **Configuration**: `omegaconf` - Flexible configuration management

### Extending the Framework
- **Custom Scenarios**: Add new crisis contexts in `wargame/` directory
- **Player Types**: Extend personality models in `src/players.py`
- **Analysis Tools**: Enhance processing capabilities in `src/survey_processing.py`

## 📝 Citation

If you use this framework in your research, please cite:

```bibtex
@software{llmwargaming_py,
  title={LLMWargaming_py: AI-Powered Crisis Simulation Framework},
  author={Spartan-Linh-Truong},
  year={2024},
  url={https://github.com/Spartan-Linh-Truong/LLMWargaming_py}
}
```

## 📄 License

This project is available under the terms specified in the repository. Please check the license file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests to improve the framework.

## 📞 Support

For questions, issues, or collaboration opportunities, please open an issue on GitHub or contact the repository maintainer.

---

**Note**: This framework is designed for research and educational purposes. Results should be interpreted within the context of AI simulation limitations and not as predictive of real-world outcomes.