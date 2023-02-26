# Nidhi is preparing for her examination, and she has so many topics to cover. She decided to study each topic properly, and then revise each topic in reverse order to finalize it. To make her work easy, write a python program and create a Stack class ( stack data structure ) where she can add the topic that she is learning for the first time. After completing all the topics she can check the peak value of the stack to check which topic she has to revise. After revising the topic she can pop the element from the stack. Once the stack becomes empty, it indicates she is ready for her examination.


class Stack:

    def __init__(self):
        self.topics = []
    

    #push
    def push(self, element):
        self.topics.append(element)

    #pop
    def pop(self):
        return self.topics.pop()

    #peek
    def peek(self):
        return self.topics[-1]
    
    #display
    def display(self):
        return self.topics
    
    def len(self):
        return len(self.topics)


#initalize
studyTopics = Stack()

#user input for topics to study
while True:
    topic = input("What topic do you want to study: ")
    studyTopics.push(topic)

    stop_loop = input("Is that all the topics you want to study? Y/N")

    if stop_loop.upper() == "Y":
        break

#spacing
print()
print()

#User input for 
while True:
    if studyTopics.len() == 0:
        print("Good job you studied all the topics for the test.")
        break

    study = input(f"Have you revised {studyTopics.peek()}")

    if study.upper() == "Y":
        studyTopics.pop()
    
    else:
        print(f"Study {studyTopics.peek()}.")
        studyTopics.pop()