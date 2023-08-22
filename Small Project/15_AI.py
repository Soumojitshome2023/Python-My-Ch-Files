#-------------------------------------------------------------------------------
# Name:        Small AI Project
# Purpose:
#
# Author:      Soumojit Shome
#
# Created:     19 February 2023
# Copyright:   (c) Soumojit Shome
#
# Note :       Data store in qna.txt file
#------------------------------------------------------------------------------- 
print("\n********** WELCOME **********\n")
print(">>> Hello, enter q to quit \n")

while(True):
    qna = open("qna.txt","r")
    question_input = input(">>> Ask anything : ")

    if(question_input=="q"):
        break
    else:

        while(True):
            try:
                f = qna.readline()
                question,ans= f.split(" : ")
                if(question==question_input):
                    print(f">>> {ans}")
                    qna.close()
                    break
            except:
                print(">>> Sorry Answer not found")
                qna.close()

                ans_input = input(">>> Pls enter the answer, if mistake then enter q : ") 
                
                if(ans_input=="q"):
                    break
                else:
                    qna = open("qna.txt","a")
                    qna.write(f"\n{question_input} : {ans_input}")
                    qna.close()
                    print(">>> Thanks for your answer\n")
                    break

qna.close()

print("\n********** THANKS **********\n")
