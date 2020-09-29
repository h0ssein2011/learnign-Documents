import random
import string


def random_user_id(digit=32):
    rand = ''.join([random.choice(string.ascii_letters + string.digits)
                    for n in range(digit)])
    return rand


def user_id_gen_by_user():
    n = int(input())
    ln = int(input())
    output = []
    for i in range(n):
        rand = ''.join([random.choice(string.ascii_letters +
                                      string.digits + string.punctuation) for n in range(ln)])
        output.append(rand)
    return '# '.join([j for j in output])

# print(user_id_gen_by_user())


def rgb_color_gen():
    first = random.randint(0, 255)
    second = random.randint(0, 255)
    third = random.randint(0, 255)
    return tuple([first, second, third])
# print(rgb_color_gen())


def list_of_hexa_colors(n=6):
    rand = '#' + ''.join([random.choice(string.digits +
                                        string.ascii_letters[:6]) for n in range(n)])
    return rand

# print(list_of_hexa_colors())


def list_of_rgb_colors(n=5):
    colors = []
    for i in range(n):
        first = random.randint(0, 255)
        second = random.randint(0, 255)
        third = random.randint(0, 255)

        colors.append('rgb(')
        colors.append(first)
        colors.append(second)
        colors.append(third)

    return(colors)


# print(list_of_rgb_colors())


def generate_colors(type='hexa', n=3):
    if type == 'hexa':
        list_of_hexa_colors(n)
    elif type == 'rgb':
        list_of_rgb_colors(n)
    else:
        print('wrong input format')


# print(generate_colors('rgb', 3))


def shuffle_list(ls):
    new_ls = []
    end = len(ls)-1
    for i in range(len(ls)):
        choice = ls[random.randint(0, end)]
        new_ls.append(choice)
        ls.remove(choice)
        end -= 1
    return new_ls


# print(shuffle_list([i for i in range(100)]))


def random_num(n=7):
    """ this function return n number of uniq number between 0-9

    Args:
        n (int, optional): [description]. Defaults to 7.
    """
    rands = []
    while len(rands) != n:
        num = int(random.choice(string.digits))
        if num not in rands:
            rands.append(num)


print(random_num())
