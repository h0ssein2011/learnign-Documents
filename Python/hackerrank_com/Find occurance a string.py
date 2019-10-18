def count_substring(string, sub_string):

    count=0
    for i in range(len(string)):
        s=''
        s=string[i:i+len(sub_string)]
        if s==sub_string:
            count+=1

    return(count)


    return(string.count(sub_string))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
