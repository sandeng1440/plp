
import difflib
import json
import sys


def jsonToDict() -> dict[str,str]:
    f = open('data.json','r')
    dictionary: dict = json.load(f)
    f.close()
    return dictionary

def defToList(usrInput: str,dictionary: dict[str,str]) -> tuple[list[str], str]:
    if usrInput.lower() in dictionary:
        usrInput = usrInput.lower()
        return list(dictionary[usrInput.lower()]), usrInput     
    elif usrInput.title() in dictionary:
        usrInput = usrInput.title()
        return list(dictionary[usrInput.title()]), usrInput
    elif usrInput.upper() in dictionary:
        usrInput = usrInput.upper()
        return list(dictionary[usrInput.upper()]), usrInput
    else:
        matches: list[str] = difflib.get_close_matches(usrInput, dictionary.keys())
        if matches:
            suggest = input(f'Did you mean {matches[0]}? [y/n]: ')
            if suggest.lower() == 'y':
                usrInput = matches[0]
                return list(dictionary[matches[0]]), usrInput
        else:
            print('Word not found')
            exit(1)
    return list(dictionary[usrInput]), usrInput

if __name__=='__main__':
    usrInput: str = ' '.join(sys.argv[1:])
    dictionary: dict[str,str] = jsonToDict()
    defList, usrInput = defToList(usrInput,dictionary)

    print(usrInput)
    for i in range(len(defList)):
        print(f'{i+1}) {defList[i]}')
