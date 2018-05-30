# this is Class tutorial

import random
from urllib.request import urlopen
import sys

WORD_URL="http:/learncodethehardway.com/words.txt"
WORD=[]
PHRASE={
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
        "class  %%%(object):\n\tdef __init__(self,***)":
            "class %%% has-a __init__ that takes self and *** parameters"
        "class %%%(object):\n\tdef ***(self,@@@)":
            "class %%%% has-a function *** that takes self and @@@"
            "*** = %%%()":
            "set *** to an instance of class %%%"


}
