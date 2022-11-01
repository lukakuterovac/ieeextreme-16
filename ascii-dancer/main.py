class Dancer:
    def __init__(self):
        self.character = [[" ","o"," "],["/","|","\\"],["/"," ","\\"]]
        self.reversed_character = [[" ","o"," "],["/","|","\\"],["/"," ","\\"]]
        self.turned = False
    def render(self):
        for row in self.character:
            print("".join(row))
    def dance(self, text): 
        if (self.turned == False):
            if (text == "right hand to head"):
                self.character[0][0] = "("
                self.character[1][0] = " "
                self.reversed_character[0][2] = ")"
                self.reversed_character[1][2] = " "
                self.render()
            if (text == "right hand to hip"):
                self.character[0][0] = " "
                self.character[1][0] = "<"
                self.reversed_character[0][2] = " "
                self.reversed_character[1][2] = ">"
                self.render()
            if (text == "right hand to start"):
                self.character[0][0] = " "
                self.character[1][0] = "/"
                self.reversed_character[0][2] = " "
                self.reversed_character[1][2] = "\\"
                self.render()
            if (text == "right leg in"):
                self.character[2][0] = "<"
                self.reversed_character[2][2] = ">"         
                self.render()
            if (text == "right leg out"):
                self.character[2][0] = "/"
                self.reversed_character[2][2] = "\\"
                self.render()
            if (text == "left hand to head"):
                self.character[0][2] = ")"
                self.character[1][2] = " "
                self.reversed_character[0][0] = "("
                self.reversed_character[1][0] = " "
                self.render()
            if (text == "left hand to hip"):
                self.character[0][2] = " "
                self.character[1][2] = ">"
                self.reversed_character[0][0] = " "
                self.reversed_character[1][0] = "<"
                self.render()
            if (text == "left hand to start"):
                self.character[0][2] = " "
                self.character[1][2] = "\\"
                self.reversed_character[0][0] = " "
                self.reversed_character[1][0] = "/"
                self.render()
            if (text == "left leg in"):
                self.character[2][2] = ">"
                self.reversed_character[2][0] = "<"
                self.render()
            if (text == "left leg out"):
                self.character[2][2] = "\\"
                self.reversed_character[2][0]="/"
                self.render()
            if (text == "turn"):
                self.turned = not(self.turned)
                self.character, self.reversed_character = self.reversed_character, self.character
                self.render()
        else:
            if (text == "left hand to head"):
                self.character[0][0] = "("
                self.character[1][0] = " "
                self.reversed_character[0][2] = ")"
                self.reversed_character[1][2] = " "
                self.render()
            if (text == "left hand to hip"):
                self.character[0][0] = " "
                self.character[1][0] = "<"
                self.reversed_character[0][2] = " "
                self.reversed_character[1][2] = ">"
                self.render()
            if (text == "left hand to start"):
                self.character[0][0] = " "
                self.character[1][0] = "/"
                self.reversed_character[0][2] = " "
                self.reversed_character[1][2] = "\\"
                self.render()
            if (text == "left leg in"):
                self.character[2][0] = "<"
                self.reversed_character[2][2] = ">"         
                self.render()
            if (text == "left leg out"):
                self.character[2][0] = "/"
                self.reversed_character[2][2] = "\\"
                self.render()
            if (text == "right hand to head"):
                self.character[0][2] = ")"
                self.character[1][2] = " "
                self.reversed_character[0][0] = "("
                self.reversed_character[1][0] = " "
                self.render()
            if (text == "right hand to hip"):
                self.character[0][2] = " "
                self.character[1][2] = ">"
                self.reversed_character[0][0] = " "
                self.reversed_character[1][0] = "<"
                self.render()
            if (text == "right hand to start"):
                self.character[0][2] = " "
                self.character[1][2] = "\\"
                self.reversed_character[0][0] = " "
                self.reversed_character[1][0] = "/"
                self.render()
            if (text == "right leg in"):
                self.character[2][2] = ">"
                self.reversed_character[2][0] = "<"
                self.render()
            if (text == "right leg out"):
                self.character[2][2] = "\\"
                self.reversed_character[2][0]="/"
                self.render()
            if (text == "turn"):
                self.turned = not(self.turned)
                self.character, self.reversed_character = self.reversed_character, self.character
                self.render()
    def do(self, text):
        if("say" in text):
            print(text[4::])
        else:
            self.dance(text)
    
testcases = int(input())
for i in range(testcases):
    dancer = Dancer()
    inputs = int(input())
    for j in range(inputs):
        dancer.do(input())
