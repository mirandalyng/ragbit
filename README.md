# Ragbit

## Setup

**Init py project**

```bash
uv init --no-package --python 3.13
```

**Create packages**

```bash
uv init --package backend
uv init --package frontend
```

**Specifie packages in pyproject in each package**

_Example (in backend/pyproject.toml)_

```python
requires-python = ">=3.13"
dependencies = [
    "pydantic-ai",
    "lancedb",
    "fastapi",

]
```

**To uv sync all packages:**

```bash
 uv sync --all-packages
```

## .env

Here you put your NVIDIA API KEY.

```.env
NVIDIA_API_KEY = {your api key here}
```
