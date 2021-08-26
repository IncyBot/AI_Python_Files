import re
import math
import nltk
from nltk.corpus import words
 
correct_spellings = words.words()
 
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.metrics.distance  import edit_distance

def extract_words(sentence):

    global extr
    global autoc
    global low_word

    extr = re.findall(r'\d+', sentence )

    ignore_words = ['a', 'the', 'if', 'br', 'and', 'of', 'to', 'is', 'are', 'he', 'she', 'my', 'you', 'it','how', 'equals', 'equal', 'with', '=', 'find'] #Ignored words, add more words with , and ""
    wordss = re.sub("[^\w]", " ",  sentence).split() # this replaces all special chars with ' '
    low_word = [w.lower() for w in wordss if w not in ignore_words]

    pattern = '[0-9]'
    low_word = [re.sub(pattern, '', i) for i in low_word]
    while("" in low_word) :
        low_word.remove("")

    autoc = []
    for entry in low_word:
        temp = [(edit_distance(entry, w),w) for w in correct_spellings if w[0]==entry[0]]
        autoc.append(sorted(temp, key = lambda val:val[0])[0][1])

    return wordss

# extr is the list that contains the numbers
# autoc is the list that contains the autocorrected sentence
# low_word contains the non - autocorrected words but it has the SI unit values

test_sentence = input("Enter your questions that relates to perimeter / area: ")
extract_words(test_sentence)

length = 0
breadth = 0
height = 0
peri_meter = 0
unit = 0
units = 0
area = 0

if "cm" or "centimeter" or "centimeters" in low_word:
    unit ="cm"
    units ="cm sq."
elif "mm" or "millimeter" or "millimeters" in low_word:
    unit = "mm"
    units ="mm sq."
elif "dm" or "decimeter" or "decimeters" in low_word:
    unit = "dm"
    units ="dm sq."
elif "m" or "meter" or "meters" in low_word:
    unit = "m"
    units ="m sq."
elif "dam" or "dekameter" or "dekameters" in low_word:
    unit = "dam"
    units ="dam sq."
elif "hm" or "hectometer" or "hectometers" in low_word:
    unit = "hm"
    units ="hm sq."
elif "km" or "kilometer" or "kilometers" in low_word:
    unit = "km"
    units ="km sq."
else:
    unit = "cm"
    units ="cm sq."

if "perimeter" in autoc:
    print("Perimeter is found in the string.")
    if "square" in autoc:
        if len(extr) == 2:
            length = float(extr[0])
            breadth = float(extr[1])
            peri_meter = 2*(length + breadth)
            print("Perimeter of the given square is: ", peri_meter, "", unit )
        elif len(extr) == 1:
            length = float(extr[0])
            peri_meter = 4*(length)
            print("Perimeter of the given square is: ", peri_meter, "", unit )
        else:
            print("Input maximum of two sides.")

    elif "rectangle" in autoc:
        if len(extr) == 2:
            length = float(extr[0])
            breadth = float(extr[1])
            peri_meter = 2*(length + breadth)
            print("Perimeter of the given rectangle is: ", peri_meter, "", unit )
        elif len(extr) == 1:
            length = float(extr[0])
            peri_meter = 4*(length)
            print("Perimeter of the given rectangle is: ", peri_meter, "", unit )
        else:
            print("Input maximum of two sides.")

    elif "triangle" in autoc:
        if len(extr) == 3:
            length = float(extr[0])
            breadth = float(extr[1])
            height = float(extr[2])
            peri_meter = length + breadth + height
            print("Perimeter of the given triangle is: ", peri_meter, "", unit )
        elif len(extr) == 2:
            print("You have entered only two sides in a triangle, so it is being taken as a right angled triangle with both parameters as sides")
            length = float(extr[0])
            breadth = float(extr[1])
            height = math.hypot(length, breadth)
            peri_meter = length + breadth + height
            print("Perimeter of the given right angled triangle is: ", peri_meter, "", unit )
        else:
            print("Input minimum of two sides.")

elif "circumference" in autoc:
    print("Circumference is found in the string.")
    if "radius" in autoc:
        length = float(extr[0])
    elif "diameter" in autoc:
        length = float(extr[0]) / 2
    peri_meter = 2 * math.pi * length
    print("Circumference of the given circle is: ", peri_meter, "", unit ) 

elif "area" in autoc:
    print("Area is found in the string.")
    if "square" in autoc:
        if len(extr) == 2:
            length = float(extr[0])
            breadth = float(extr[1])
            area = length * breadth
            print("Area of the given square is: ", area, "", units )
        elif len(extr) == 1:
            length = float(extr[0])
            area = length * length
            print("Area of the given square is: ", area, "", units )
        else:
            print("Input maximum of two sides.")

    elif "rectangle" in autoc:
        if len(extr) == 2:
            length = float(extr[0])
            breadth = float(extr[1])
            area = length * breadth
            print("Area of the given rectangle is: ", area, "", units )
        elif len(extr) == 1:
            length = float(extr[0])
            area = length * length
            print("Area of the given rectangle is: ", area, "", units )
        else:
            print("Input maximum of two sides.")

    elif "triangle" in autoc:
        if len(extr) == 3:
            length = float(extr[0])
            breadth = float(extr[1])
            height = float(extr[2])
            peri_meter = (length + breadth + height) / 2  
            area = (peri_meter*(peri_meter - length)*(peri_meter - breadth)*(peri_meter - height)) ** 0.5
            print("Area of the given triangle is: ", area, "", units )
        elif len(extr) == 2:
            length = float(extr[0])
            breadth = float(extr[1])
            area = 1/2 * length * breadth
            print("Area of the given triangle is: ", area, "", units )
        else:
            print("Input minimum of two sides.")
    
    elif "circle" or "radius" or "diameter" in autoc:
        if "radius" in autoc:
            length = float(extr[0])
        elif "diameter" in autoc:
            length = float(extr[0]) / 2
        area = length * math.pi * length
        print("Area of the given circle is: ", area, "", units )

else:
    print("Try something different or try wording it better.")
        