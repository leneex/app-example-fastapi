# FastAPI

Example [FastAPI](https://fastapi.tiangolo.com/) app. FastAPI is a modern, fast Python framework for building APIs, with data validation and interactive docs generated from type hints.

## Deploy settings

| Field | Value |
| --- | --- |
| Build | Railpack |
| Project directory | `/` |
| Install command | leave empty |
| Build command | leave empty |
| Start command | leave empty |
| Application port | `8000` |
| Health check path | `/` |

## <a name="dev"></a>Run locally

```bash
# virtual environment and dependencies
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# start the app
python3 main.py
```
