# Everything in backend will be able to reach constants


from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data"  # src to data
VECTOR_DB_PATH = Path(__file__).parents[1] / "knowledge_base"
