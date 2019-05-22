

class Story:

    #Static dictionary variable -> storiestitle
    storiesTitle = {"CIDH": "Can I Have Your Daughter`s Hand?", "LOVL": "LoveLetter", "0": "Exit"}


    def __init__(self,code):
        self.stories = {"CIDH": self.CIDH, "LOVL": self.LOVL}
        print("Enter the following details : ")
        self.stories[code]()

    def CIDH(self):
        varibles = {1 : "Silly Name", 2 : "Silly Word", 3 : "Verb(Totally Random)", 4: "Noun", 5: "Body Part(Plural)",
                    6: "Female Name", 7: "Verb Ending with 'ED'", 8: "Noun", 9: "Occupation", 10 : "Number",
                    11 : "Verb", 12: "Silly Word", 13:"Silly Name"}

        self.takeInput(varibles)

    def LOVL(self):
        print("In LOVL")

    def takeInput(self, variables):
        for var in variables:
            variables[var] = input(variables[var] + " : ")


