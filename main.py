import os 
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory

os.environ["OPENAI_API_KEY"] = "..."

path = '/Users/jediahmattison/Desktop/csv_bot/merged.csv'

llm = ChatOpenAI(temperature=0)
csv_memory = ConversationSummaryMemory(llm=llm, return_messages=True)

agent = create_csv_agent(llm=llm,
                         path = path,
                         memory = csv_memory,
                         verbose= True)


print(agent.agent.llm_chain.prompt.template)

exit_command = 'exit'
while True:
    user_input = input("Ask a question or type 'exit': ")
    if user_input == exit_command:
        print("Thank you! Goodbye!")
        break
    else:
        answer = agent.run(input = user_input)
        print(answer)
