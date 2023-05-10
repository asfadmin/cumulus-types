# Cumulus Types
Cumulus Types

## Installing
Cumulus Types can be installed from GitHub using `pip`.
```
$ pip install git+https://github.com/asfadmin/cumulus-types@main
```

## Developing
Type definitions are generated automatically from the Cumulus JSON Schemas. The
generation code is located in the `gentypes` module which is not part of the
package distribution.

To use this module, install the dependencies with poetry:
```
poetry install --with gentypes
```

And then run the main entry point:
```
poetry run python -m gentypes /path/to/cumulus
```
