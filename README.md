# goal-guru

The Goal Guru application has the objective of helping you create SMART goals, for the purpose of guiding employees and managers with goal-setting, at companies requiring goals as part of the performance management process, with inputs from employees and management, to enable high-performance teams, doing meaningful work that contribute to higher level strategic goals of the company.

## Purpose
Goal-setting and performance contracts are dreaded by employees and managers alike. It is a slow process, and often is neglected. Goals then tend to be vague, with no clear measurements and outcomes. Consistency between the goals of different individuals remain a challenge. Performance reviews are then meaningless and good and bad performance can not be measured meaningfully. As a result, the benefit of improving performance over time, and addressing problem areas, are neglected. In order not to do work without any meaning, goal-setting itself needs to be useful and have a clear business outcome and benefit.

## Design
This is a [gradio](https://gradio.app/) web application that uses Whisper and ChatGPI APIs from [OpenAI](https://openai.com/).

## Getting started
1. Ensure `git` and `python` (version 3.6+) are installed.
2. Clone this project with `git clone git@github.com:thirionjwf/goal-guru.git`.
3. Sign up for an account at [OpenAI](https://platform.openai.com/).
4. Create an [API key](https://platform.openai.com/account/api-keys).
5. Setup the config file in `.env` using the template in `config.txt`.
6. Create and edit the company objectives file (`cp company_objectives-example.csv company_objectives.csv`).
7. Create a Python environment in the project folder with `python -m venv .env`.
8. Activate the Python virtual environment with `source .venv/bin/activate`, or `deactivate` to exit.
9. Install pre-requisites (run `pip install -r requirements.txt`):
```
pip install --upgrade pip
pip install gradio
pip install pandas
pip install config
pip install pre-commit
pip install toml
pip install black
pip install flake8
pip install isort
pip install openai
```
10. Install the pre-commit hooks:
```
pre-commit --version
pre-commit install
pre-commit run --all-files
```
11. Run the project by typing `gradio app.py` on the command line.

## Credits
This project drew its inspiration (and borrowed heavily from) the following YouTube video by [Part Time Larry](https://www.youtube.com/watch?v=Si0vFx_dJ5Y):
[OpenAI ChatGPT API (NEW GPT 3.5) and Whisper API - Python and Gradio Tutorial](https://youtu.be/Si0vFx_dJ5Y)
