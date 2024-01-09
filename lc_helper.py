import environ
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
env = environ.Env()
environ.Env.read_env()

OPENAI_API_KEY = env('OPENAI_API_KEY')

def generate_therapy_response(question):
    llm = openai.OpenAI(temperature = 0.7)

    prompt_template_name = PromptTemplate(
        input_variables = ['question'],
        template = "This is a teenager talking. Give me a positive response for the query, {question}"
    )

    name_chain = LLMChain(llm = llm, prompt = prompt_template_name)

    response = name_chain({'question': question})

    return response

if __name__ == "__main__":
    print(generate_therapy_response("I'm feeling really angry with myself because I failed my math test, what do I do?"))