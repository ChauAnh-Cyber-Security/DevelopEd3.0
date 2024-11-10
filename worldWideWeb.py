#---------------------------------------------------------------------------
# Summary: This function uses the world wide web database to answer the question
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# SETUP

from help import*
from momMode import*

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
#---------------------------------------------------------------------------

def useWorldWideWeb(llm, retriever, mom_mode):

    # -----------------------------------------------------------
    # AI Setup
    # ----------------------------------------------------------- 
    if (mom_mode == 1):
        system_prompt = (momMode() + 
                        "Provide an answer to your child"
                        "{context}")
    
    else:
        system_prompt = ("You are an instructor for the student you are teaching, you want them to do well,"
                        "provide an answer for the student. Use the Internet or given data is fine.\n"
                        "{context}")

    prompt = ChatPromptTemplate.from_messages([ ("system", system_prompt), ("human", "{input}")])

    chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, chain)

    # -----------------------------------------------------------
    # Execution
    # -----------------------------------------------------------
    question = input("\nEnter your question, or type 'exit': ")
    while (question.lower() != "exit"):

        if (question.lower() == "help"):
            help()

        else:
            response = rag_chain.invoke({"input": question })
            print("--------------------------------------------------")
            if (response['answer'] == ""): print("I am unable to help right now, try again")
            else: print(response['answer'])
            print("--------------------------------------------------")

        question = input("\nEnter your question, or type 'exit': ")
