ls = [[1, 2, 3], [4, 7, 9]]
ls = [row for num in ls for row in num]
print(ls)


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negs = [i for i in numbers if i <= 0]
print(negs)


list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [r for n in [row for num in list_of_lists for row in num] for r in n]

print(flatten)


ls = [(i, 1, i*1, i**2, i**3, i**4, i**5) for i in range(10)]
print(ls)

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat1 = [row for num in countries for row in num]
flat2 = [row for num in flat1 for row in num]
print(flat2)

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat1 = [row for num in countries for row in num]
ls = [{'country': c[0], 'city':c[1]} for c in flat1]
print(ls)


names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
flat1 = [row for num in names for row in num]
ls = [c[0]+' '+c[1] for c in flat1]
print(ls)


""" y = ax + b """
def slope(x, y, b): return (y-b) / x


def intercept(y, a, x): return y - (a * x)


print(slope(3, 2, 5))
print(intercept(3, 2, 1))
