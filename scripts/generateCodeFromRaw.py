import os
import glob

from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from langchain_community.chat_models import AzureChatOpenAI


os.environ["AZURE_OPENAI_API_KEY"]
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://dbs-openai-gpt-4o1-poc01.openai.azure.com/"

llm = AzureChatOpenAI(
    deployment_name="gpt-4o-mini",  # The name of your deployed model
    openai_api_version="2024-08-01-preview",
    model_name="gpt-4o-mini",                      # The model you deployed (gpt-4, gpt-3.5-turbo, etc.)
    temperature=0.2                          # Adjust the creativity of the response
)


with open('scripts/prompts/generateCodeFromRaw.txt', 'r') as file:
    prompt = file.read()


with open('src/cobol/addnumbers.cbl', 'r') as file:
    cobol_code = file.read()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", prompt),
        ("human", "{cobol_code}")

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


# Loop through all .cbl files in the src/cobol directory
for cobol_file in glob.glob('src/cobol/*.cbl'):
    with open(cobol_file, 'r') as file:
        cobol_code = file.read()

    response = chain.invoke(
        {
            "cobol_code": cobol_code
        }
    )

    output_file = cobol_file.replace('src/cobol', 'src/java/fromraw').replace('.cbl', 'Function.java')
    with open(output_file, "w") as file:
        file.write(response)

print(prompt_template)
print(response)

#with open("src/java/fromraw/AddNumbersFunction.java", "w") as file:
 #   file.write(response)
