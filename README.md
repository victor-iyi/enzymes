# enzymes

<!-- [![CI](https://github.com/victor-iyi/enzymes/actions/workflows/ci.yaml/badge.svg)](https://github.com/victor-iyi/enzymes/actions/workflows/ci.yaml) -->
<!-- [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/victor-iyi/enzymes/main.svg)](https://results.pre-commit.ci/latest/github/victor-iyi/enzymes/main) -->
[![formatter | docformatter](https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter)
[![style | google](https://img.shields.io/badge/%20style-google-3666d6.svg)](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)

[ENZYMES][enzymes] is a dataset of protein tertiary structures obtained from
*(Borgwardt et al., 2005)* consisting of 600 enzymes from the BRENDA enzyme
database *(Schomburg et al., 2004)* where each graph represents exactly one
protein. The task is to correctly assign each enzyme to one of the 6
[Enzyme Commission][enzyme-cn] top-level enzyme classes (EC classes).

1. EC 1 Oxidoreductases
2. EC 2 Transferases
3. EC 3 Hydroiases
4. EC 4 Lyases
5. EC 5 Isomerases
6. EC 6 Ligases

[enzymes]: https://paperswithcode.com/dataset/enzymes
[enzyme-cn]: https://www.abbexa.com/enzyme-commission-number

## Installation

Create and activate a new virtual environment.

```sh
virtualenv venv
. venv/bin/activate
```

Install necessary dependencies by running the following commands:

```sh
poetry install --with dev

# To enable GPU acceleration (for Apple Silicon only).
poetry install --with dev -E metal
```

You can either manually install [`spektral`] by running `pip install spektral`.
However, if that doesn't work on your device for some reason, you can always
build it from source as show below:

```sh
# Clone spektral from GitHub.
git clone https://danielegrattarola/spektral.git

# Run the install script.
cd spektral && pip install .

# Remove the clone repo after successful installation.
cd ..
rm -rf spektral
```

To test the successful installation of `spektral`, run:

```sh
python -c "import spektral; print(spektral.__version__)"
1.2.0
```

For more [installation instructions for spektral][`spektral`].

[`spektral`]: https://graphneural.network

## Contribution

You are very welcome to modify and use them in your own projects.

Please keep a link to the [original repository]. If you have made a fork with
substantial modifications that you feel may be useful, then please [open a new
issue on GitHub][issues] with a link and short description.

## License (MIT)

This project is opened under the [MIT][license] which allows very
broad use for both private and commercial purposes.

A few of the images used for demonstration purposes may be under copyright.
These images are included under the "fair usage" laws.

[original repository]: https://github.com/victor-iyi/enzymes
[issues]: https://github.com/victor-iyi/enzymes/issues
[license]: ./LICENSE
