from ollama import Client

client = Client(host="127.0.0.1:11434")
text = "有哪些好用的模型推荐一下"

message = list()
message.append(
    {
        "role": "system",
        "content": "所有回答均使用中文。你是一个乐于助人的助手，提供有用的信息。"
    }
)
message.append(
    {
        "role": "user",
        "content": "用中文回答，中国队拿过世界足球冠军吗？"
    }
)

response = client.chat(
    model="llama3:latest",
    messages=message,
    stream=True
)
texts = ""
for res in response:
    print("大模型回答", "\n", res["message"])
    texts += res["message"]["content"]
texts = texts.strip()

print("大模型回答+流式输出", "\n", texts)