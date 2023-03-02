import openai
import csv
import os

openai.api_key = ""  # put your openai API key here, apply for a key in https://platform.openai.com/account/api-keys
user_name = ""  # put your name here
def get_response(chat):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat
    )
    return response["choices"][0]["message"]["content"]

def main():
    print(f"Welcome to the ChatGPT command line tool!\n")
    history = [{"role": "system", "content": f"You are a helpful assistant."}]

    while True:
        user_input = input("> {} : ".format(user_name)).strip()
        print()
        if user_input == "q":
            history.append({"role": "user", "content": "summarize the entire conversation in under 4 words"})
            with open(f'chat_history/{get_response(history[1:])}csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["role", "content"])
                writer.writeheader()
                for row in history[1:-1]:
                    writer.writerow(row)
            break
        history.append({"role": "user", "content": user_input})
        rsp_content = get_response(history)
        print(f'> ChatGPT: {rsp_content}\n')
        history.append({"role": "assistant", "content": rsp_content})

if __name__ == "__main__":
    main()
