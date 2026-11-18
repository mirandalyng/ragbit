# Agent and tool

from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DB_PATH
import lancedb
from model import setup_model

vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

model = setup_model("nvidia/nemotron-3.5-super-vl-120b-a12b")

rag_agent = Agent(
    model=model,
    retries=2,
    system_prompt=(
        "You are an expert in rabbit races and knows how to distinguish between the rabbits",
        "Always answer based on the retrieved knowledge, but you can mix in your expertise to make the answer more coherent",
        "Don't hallucinate, rather say you can't answer it if the user prompts outside of the retrieved knowledge",
        "Make sure tho keep the answer clear and concise, getting to the point directly, max 6 sentences",
        "Also describe which file you have used as source",
    ),
    output_type=RagResponse,
)


# tool
@rag_agent.tool_plain
def retrieve_top_doc(query: str) -> str:
    """
    vector search to match closest document to the query
    """

    results = vector_db["articles"].search(query=query).to_list()

    return f"""
    
    Filename: {results[0]["filename"]},
    
    Filepath: {results[0]["filepath"]},

    Content: {results[0]["content"]}
    
    """
