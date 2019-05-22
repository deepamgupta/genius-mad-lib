

class Story:

    #Static dictionary variable -> storiestitle
    storiesTitle = {"cidh": "Can I Have Your Daughter`s Hand?", "lovl": "LoveLetter", "0": "Exit"}


    def __init__(self,code):
        self.stories = {"cidh": self.cidh, "lovl": self.lovl}
        print("\nEnter the following details : ")
        self.stories[code]()

    def cidh(self):
        code = "cidh"
        variables = {1: "Silly Name",
                    2: "Silly Word",
                    3: "Verb(Totally Random)",
                    4: "Noun",
                    5: "Body Part(Plural)",
                    6: "Female Name",
                    7: "Verb Ending with 'ED'",
                    8: "Noun",
                    9: "Noun(Plural)",
                    10: "Verb",
                    11: "Noun",
                    12: "Occupation",
                    13: "Number",
                    14: "Verb",
                    15: "Silly Word",
                    16: "Silly Name"
                     }

        values = self.takeInput(variables)
        print("\n\t*********** " + self.storiesTitle[code] + " **********")
        print("\n\t\t\t\t\tDear Mr. and Mrs. " + values[1] + " " + values[2] + ",\n")
        print("\tWill you let me " + values[3] + " your " + values[4] + "?")
        print("\tEver since I have laid " + values[5] + " on " + values[6] + ",")
        print("\tI have " + values[7] + " madly in love with her.")
        print("\tI wish that she will be the " + values[8] + " of my " + values[9])
        print("\tand that someday we will " + values[10] + " happily ever after.")
        print("\tI have a " + values[11] + " as an " + values[12] + " that pays ")
        print("\t$"+ values[13] + " each month. I promise to " + values[14] + " ")
        print("\t"+values[6] + " with kindness and respect.")
        print("\n\t\t\t\t\t\tSincerely,")
        print("\t\t\t\t\t\t"+values[15] + " " + values[16] + "	")

    def lovl(self):
        print("In lovl")

    def takeInput(self, variables):
        values = {}
        for var in variables:
            values[var] = input(variables[var] + " : ")

        return values


