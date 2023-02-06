with open('f1.txt' ,'r') as f:
    f1 = f.readlines()
with open('f2.txt' ,'r') as f:
    f2 = f.readlines()

f1 = [int(x) for x in f1]
f2 = [int(x) for x in f2]

common_nums = [x for x in f1 if x in f2]

# Write your code above 👆
print(f1)
print(f2)
print(common_nums)

word ="what is the airspedd velocity of an unladen Swallow?"
word_list = word.split()

word_count_dict ={w:len(w) for w in word_list}
print(word_count_dict)