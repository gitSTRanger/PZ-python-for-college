'''
Дана строка, состоящая из русских слов, разделенных пробелами (одним или
несколькими). Вывести строку, содержащую эти же слова, разделенные одним
символом «.» (точка). В конце строки точку не ставить.
'''

string = " Слово    один слово два  "

outputString: str = ""

def changeLine(stringLine):

    corectString: str = ""

    for (index, char) in enumerate(stringLine):
        if char == " ":
            char = "."
        outputString += char


print(outputString)