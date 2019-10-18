def swap_case(s):
    swc=[i.upper()  if i.islower() else i.lower() for i in s ]
    swc=''.join(swc)
    return swc

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
