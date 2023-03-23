# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Background

## Folder Structure

* [`resources`](./resources): Random nice resources, e.g. [`useful links`](./resources/README.md)
* [`src`](./src): Folder for all source files specific to this project
* [`scripts`](./scripts): Folder with example scripts for performing different tasks (could serve as usage documentation)
* [`tests`](./tests) Test example
* [`media`](./media): Folder containing media files (icons, video)
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
    
```bash
pip install -r requirements.txt
```

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

Feel free to help out! Open an issue, submit a PR or [contact us](https://amsterdamintelligence.com/contact/).

## Acknowledgements

{% if cookiecutter.team == 'AI' -%}
This repository was created by [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the City of Amsterdam.

{% elif cookiecutter.team == 'intern' %}
This repository was created in collaboration with [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the City of Amsterdam.

{% endif %}

## License 

TODO choose a license from [here](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)