from langchain.llms import OpenAI
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

documents = SimpleDirectoryReader("docs/").load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

def search_docs(query):
    return index.query(query)
