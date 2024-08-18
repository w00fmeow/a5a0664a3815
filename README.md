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
Usage: credentials-extractor [OPTIONS]

Options:
  --s3_bucket_name TEXT  S3 bucket name  [required]
  --s3_access_key TEXT   S3 access key  [required]
  --s3_secret TEXT       S3 secret  [required]
  --help                 Show this message and exit.


```

Example with arguments:

```
$ credentials-extractor --s3_bucket_name BUCKET_NAME --s3_access_key ACCESS_KEY --s3_secret SECRET

```

## Tests

Runing tests with poetry:

```
$ poetry run pytest
```
