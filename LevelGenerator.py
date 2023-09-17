from time import sleep
import random as rnd
import os

def Main():
    print("Welcome!\n------------\n1. Generate A Level\n2. License\n3. Close\n")

    userInput = int((input(">> ")))

    # level generation
    if userInput == 1:
        GenerateLevelParams()

    # display MIT license
    if userInput == 2:
        sleep(0.5)
        print("Copyright (c)a-glock17 2023\n------------------------\nMIT License\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n------------------------")
        sleep(10)
        Main()

    if userInput == 3:
        quit(0)

# params are initalized and instantly produces a result
def GenerateLevelParams():

    sleep(0.75)

    # index 0 is made "0" for random purposes
    LevelDifficultyList = ["0","Easy","Normal","Hard","Harder","Insane","Easy Demon","Normal Demon","Hard Demon","Insane Demon","Extreme Demon"]
    LevelLengthList = ["0","Medium (0:30)","Long (1:00)","Long (1:25)","Long (1:30)","XL (2:00)","XL (2:30)","XL (3:00)","XL (3:30)","XL (4:00+)"]
    LevelColourSchemeList = ["0","Red","Green","Orange","Yellow","Blue","Purple","Pink","Hell","Multicolour","Emerald","Black","Gray"]

    # completes actual randomization
    LevelGeneratedDifficulty = LevelDifficultyList[rnd.randint(1,10)]
    LevelGeneratedLength = LevelLengthList[rnd.randint(1,9)]
    LevelGeneratedColourScheme = LevelColourSchemeList[rnd.randint(1,12)]

    # 0 is false, 1 is true
    LevelGeneratedHasMemory = rnd.randint(0,1)
    LevelGeneratedIsDual = rnd.randint(0,1)

    if LevelGeneratedIsDual == 1:
        LevelGeneratedDualIsAsync = rnd.randint(0,1)
    else:
        LevelGeneratedDualIsAsync = 0

    sleep(0.25)
    print("Level param generation complete!")
    sleep(0.25)
    print("Printing results...")
    sleep(1)
    print("\n1. Length: " + LevelGeneratedLength)
    print("2. Difficulty: " + LevelGeneratedDifficulty)
    print("3. Colour Scheme: " + LevelGeneratedColourScheme)
    print("4. Dual:", LevelGeneratedIsDual)
    print("5. Asnyc Dual:", LevelGeneratedDualIsAsync)
    print("6. Memory:", LevelGeneratedHasMemory)
    print("\nThese are the generated params.\nIn a boolean context; 0 means false, 1 means true.\n")
    sleep(5)
    os.system('cls')
    Main()

if __name__ == "__main__":
    Main()
