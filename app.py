import openai

# Replace this with your actual OpenAI API key
openai.api_key = "your-api-key-here"

def chat_with_gpt():
    print("ChatGPT Bot is ready! Type 'exit' to stop.\n")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers generic questions."}
    ]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or use "gpt-3.5-turbo" if you don't have GPT-4 access
                messages=messages,
                temperature=0.7
            )

            reply = response['choices'][0]['message']['content']
            messages.append({"role": "assistant", "content": reply})
            print("ChatGPT:", reply)
        
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    chat_with_gpt()
