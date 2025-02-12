import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser


 
os.environ["OPENAI_API_KEY"] = "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"

with open('scripts/prompts/generateTests.txt', 'r') as file:
    prompt = file.read()

with open('src/java/AddNumbersFunction.java', 'r') as file:
    java_code = file.read()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", prompt),
        ("human", "{java_code}")

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
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
output_parser = JavaCodeStripperOutputParser()
chain = prompt_template | llm | output_parser


response = chain.invoke(
    {
        "java_code": java_code
    }
)

print(prompt_template)
print(response)

with open("tests/java/AddNumbersFunctionTest.java", "w") as file:
    file.write(response)