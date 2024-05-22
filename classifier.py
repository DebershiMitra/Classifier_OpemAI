from openai import OpenAI
import json
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_completion(prompt, model="gpt-4-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response.choices[0].message.content


user_request = input("Enter the prompt: ")
def test(user_request):
    prompt =f"""I am a virtual assistant trained to classify user requests into specific categories. Below are some categories and examples of user requests:

                1. Search Web:
                - "Please recommend some upcoming movies which I can watch with my family on a weekend in a local theatre."
                - "Hey, can you quickly do a web search for me? I want to know how many pounds is 10 kilograms."

                2. Send Email:
                - "Write an email to ask the entire team if they are available for a meeting tomorrow at 3PM."
                - "Send a mail with file.xyz as an attachment to everyone."
                - "Generate an email to share the last 3 messages with the team."
                - "Tell ashish to be on time"

                3. Query Document:
                - "Which document had the report on diabetes?"
                - "Can you look up the discussion on project specifications in this chat and let me know the details?"

                4. Butler Query:
                - "How can I use pibot to send an email"
                - "What can you do"
                - "how can i search"

                Your task is to analyze the following user request and classify it into the correct category by providing the category number:
                
                "{user_request}"

                What is the intent of this request? Give response in JSON format with the following classes: text, intent without the ```
                Use this JSON output format only:
                
                    "text": "this is where the prompt is stored",
                    "intent": [1-4] 
                
                text - stores the prompt
                intent - stores a number between 1-4 where 1 means search web, 2 means send email, 3 means query document and 4 means butler.
                """

    response = json.loads(get_completion(prompt))
    if response['intent'] not in [1,2,3,4]:
        if 'search' in response['intent'].lower():
            return 1
        elif 'email' in response['intent'].lower():
            return 2
        elif 'document' in response['intent'].lower():
            return 3
        else:
            return 4
    
    # if response["intent"] == 1:
    #     print("PROMT:",response["text"])
    #     print("Search Web")
    # elif response["intent"] == 2:
    #     print("PROMT:",response["text"])
    #     print("Send Email")
    # elif response["intent"] == 3:
    #     print("PROMT:",response["text"])
    #     print("Query Document")
    # else:
    #     print("PROMT:",response["text"])
    #     print("Butler Query")
    
    return response['intent']



test(user_request)

