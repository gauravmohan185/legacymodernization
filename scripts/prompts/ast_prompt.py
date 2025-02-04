from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.schema import BaseOutputParser
 
# Define the PromptTemplate
prompt_template = """
You are an expert in programming languages and Java development. Your task is to generate a modular, accurate, and maintainable Java program based on the provided Abstract Syntax Tree (AST) in JSON format, so that the logic of the COBOL program should precisely reflect in the generated Java program.
 
The AST JSON structure contains nodes representing COBOL program elements, such as PROCEDURE DIVISION, DATA DIVISION, variables, file handling, basic arithmetic & logical operations.
 
- The AST JSON is generated from COBOL grammar using ANTLR.
- The Java program should adhere to the following guidelines:
  - Follow industry best practices for maintainability and modularization.
  - Java code should properly follow the OOPS concepts.
  - Include proper exception handling, logging, and comments.
  - Use meaningful names for variables, methods, and classes.
  - Write clean, readable, and testable code.
Generate only the Java code as output. The provided AST is: {ast_json}
"""
 
# Create the Langchain prompt template
template = PromptTemplate(
    input_variables=["ast_json"],
    template=prompt_template
)
 
# Define a simple output parser class (optional, you can define any custom output parser)
class SimpleJavaOutputParser(BaseOutputParser):
    def parse(self, output: str) -> str:
        # You can implement any logic to further parse the output if needed
        return output.strip()
 
# Initialize OpenAI LLM (adjust model and parameters accordingly)
llm = OpenAI(model="gpt-4", temperature=0.2)
 
# Set up the chain with the prompt template and LLM
chain = LLMChain(prompt=template, llm=llm, output_parser=SimpleJavaOutputParser())
 
# Example AST JSON to input
ast_json_example = '''
{
  "type": "Program",
  "divisions": {
    "procedure": {
      "operations": [
        {"type": "COMPUTE", "left": "A", "operator": "+", "right": "B", "result": "C"}
      ]
    },
    "data": {
      "variables": [
        {"name": "A", "type": "int"},
        {"name": "B", "type": "int"},
        {"name": "C", "type": "int"}
      ]
    }
  }
}
'''
 
# Run the chain with the AST JSON
java_code = chain.run(ast_json=ast_json_example)
 
# Output the generated Java code
print(java_code)