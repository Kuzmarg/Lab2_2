"""Task2"""
import json
import twitter1
import twitter2

def navigate(data):
    """
    The function that enables navigation through the objects
    Args:
        data (dict): dictionary with data in the present
        state
    """
    while True:
        print('Possible ways -', list(data))
        print()
        obj = input('Choose the way by inserting the position in the list (from 0)\
or use -1 to return: ')
        while not obj.isnumeric() or int(obj) not in range(len(list(data))):
            if obj == '-1':
                return False
            obj = input('Wrong option, choose again: ')
            print()
        obj = list(data)[int(obj)]

        if isinstance(data, dict) and isinstance(data[obj],list):
            print('The choosen object is a list.')
            navigate(data[obj])

        elif isinstance(data, list) and isinstance(obj,list):
            print('The choosen object is a list.')
            navigate(obj)

        elif isinstance(data, dict) and isinstance(data[obj],dict):
            print('The choosen object is a dictionary.')
            navigate(data[obj])

        elif isinstance(data, list) and isinstance(obj,dict):
            print('The choosen object is a dictionary.')
            navigate(obj)

        else:
            if isinstance(data, list):
                print(obj)
                print()
            if isinstance(data,dict):
                print(data[obj])
                print()

def main():
    """
    The main function
    """
    while True:
        print('Should I get the timeline of a user or the friends? 1/2')
        check = input()
        while check not in ['1','2']:
            check = input('Wrong data. Should I get the timeline of a user or the friends? 1/2')
        if check == '1':
            data = twitter1.get_data()
        else:
            data = twitter2.get_data()

        data = json.loads(data)
        navigate(data)

if __name__=='__main__':
    main()
