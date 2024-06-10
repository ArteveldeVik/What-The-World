import os
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage

#Langchain OpenAi
from langchain_openai import ChatOpenAI

#Langchain Agent
from langchain.agents import create_openai_functions_agent, AgentExecutor

#Create the conversation
def generate_conversation(detections): 
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API")
    llm = ChatOpenAI(temperature = 0.5, openai_api_key = openai_api_key, model_name="gpt-3.5-turbo", max_tokens=50)

    message = [
        SystemMessage(content = "You are an intelligent assistant that describes a museum scene with the given list of objects. You make sure you include every object in the scene."),
        HumanMessage(content = f"List of objects in the scene:{detections}"),
    ]

    #Invoke the Large Language Model
    result = llm.invoke(message)
    return result.content



# #Create a prompt
# prompt = hub.pull("hwchase17/openai-functions-agent")


# #1. Link the wikipedia superpowers to openai functions
# agent = create_openai_functions_agent(llm, tools, prompt)

# #2. Create an agent executer
# agent_executor = AgentExecutor(agent = agent, tools=tools, verbose=True)

# #3. Execute the agent
# result = agent_executor.invoke({"input": "Making a movie from paper."})

#4. Print the result
# print(result)