from queue import Queue

BOARD= [["a","a","a","a","a","a"],
       ["a","a","a","d","a","a"],
       ["a","a","a","f","a","a"],
       ["a","a","a","g","a","a"],
       ["a","a","a","a","a","a"],
       ]

def find_letter(target_letter:str)->list:
    found=[]
    for x,row in enumerate(BOARD):
        for y,letter in enumerate(row):
            if letter ==target_letter:
                found.append((x,y))
    return found

def is_valid(x:int,y:int)->bool:
    max_x=len(BOARD[x])
    max_y=len(BOARD)

    if x >= max_x:
        return False
    elif y >= max_y:
        return False
    elif x<0 or y<0:
        return False

    return True

def find_word(word:str)->list:
    first=word[0]
    starts=find_letter(first)
    print(starts)

    return []

def main()->None:
    searching="dfg"
    find_word(searching)

if __name__ == "__main__":
    main()
