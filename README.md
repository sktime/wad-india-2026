# sktime workshop at WeAreDevelopers India 2026

This repository contains materials for a hands-on workshop on [sktime](https://www.sktime.net/), a unified Python framework for machine learning with time series, presented at [WeAreDevelopers India 2026](https://www.wearedevelopers.com/conference-india).

The materials are Jupyter notebooks in `notebooks/`. The notebook list may change over time. Start with the notebooks in `notebooks/` and follow the order suggested by the file names or by the workshop instructor.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sktime/workshop-wad-2026/main?urlpath=lab/tree/notebooks) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sktime/workshop-wad-2026/) [![sktime docs](https://img.shields.io/badge/docs-sktime-blue)](https://www.sktime.net/en/stable/) [![GitHub](https://img.shields.io/badge/github-workshop-black?logo=github)](https://github.com/sktime/workshop-wad-2026/) [![Discord](https://img.shields.io/badge/discord-chat-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/54ACzaFsn7) [![LinkedIn](https://img.shields.io/badge/linkedin-sktime-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/company/scikit-time/)

## Workshop contents

The notebooks are a practical introduction to time series machine learning with `sktime`, with a focus on agentic and LLM-assisted workflows. Topics include:

- **Introduction to forecasting with sktime:** the common `sktime` forecasting interface, from simple baselines to statistical models, reduction, pipelines and probabilistic forecasts.
- **Deep learning for forecasting:** deep learning forecasters and pretraining in `sktime`.
- **Foundation models for forecasting:** using pretrained time series foundation models through `sktime`, fine-tuning them, and when to use them.
- **LLM-assisted forecasting with `AutoResearchForecaster`:** an LLM proposes sktime estimators, and sktime evaluates and refines them.
- **Extending sktime:** writing your own estimators with extension templates.
- **Building estimators with AI coding agents:** agent skills, the skills sktime provides, and a live demo.
- **Benchmarking:** comparing forecasters reproducibly across datasets and evaluation folds.
- **Next steps:** where to go from here and how to get involved with the `sktime` community.

The LLM-assisted notebooks (such as the `AutoResearchForecaster` one) call an LLM through [LiteLLM](https://docs.litellm.ai/). The default model is `openai/gpt-4o-mini`, so set an OpenAI API key in your environment before you start Jupyter:

```bash
export OPENAI_API_KEY="sk-..."
```

To use another provider, change the model string in the notebook to any [LiteLLM model string](https://docs.litellm.ai/docs/providers) (for example `anthropic/...` or `ollama/...`) and set that provider's credentials. Responses are cached locally, so re-running cells does not repeat LLM calls.

The coding-agent demos use an AI coding agent (Claude Code). You don't need one to follow along; it is optional if you want to try the demos yourself.

## Agent skills for sktime

[Agent skills](https://agentskills.io/) are folders with a `SKILL.md` file that teach a coding agent (Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and others) how to do one task well. The agent always sees each skill's short description, and loads the full instructions only when a task matches. sktime provides two sets of skills.

### The `sktime` user skill

[sktime/skills](https://github.com/sktime/skills) contains the `sktime` skill, for **using** sktime in your own projects. It covers forecasting, classification, regression, clustering, anomaly and change-point detection, composition and pipelines, model selection from the model zoo, benchmarking, and writing estimators from extension templates. It also tells the agent how to find and install the soft dependencies a given estimator needs.

**Install with the `skills` CLI** (from [skills.sh](https://skills.sh/); needs Node.js). It detects your installed agents and copies the skill to the right place:

```bash
npx skills add sktime/skills
```

**Or install manually** by cloning the repository into your agent's skills folder. The folder name must be `sktime`.

```bash
# Claude Code, for all your projects
git clone https://github.com/sktime/skills.git ~/.claude/skills/sktime

# Claude Code, for one project only (run from the project root)
git clone https://github.com/sktime/skills.git .claude/skills/sktime

# Codex, Cursor, Gemini CLI and other agents that read .agents/skills (run from the project root)
git clone https://github.com/sktime/skills.git .agents/skills/sktime
```

To update the skill later, run `git pull` inside that folder. On claude.ai or the Claude desktop app, you can instead zip the repository and upload it under *Settings → Capabilities → Skills*.

**Use it** by asking your agent for time series work, for example *"Forecast the next 12 months of `sales.csv` with sktime and compare against a seasonal naive baseline"*. The agent loads the skill on its own when the task matches. In Claude Code you can also call it directly with `/sktime`.

### sktime developer skills

The [sktime repository](https://github.com/sktime/sktime) ships skills for **contributing to** sktime. The same files are in [`.claude/skills/`](https://github.com/sktime/sktime/tree/main/.claude/skills) (for Claude Code) and [`.agents/skills/`](https://github.com/sktime/sktime/tree/main/.agents/skills) (for Codex, Cursor, Gemini CLI and other agents).

| Skill | Use it to |
| --- | --- |
| `sktime-dev-setup` | Set up, check or repair a local development environment: virtual environment, editable install with dev/test/docs extras, pre-commit, upstream remote, local docs build. |
| `sktime-add-estimator` | Add a new estimator end to end: choose the scitype and extension template, set tags, write `get_test_params` and the docstring, add the API reference entry, and pass `check_estimator`. |
| `sktime-add-foundation-model` | Integrate a pretrained time series foundation model (for example from a Hugging Face checkpoint) as a forecaster, including licensing, vendoring, soft dependencies, caching and devices. |
| `sktime-golden-tests` | Write golden-output regression tests that check an estimator matches its original upstream implementation. |
| `sktime-deprecation` | Rename or remove parameters, change defaults, move classes, and handle deprecation cycles and overdue removal markers. |
| `sktime-pr-check` | Self-review a branch or pull request against what maintainers look for, before asking for review or after review comments. It reports findings and never posts to GitHub. |

**Use them when contributing to sktime.** You don't need to install anything. Fork and clone sktime, then start your agent from the repository root, and it picks up the skills automatically:

```bash
git clone https://github.com/<your-username>/sktime.git
cd sktime
claude    # or codex, cursor, gemini, ...
```

Then ask in plain words, for example *"Set up my sktime dev environment"*, *"Add the Theta-ARIMA forecaster from this paper to sktime"* or *"Is my branch ready for a PR?"*. In Claude Code you can also call a skill directly, for example `/sktime-add-estimator`.

**Use them in your own codebase.** `sktime-add-estimator` also works for sktime-compatible estimators in a third-party extension package or a private codebase. Copy it from a clone of sktime into your project:

```bash
git clone --depth 1 https://github.com/sktime/sktime.git /tmp/sktime
mkdir -p .claude/skills .agents/skills
cp -r /tmp/sktime/.claude/skills/sktime-add-estimator .claude/skills/   # Claude Code
cp -r /tmp/sktime/.agents/skills/sktime-add-estimator .agents/skills/   # other agents
```

Skills can include scripts the agent may run. As with any third-party skill, read through it before installing, and review the code an agent writes before you push it.

## What you will need

- Python 3.11, 3.12 or 3.13
- A local clone of this repository
- A Python environment with the workshop dependencies installed
- Jupyter Lab, Jupyter Notebook, or another notebook environment that uses the same Python environment
- An LLM API key for the LLM-assisted sections (see above)

If you are new to Python environments, `uv` is usually the quickest way to set one up. `pip`, `venv`, `conda` and Poetry also work if you already use them.

The main dependency list is in `pyproject.toml`. `requirements.txt` has the same dependencies for people who prefer a pip requirements file.

## Quick setup with uv

From the repository root:

```bash
uv sync --python 3.13
uv run jupyter lab
```

Then open the notebooks in `notebooks/`.

If you don't have `uv` yet, see the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## Setup with venv and pip

From the repository root:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyter lab
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

## Setup with conda

```bash
conda create -n sktime-workshop python=3.13
conda activate sktime-workshop
python -m pip install -r requirements.txt
python -m jupyter lab
```

## Setup with Poetry

Use Poetry 2.0 or newer.

```bash
poetry env use 3.13
poetry install
poetry run jupyter lab
```

Open the repository in Jupyter Lab and select the kernel for the environment where you installed the dependencies. If that environment is not listed as a kernel, register it yourself:

```bash
python -m ipykernel install --user --name sktime-workshop --display-name "sktime workshop"
```

Restart the notebook kernel after you change dependencies or switch environments.

## Troubleshooting

- If a package cannot be imported, check that Jupyter is using the same Python environment where you installed the dependencies.
- The deep learning and foundation model dependencies (PyTorch, `transformers`, `timesfm`, `pytorch-forecasting`) are large, a few GB in total. Set up the environment before the workshop, not on conference Wi-Fi.
- The foundation model notebooks download pretrained model weights from Hugging Face the first time they run. Run them once before the workshop so the weights are cached.
- If the LLM calls fail with an authentication error, check that your API key is set in the same shell or environment that started Jupyter, then restart the kernel.
- If you are on macOS with Apple Silicon and an optional dependency fails to install, set up the core workshop environment first and install optional packages only when you need them.
- For general sktime installation notes, see the [sktime installation guide](https://www.sktime.net/en/stable/installation.html).

## About sktime

`sktime` provides scikit-learn compatible tools for time series learning tasks such as forecasting, classification, regression, clustering, annotation, and pipeline composition. See the [sktime website](https://www.sktime.net/), [documentation](https://www.sktime.net/en/stable/), and [GitHub repository](https://github.com/sktime/sktime) for more.

Community links are on the sktime [get involved page](https://www.sktime.net/en/stable/get_involved.html).

For reference, there is also [sktime-mcp](https://github.com/sktime/sktime-mcp), an MCP (Model Context Protocol) server that lets LLM clients use sktime.

## Other sktime workshops and tutorials

Similar workshop and tutorial repositories, most recent first:

- [PyCon Ireland 2026 - sktime workshop](https://github.com/sktime/sktime-workshop-pycon-ireland-2026)
- [WeAreDevelopers World Congress Europe 2026 - sktime workshop](https://github.com/sktime/sktime-workshop-wearedevelopers-europe-2026)
- [Python Brasil 2025 - sktime workshop materials](https://github.com/sktime/python_brasil_2025)
- [PyCon Colombia 2025 - sktime workshop](https://github.com/sktime/sktime-workshop-pycon-colombia-2025)
- [HAICON Prologue Day 2025 - sktime tutorial materials](https://github.com/sktime/tutorial_haicon_prologue_day)
- [PyData Global 2024 - sktime tutorial](https://github.com/sktime/sktime-tutorial-pydata-global-2024)
- [ODSC Europe 2024 - sktime tutorial](https://github.com/sktime/sktime-tutorial-ODSC-Europe-2024)
- [PyCon PL 2024 - sktime workshop](https://github.com/sktime/sktime-workshop-pyconPL2024)
- [EuroSciPy 2024 - hierarchical and global forecasting, foundation models, extensions, and marketplace](https://github.com/sktime/sktime-tutorial-euroscipy2024)
- [SciPy 2024 - sktime workshop](https://github.com/sktime/sktime-workshop-scipy-2024)
- [PyData Global 2023 - general sktime introduction and new features](https://github.com/sktime/sktime-tutorial-pydata-global-2023)
- [PyData Amsterdam 2023 - probabilistic prediction, forecasting, and evaluation](https://github.com/sktime/sktime-tutorial-pydata-Amsterdam-2023)
- [PyData Prague 2023 - forecasting, advanced pipelines, and benchmarking](https://github.com/sktime/sktime-workshop-pydata-prague-2023)
- [EuroPython 2023 - general sktime introduction](https://github.com/sktime/sktime-tutorial-europython-2023)
- [ODSC Europe 2023 - forecasting, pipelines, and ML engineering](https://github.com/sktime/sktime-tutorial-ODSC-Europe-2023)
- [PyData London 2023 - time series classification, regression, distances, and kernels](https://github.com/sktime/sktime-tutorial-pydata-london-2023)
- [PyData Global 2022 - feature extraction, pipelines, and tuning](https://github.com/sktime/sktime-tutorial-pydata-global-2022)
- [PyData London 2022 - sktime workshop](https://github.com/sktime/sktime-workshop-pydata-london-2022)

## Contributing

Contributions to the workshop materials are welcome. If you find a problem, please open a GitHub issue or pull request in this repository. For contributions to `sktime` itself, see the sktime [contribution guide](https://www.sktime.net/en/stable/get_involved/contributing.html).
