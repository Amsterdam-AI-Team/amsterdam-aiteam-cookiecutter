# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Folder Structure

* [`resources`](./resources): Random nice resources, e.g. [`useful links`](./resources/README.md)
* [`src`](./src): Folder for all source files specific to this project
* [`scripts`](./scripts): Folder with example scripts for performing different tasks (could serve as usage documentation)
* [`tests`](./tests) Test example
* [`media`](./media): Folder containing media files (icons, video)
* ...

OR

Use something like `tree` to include the overall structure with preferred level of detail (`-L 2` or `-d` or `-a`...)
```buildoutcfg
├── media --> you can still add comments and descriptions in this tree
│   └── examples
├── resources --> a lot of useful links here
├── scripts
├── src --
└── tests
```

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


1) Install all dependencies:
    
```bash
pip install -r requirements.txt
```

## Usage

|Argument | Type or Action | Description | Default |
|---|:---:|:---:|:---:|
|`--batch_size`| int| `Batch size.`|  32|
|`--device`| str| `Training device, cpu or cuda:0.`| `cpu`|
|`--early-stopping`|  `store_true`| `Early stopping for training of sparse transformer.`| True|
|`--epochs`| int| `Number of epochs.`| 21|
|`--input_size`|  int| `Input size for model, i.e. the concatenation length of te, se and target.`| 99|
|`--loss`|  str|  `Type of loss to be used during training. Options: RMSE, MAE.`|`RMSE`|
|`--lr`|  float| `Learning rate.`| 1e-3|
|`--train_ratio`|  float| `Percentage of the training set.`| 0.7|
|...|...|...|...|


## Acknowledgements

{% if cookiecutter.team == 'AI' -%}
This repository was created by [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the City of Amsterdam.

{% elif cookiecutter.team == 'intern' %}
This repository was created in collaboration with [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the City of Amsterdam.

{% endif %}

## License 

TODO choose a license from [here](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)


