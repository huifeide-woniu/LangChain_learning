from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

# #1.基本用法
# #LangChain封装了更上层的方法，让我们来初始化模型
# deepseek_model=init_chat_model("deepseek-chat",model_provider="deepseek",temperature=0.3)
#
# print(f"deepseek-chat{deepseek_model.invoke("以猫为主题，写一个50字左右的有趣故事").content}")
#
# #2.定义可配置模型(模型模拟器)
# config_model =init_chat_model(temperature=0.2)
# messages=[
#     SystemMessage(content="请补全一段有趣的故事，100字以内"),
#     HumanMessage(content="一只狗正在")
# ]
# # #.invoke() 的config参数才真正意义上定义了模型
# result=config_model.invoke(messages,config={"configurable":{"model":"deepseek-chat"}}).content
# print(result)


# 3.可配置的模型(默认参数)、更换参数
# 原本输出
# 精简版本
model= init_chat_model(
    model="gpt-4o-mini",
    model_provider="openai",
    temperature=0.2,
    max_tokens=500,
    configurable_fields=("model","temperature","model_provider"),
    config_prefix="first",
)
messages=[
    SystemMessage(content="请补全一段故事，100个字以内："),
    HumanMessage(content="一只猫正在__？")
]
# result = model.invoke(messages)
# print(result)

result=model.invoke(
    input=messages,
    config={
        "configurable": {
            "first_max_tokens": 10,
            "first_model": "deepseek-chat",
            "first_model_provider": "deepseek",
        }
    }
).content
print(result)
