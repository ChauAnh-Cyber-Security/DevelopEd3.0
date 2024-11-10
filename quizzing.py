#---------------------------------------------------------------------------
# Summary: This function quizzes the user based on everything learned so far
# Choices are: MCQ, Open question, and checking student's answers
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# SETUP

from help import*

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
#---------------------------------------------------------------------------

def quizzing(llm, retriever):

    # -----------------------------------------------------------
    # AI Setup
    # -----------------------------------------------------------
    system_prompt = ("You are an instructor for the student you are teaching, you want them to do well,"
                     "You will ask them questions, DO NOT REPEAT ANY TOPIC"
                    "only provide questions from the given relevent information.\n"
                    "{context}")

    prompt = ChatPromptTemplate.from_messages([ ("system", system_prompt), ("human", "{input}")])

    chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, chain)

    # -----------------------------------------------------------
    # Execution
    # -----------------------------------------------------------

    option = input("\nWould you like to do: \n1) MCQ \n2) Open questions?\n")
    extra = input("\nAny particular topic you want to test on? Enter if none: ")

    if (option.lower() == "help"):
        help()
        return

    elif (option == "1"):
        question = "Create 10 Multiple choice questions, only provide questions from the given relevent information."
        if (extra != ""):
            question += "Focus on this topic: " + extra
        

    elif (option == "2"):
        question = "Create an open question quiz, only provide questions from the given relevent information."
        if (extra != ""):
            question += "Focus on this topic: " + extra
    
    response = rag_chain.invoke({"input": question})
    print("--------------------------------------------------")
    if (response['answer'] == ""): print("I am unable to help right now, try again")
    else: print(response['answer'])
    print("--------------------------------------------------")