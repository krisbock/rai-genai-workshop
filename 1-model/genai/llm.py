import os

from dotenv import load_dotenv
from openai.version import VERSION as OPENAI_VERSION

from promptflow.tracing import trace
from openai import AzureOpenAI

def get_client():
    if OPENAI_VERSION.startswith("0."):
        raise Exception(
            "Please upgrade your OpenAI package to version >= 1.0.0 or using the command: pip install --upgrade openai."
        )
    api_key = os.environ.get("OPENAI_API_KEY", None)
    if api_key:
        from openai import OpenAI

        return OpenAI()
    else:
        from openai import AzureOpenAI              
        return AzureOpenAI(
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
            azure_deployment=os.environ.get("AZURE_OPENAI_EVALUATION_DEPLOYMENT")
        )


@trace
def llm_tool(question: str) -> str:
    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        # load environment variables from .env file
        load_dotenv('../.env', override=True)
        print('loaded')
    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        raise Exception(
            "Please specify environment variables: OPENAI_API_KEY or AZURE_OPENAI_API_KEY"
        )

    system_message = "You are a chatbot having a conversation with a human."

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": question}
    ]    

    with AzureOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"]
    ) as client:
        response = client.chat.completions.create(
            model=os.environ.get("AZURE_OPENAI_EVALUATION_DEPLOYMENT"),
            messages=messages, temperature=0.7,
            max_tokens=800
        )
        print(f"response: {response.choices[0].message.content}")
        return {
        "answer": response.choices[0].message.content,
        #"context": str(context)
        }
    

    # messages = [{"content": question, "role": "user"}]
    # response = get_client().chat.completions.create(
    #     messages=messages,
    #     #model=deployment_name,
    #     max_tokens=int(max_tokens),
    #     temperature=float(temperature),
    #     top_p=float(top_p),
    #     n=int(n),
    # )

    # # get first element because prompt is single.
    # return response.choices[0].message.content


if __name__ == "__main__":
    result = llm_tool(
        question="Write a simple Hello, world! program that displays the greeting message.",
    )
    print(result)