# Cookiecutter Amsterdam AI Team 

A [cookiecutter](https://www.cookiecutter.io/) template maintained by the AI Team of the City of Amsterdam.

## Cookiecutter Structure

* [`{{ cookiecutter.repo_name }}`](./{{%20cookiecutter.repo_name%20}}): the folder used for project creation
* [`cookiecutter.json`](./cookiecutter.json): cookiecutter parameters and default values

## Installation
```bash
git clone https://github.com/Amsterdam-AI-Team/amsterdam_aiteam_cookiecutter.git
```

## Usage
```bash
pip install cookiecutter
cookiecutter https://github.com/Amsterdam-AI-Team/amsterdam_aiteam_cookiecutter
```

You will be prompted to provide the following parameters:

| Parameter       | Description                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`  | The name of the project to be displayed as a header of the readme                                                                                                       |
| `repo_name`     | The name of the repository. It will be used as name of the root folder                                                                                                  |
| `description`   | Short description of the repository to be used in the readme                                                                                                            |
| `team`          | "AI" or "intern" - will be used to fill in the clone step in the installation section with the correct github organization (Amsterdam-AI-Team or Amsterdam-Internships) |
| `env_management`| "pip" or "conda" - will be used to fill in the packages step in the installation section                                                                                |

## Acknowledgements

This repository was created by [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the City of Amsterdam.

The content of this repository is inspired by other cookiecutter templates such as the [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) and [cookiecutter-modern-datascience](https://github.com/crmne/cookiecutter-modern-datascience).

We also owe special thanks to fellow data scientists and developers from the City of Amsterdam for the provided input on best practices and guidelines.

## Contributing

Feel free to help out! [Open an issue](https://github.com/Amsterdam-AI-Team/amsterdam_aiteam_cookiecutter/issues), submit a [PR](https://github.com/Amsterdam-AI-Team/amsterdam_aiteam_cookiecutter/pulls) or [contact us](https://amsterdamintelligence.com/contact/).

## License 

This project is licensed under the terms of the European Union Public License 1.2 (EUPL-1.2).
