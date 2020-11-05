from nltk.stem.snowball import SnowballStemmer
from nltk import WordNetLemmatizer
from sklearn.datasets import load_diabetes
import numpy as np
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for counry in countries:
    print(counry)

for name in names:
    print(name)


def make_upper(x):
    return [i.upper() for i in x]


def make_upper_ls(function, *args):

    upper = function(*args)
    return upper


print(make_upper_ls(make_upper, countries))


feature_dict = {}
# calculate mean
feature_dict['mean'] = np.mean(x)


ls = [2, 3, 4, 5]
print(ls[:-2])

X = load_diabetes['date']
y = load_diabetes['']


def test1(x):
    return x


def test2(x):
    print(x)


w1 = test1(33)
w2 = test2(33)
print(w1 is None)
print(w2 is None)


class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "actor":
            print(self.name, "shoots film")
        elif self.occupation == "tenis player":
            print(self.name, "plays tennis")

    def speak(self):
        print(self.name, "says hello, how are you?")


Tom = Human(name="Tom", occupation="actor")
Tom.do_work()
Tom.speak()

Hossein = Human(name="Hossein", occupation="tenis player")
Hossein.do_work()
Hossein.speak()


class animals:
    # properties
    def __init__(self, name, color, legs):
        self.name = name
        self.color = color
        self.product = product
    # methods

    def benefit(self):
        if self.name = "lion":
            print(self.name, "pray other animals")
        elif self.name = "sheep":
            print(self.name, "produce meat for human")

    def walk(self):
        if self.name = "lion":
            print(self.name, "can walk")
        elif self.name


class vehicle:
    def usage(self):
        print("the main purpose is transportaion")


class Car(vehicle):
    def general_usage(self):
        print("the main purpose is commuting")


class motorcycle(vehicle):
    def general_usage(self):
        print("the main purpose is racing")


c = Car()
c.usage()
c.general_usage()
m = motorcycle()
m.usage()
m.general_usage()


# multiple inheritance
class Father:
    def skills(self):
        print("gardening and programming")


class Mother:
    def skills(self):
        print("I enjoy art")


class child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I enjoy sport")


c = child()
c.skills()


class Remote_Control():

    def __init__(self):
        self.channel = ["CNN", "BBC", "IRIB", "Manoto"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.channel[self.index]

    def __prev__(self):
        self.index -= 1
        return self.channel[self.index]


r = Remote_Control()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(prev(itr))


lemetizer = WordNetLemmatizer()
stemmer = SnowballStemmer("English")

corpus = ["fish", "fishes", "fishing"]

for word in corpus:
    print(f'word :{word}')
    print(f'stemmed :{stemmer.stem(word)}')
    print(f'lema :{lemetizer.lemetize(word)}')
