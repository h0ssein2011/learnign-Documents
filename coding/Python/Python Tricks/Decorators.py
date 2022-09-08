

def wrapp_an_item(item):
    # print(f'We are ready to wrap {item}')
    def wrapp_it():
        return f'the {item} is wrapped successfully'

    return wrapp_it


@wrapp_an_item
def my_gift():
    return 'This is my gift'

print(my_gift())