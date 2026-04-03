from mistralai import Mistral

client = Mistral(api_key="Vein2fnjjCLEqG3MNoJOWlxsenNeoSxp")

response = client.chat.complete(
    model="mistral-large-latest",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)



