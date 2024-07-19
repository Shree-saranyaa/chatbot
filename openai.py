import openai

openai.api_key = "sk-proj-wNBERqiTMexyRNVOH405T3BlbkFJQcmL6LkXziYeQ2neKrTd "

def chat_with_gpt(prompt):
    response   = openai.ChatCompletion.create(
    model ="gpt-3.5-turbo",
    message = [{"role":"user","content": prompt}]
    )
     
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Ask tour doubts?: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("chatbot: ",response )
        
        