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
$ pipx uninstall change_me
```

## Running

```
$ change_me --help
Usage: change_me [OPTIONS]

Options:
  --help  Show this message and exit.

```

Example with arguments:

```
$ change_me --help
```

## Tests

Runing tests with poetry:

```
$ poetry run pytest
```
