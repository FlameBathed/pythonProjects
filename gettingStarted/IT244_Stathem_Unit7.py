class golf:
    results = " "
    def __init__(self,hole,score,par):
        self.hole=hole
        self.score=score
        self.par=par
    def scoreEval(self,score):
        if score > self.par:
            self.results="Over Par"
        elif score < self.par:
            self.results="Under Par"
        else:
            self.results="At Par"
        print(f"You scored {self.results} for hole # {self.hole} with a par of {self.par}.")
score = 0
hole1 = golf(1,score,3)
hole2 = golf(2,score,5)
hole3 = golf(3,score,4)
holePlayed =int(input("Please enter the hole played: "))
scoreVar = int(input("Please enter your score: "))
if holePlayed == 1:
    hole1.scoreEval(scoreVar)
elif holePlayed == 2:
    hole2.scoreEval(scoreVar)
elif holePlayed == 3:
    hole3.scoreEval(scoreVar)
#elif holePlayed > 3:
 #    holeVar = golf(holePlayed,score, 4)
  #   holeVar.scoreEval(scoreVar)
else:
    print("Error. Please enter 1, 2, or 3 for the hole played.")

