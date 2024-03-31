
#miscleanous codes only

chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    genai.configure(api_key=apikey)
    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
    chatStr += f"Supriyo: {query}\n Assistant: "
    response = model.generate_content(query)
    
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



    
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Gemini/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text) 




        

        elif "Using artificial intelligence".lower() or "Using AI".lower() in query.lower():
            ai(prompt=query)

        elif "Assistant Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
