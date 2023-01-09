
def path_list(number: int):
    answer = [number]
    while(number != 1):
        if(number % 2 == 0):
            number = number//2
        else:
            number = number*3 + 1
        answer.append(number)
    return(answer)


# testing area

if(__name__ == '__main__'):
    print(path_list(7))
