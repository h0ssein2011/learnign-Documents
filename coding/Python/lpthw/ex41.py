# this is Class tutorial

import random
from urllib.request import urlopen
import sys

WORD_URL="http:/learncodethehardway.com/words.txt"
WORDS=[]
PHRASE={
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
        "class  %%%(object):\n\tdef __init__(self,***)":
            "class %%% has-a __init__ that takes self and *** params.",
        "class %%%(object):\n\t def ***(self,@@@)":
            "class %%%% has-a function *** that takes self and @@@",
            "*** = %%%()":
            "set *** to an instance of class %%%",
            "***.***@@@":
            "From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases print_first_word
if len(sys.argv)== 2 and sys.argv[1]=="English":
    PHRASE_FIRST=True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(Str(word.strip(),encoding='utf-8'))

def convert(snippets,phrase):
    class_names=[w.capitalize() for w in
    random.sample(WORDS,snippets.count("%%%"))]

    other_names=random.sample(WORDS ,snippets.count("***"))
    result=[]
    param_names=[]

    for i in range(0,snippets.count("@@@")):
        param_count=random.randint(1,3)
        param_names.append(", ".join(
        random.sample(WORDS,param_count)))

    for sentence in snippet,phrase:
        result=sentence[:]

        #fake class name
        for word in class_names:
            result=result.replace("%%%",word,1)

        #fake class name
        for word in other_names:
            result=result.replace("***",word,1)

                    #fake parameter list
        for word in param_names:
            result=result.replace("@@@",word,1)

            results.append(result)

    return results

# KEEP GOING UNTIL  they hit CTR-D
try:
    while True:
        snippets=list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets :
            phrase=PHRASE[snippet]
            question,answer=convert(snippet,phrase)
            if PHRASE_FIRST:
                question,answer=answer,question

            print(question)

            input(">")
            print("ANSWER:{}\n\n".format(answer))
except EOFError:
    print("\nBye")
