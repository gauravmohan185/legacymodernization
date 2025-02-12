import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from langchain_community.chat_models import AzureChatOpenAI


 
#os.environ["OPENAI_API_KEY"] = "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"

#os.environ["AZURE_OPENAI_API_KEY"] = "5Yo5vDcMqXQKthSerd8BusoE8i4RgCy88dp5qNnicT6BSQ3YLwTlJQQJ99BBACHYHv6XJ3w3AAABACOGyjSJ"
os.environ["AZURE_OPENAI_API_KEY"]
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://dbs-openai-gpt-4o1-poc01.openai.azure.com/"

llm = AzureChatOpenAI(
    deployment_name="gpt-4o-mini",  # The name of your deployed model
    openai_api_version="2024-08-01-preview",
    model_name="gpt-4o-mini",                      # The model you deployed (gpt-4, gpt-3.5-turbo, etc.)
    temperature=0.2                          # Adjust the creativity of the response
)

with open('scripts/prompts/generateCodeFromAntlr.txt', 'r') as file:
    prompt = file.read()

with open('src/cobol/addnumbers_code_structure.json', 'r') as file:
    antlr_json = file.read()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", prompt),
        ("human", "{antlr_json}")

    ]
)
 
class JavaCodeStripperOutputParser(BaseOutputParser[str]):
    """
    Custom output parser to strip ```java and ``` from OpenAI responses.
    """

    def parse(self, text: str) -> str:
        # Strip code block markers ```java ... ```
        if text.startswith("```java"):
            text = text.replace("```java", "").strip()
        if text.endswith("```"):
            text = text[:-3].strip()
        
        return text
 
# Initialize OpenAI LLM (adjust model and parameters accordingly)
#llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
output_parser = JavaCodeStripperOutputParser()
chain = prompt_template | llm | output_parser


response = chain.invoke(
    {
        "antlr_json": antlr_json
    }
)

print(prompt_template)
print(response)

with open("src/java/fromantlr/AddNumbersFunction.java", "w") as file:
    file.write(response)