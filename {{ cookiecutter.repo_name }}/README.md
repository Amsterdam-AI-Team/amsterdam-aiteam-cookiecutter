# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Background

## Folder Structure

* [`data`](./data): Sample data for demo purposes
* [`docs`](./docs): If main [README.md](./README.md) is not enough
* [`notebooks`](./notebooks): Jupyter notebooks / tutorials
* [`res`](./res): Relevant resources, e.g. [`images`](./res/images/) for the documentation
* [`scripts`](./scripts): Scripts for automating tasks
* [`src`](./src): All sourcecode files specific to this project
* [`tests`](./tests) Unit tests
* ...

## Installation 

1) Clone this repository:

{% if cookiecutter.team == 'AI' -%}

```bash
git clone https://github.com/Amsterdam-AI-Team/{{ cookiecutter.repo_name }}.git
```

{% elif cookiecutter.team == 'intern' %}

```bash
git clone https://github.com/AmsterdamInternships/{{ cookiecutter.repo_name }}.git
```

{% endif %}


2) Install all dependencies:
    
{% if cookiecutter.env_management == 'pip' %}

```bash
pip install -r requirements.txt
```

{% elif cookiecutter.env_management == 'conda' %}

```bash
conda env create -f environment.yml
```

{% endif %}

The code has been tested with Python x.x on Linux/MacOS/Windows. 

## Usage

## How it works

Can be divided in subsections:

### input
### algorithm
### output

OR

### training
### prediction
### evaluation

## Contributing

{% if cookiecutter.team == 'AI' -%}

Feel free to help out! [Open an issue](https://github.com/Amsterdam-AI-Team/{{ cookiecutter.repo_name }}/issues), submit a [PR](https://github.com/Amsterdam-AI-Team/{{ cookiecutter.repo_name }}/pulls) or [contact us](https://amsterdamintelligence.com/contact/).

{% elif cookiecutter.team == 'intern' %}

Feel free to help out! [Open an issue](https://github.com/AmsterdamInternships/{{ cookiecutter.repo_name }}/issues), submit a [PR](https://github.com/AmsterdamInternships/{{ cookiecutter.repo_name }}/pulls)  or [contact us](https://amsterdamintelligence.com/contact/).

{% endif %}


## Acknowledgements

{% if cookiecutter.team == 'AI' -%}
This repository was created by [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the City of Amsterdam.

{% elif cookiecutter.team == 'intern' %}
This repository was created in collaboration with [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the City of Amsterdam.

{% endif %}

Optional: add citation or references here.


## License 

This project is licensed under the terms of the European Union Public License 1.2 (EUPL-1.2).
