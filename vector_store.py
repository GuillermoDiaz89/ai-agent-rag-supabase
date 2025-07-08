import os
from supabase import create_client, Client
from typing import List

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_vectors(chunks: List[str], vectors: List[List[float]]) -> None:
    for chunk, vector in zip(chunks, vectors):
        response = supabase.table("documents").insert({
            "content": chunk,
            "embedding": vector
        }).execute()
        if response.data is None:
            print("Error storing vector:", response)

def search_similar_chunks(question_vector: List[float], top_k: int = 3) -> List[str]:
    response = supabase.rpc("match_documents", {
        "query_embedding": question_vector,
        "match_count": top_k
    }).execute()
    if response.data is None:
        print("Error retrieving similar chunks:", response)
        return []
    return [doc["content"] for doc in response.data]
