from openai import OpenAI
from tool import get_course_fee

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_course_fee",
        "description": "Look up the fee for a college course using its course code.",
        "parameters": {
            "type": "object",
            "properties": {
                "course_code": {
                    "type": "string",
                    "description": "The course code, such as AI202 or CS101."
                }
            },
            "required": ["course_code"]
        }
    }
]

question = "What is the fee for AI202?"

response = client.responses.create(
    model="gpt-5-mini",
    input=question,
    tools=tools
)

for item in response.output:
    if item.type == "function_call":
        print("Tool call:")
        print("Function:", item.name)
        print("Arguments:", item.arguments)

        result = get_course_fee("AI202")

        print("Tool result:", result)