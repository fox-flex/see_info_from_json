"""
module for see info from json file
"""
import json


def read_file_and_see_it_info(path: str):
    """
    this function read json file and give instructions to user how to see,
    what actually is in that file
    """
    with open(path) as file:
        data = json.load(file)
    data_c = data

    print('Let\'s know what is in our json file')
    # typ = type(data)
    # print(isinstance(data, dict))
    # print(type(typ))
    while True:
        if isinstance(data, list):
            print(f'Now we are in some list.\n'
                  f'Which position do you want to see?\n'
                  f'There are {len(data)} positions\n'
                  f'Type of vals in each positions are next:')
            for i, val in enumerate(data):
                print('{:3d} - '.format(i + 1), end='')
                print(type(val))
            num = input('Print numb of position, which val you want to see: ')
            bul = True
            while bul:
                try:
                    num = int(num) - 1
                    data = data[num]
                    bul = False
                except ValueError:
                    print('Wrong number. Try again!')
                    num = input('Print number of position: ')
                except IndexError:
                    print('Wrong number. Try again!')
                    num = input('Print number of position: ')
        elif isinstance(data, dict):
            print('Now we are in some dict.')
            print(f'Which position do you want to see? There are {len(data)} '
                  f'positions')
            keys = list(data.keys())
            print(f'And keywords are next:')
            for i, val in enumerate(keys):
                print('{:3d} - {:s}'.format(i+1, val))
            key = input('Print num of keyword, which val you want to see: ')
            bul = True
            while bul:
                try:
                    key = int(key) - 1
                    data = data[keys[key]]
                    bul = False
                except ValueError:
                    print('Wrong num. Try again!')
                    key = input('Print num of keyword: ')
                except IndexError:
                    print('Wrong num. Try again!')
                    key = input('Print num of keyword: ')
                except KeyError:
                    print('Wrong num. Try again!')
                    key = input('Print num of keyword: ')
        else:
            print(f'The next value is: {data}')
            print('It\'s the end of search. If you want to search one more '
                  'time press Enter, if not type any symbol: ', end='')
            if input() == '':
                data = data_c
            else:
                break


if __name__ == '__main__':
    path = './examples_json/kved.json'
    read_file_and_see_it_info(path)
