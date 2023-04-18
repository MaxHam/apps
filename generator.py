from data import DataLoader
from eval.chat_GPT import GPT_Model

if __name__ == "__main__":
    data_loader = DataLoader("data/HumanEval.csv")
    chat_gpt = GPT_Model()
    # same temp as in chat gpt playground
    temp = 0.7
    # same max tokens as in chat gpt playground
    max_tokens = 256

    # load human eval data
    data = data_loader.load_data()
    # get human eval data prompts
    prompts = data["prompt"].tolist()
    # query chat GPT with prompts
    responses = []
    for prompt in prompts:
        response = chat_gpt._query(
            [{"role": "user", "content": prompt}], max_tokens, temp
        )
        responses.append(response.choices[0].message.content)
        print(response.choices[0].message.content)
    # save responses to csv
    data["chat_gpt_solution"] = responses
    data.to_csv("data/HumanEval_ChatGPT.csv", index=False)
