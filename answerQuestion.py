#---------------------------------------------------------------------------
# Summary: This function answer user questions based on the existing data
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# SETUP

from help import*
from momMode import*

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
#---------------------------------------------------------------------------

def answerQuestion(llm, retriever, mom_mode):

    # -----------------------------------------------------------
    # AI Setup
    # -----------------------------------------------------------
    if (mom_mode == 1):
        system_prompt = (momMode() + 
                        "only provide answers from the relevent information on the data given."
                        "If you don't know the answer, must say that you don't know, don't try to make up an answer.\n"
                        "{context}")

    else:
        system_prompt = ("You are an instructor for the student you are teaching, you want them to do well,"
                        "only provide answers from the relevent information on the data given."
                        "If you don't know the answer, must say that you don't know, don't try to make up an answer.\n"
                        "{context}")

    prompt = ChatPromptTemplate.from_messages([ ("system", system_prompt), ("human", "{input}")])

    chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, chain)

    # -----------------------------------------------------------
    # Execution
    # -----------------------------------------------------------

    question = input("\nEnter your question, or type 'exit': ") + " only provide an answer from the relevent information on the data given."
    while (question.lower() != "exit"):
        
        if (question.lower() == "help"):
            help()

        else:
            response = rag_chain.invoke({"input": question})
            print("--------------------------------------------------")
            if (response['answer'] == ""): print("Sorry, I am unable to help right now, try again")
            else: print(response['answer'])
            print("--------------------------------------------------")
        
        question = input("\nEnter your question, or type 'exit': ")