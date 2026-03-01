import os

from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
os.environ["DASHSCOPE_API_KEY"] = "sk-597dad8574134de6be60dbf74113d5de"


vector_store = DashScopeEmbeddings()

print(vector_store.embed_query("你是谁"))