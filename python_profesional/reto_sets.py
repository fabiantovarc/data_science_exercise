def remove_duplicate(lista):
    return list(set(lista))

def run():
    list_A = [55,11,65,66,66,65,55,21,35]
    print(remove_duplicate(list_A))

if __name__ == '__main__':
    run()


