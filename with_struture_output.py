from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict



load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

class review(TypedDict):

    summary : str
    sentiment : str

struture_model=model.with_structured_output(review)

result=struture_model.invoke("The fragrance feels too synthetic and slightly harsh after a few minutes. Some users even find it unpleasant compared to other budget deos")

print(result)
print(result['summary'])
print(result['sentiment'])