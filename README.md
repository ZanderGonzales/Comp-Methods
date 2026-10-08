# Computational Methods

Coursework scripts, data files, and lab materials for Computational Methods.

## Reproducible setup

The repository targets Python 3.12.10 and pins the third-party packages used
by the scripts.

On Windows, create a virtual environment and install the dependencies with:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run a script from the directory containing its input files. For example:

```powershell
python ".\Original Labs\Lab 3.py"
```

Most scripts use relative paths for their data files, so the working directory
matters. The data files required by the coursework are included in the
repository.
