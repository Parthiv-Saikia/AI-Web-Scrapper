from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Replace with your actual Groq API key and endpoint (OpenAI-compatible)
model = ChatOpenAI(
    model="llama3-70b-8192",  # or "mixtral-8x7b-32768" or any model of your choice
    openai_api_key="Your Groq API KEY",
    base_url="https://api.groq.com/openai/v1",  # Groq's endpoint
)

def parse_with_groq(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parse_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parse_results.append(response.content if hasattr(response, "content") else response)

    return "\n".join(parse_results)
