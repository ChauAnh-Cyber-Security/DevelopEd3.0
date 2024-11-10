from uploadNote import*
from answerQuestion import*
from quizzing import*
from worldWideWeb import*
from summarizeNotes import*
from getLlmRetriever import*

def main():
    #setup
    llm, retriever = getLlmRetriever()
    mom_mode = 0

    #welcome message
    print("\nHello! I am your Study Buddy. I am 3 days old, so I still have a lot of flaws - forgive me!")
    print("At anytime you have problems with my answer, type 'help' to see some hints from my parents (they will cry but woe oh woe)")
    print("Let's get started!")

    while(1):
        user_decision = input("\n~~~~~~ MAIN MENU ~~~~~~\n"
                        "1) Update Knowledge\n"
                        "2) Ask questions based on given knowledge\n"
                        "3) Ask me anything! \n       P/S: The answer can come from the Internet or the given knowledge\n"
                        "4) Create a quiz from given knowledge\n"
                        "5) Summarize my notes about a topic\n"
                        "6) Switch mode\n"
                        "9) Exit\n"
                        "Enter Selection: ")


        if (user_decision == "1"):
            llm, retriever = uploadNote() #update new llm and retriever as there are new data

        elif(user_decision == "2"):
            answerQuestion(llm, retriever, mom_mode)

        elif(user_decision == "3"):
            useWorldWideWeb(llm, retriever, mom_mode)

        elif (user_decision == "4"):
            quizzing(llm, retriever) #Quizzing won't support mom mode the question might get mixed with "mom commentaries"

        elif (user_decision == "5"):
            summarizeNotes(llm, retriever, mom_mode)

        elif (user_decision == "6"):
            if (mom_mode == 0):
                mom_mode = 1
                print("\nSwitched to Asian Mom Mode")
            else:
                mom_mode = 0
                print("\nSwitched to Educative mode")

        elif (user_decision == "9"):
            print("\n~~~~~ That was fun, come again soon okay! Bye byee! ~~~~~\n")
            break

        elif (user_decision.lower() == "help"):
            print("\nSelect one of the activity by typing their number")
        
        else:
            print("\nThat was not one of the given options, try again!")

    return

if __name__ == "__main__":
   main()
