# a5a0664a3815

---

## high level plan

NOTE: All the operations are performed inside poetry shell. To get inside use:

```
$ poetry shell
```

## Linting

Linting is performed with flake8 toolset. To lint the code use:

```
$ poetry run flake8
```

## Formatting

Formatting is performed with black toolset. To format the code use:

```
$ poetry run black .
```

## Installation

The app can be install using [pipx](https://github.com/pypa/pipx)

```
$ pipx install git+https://github.com/w00fmeow/a5a0664a3815.git
```

## Removal

The app can be uninstalled like so:

```
$ pipx uninstall credentials-extractor
```

## Running

```
$ credentials-extractor --help
Usage: change_me [OPTIONS]

Options:
  --help  Show this message and exit.

```

Example with arguments:

```
$ credentials-extractor --help
```

## Tests

Runing tests with poetry:

```
$ poetry run pytest
```
