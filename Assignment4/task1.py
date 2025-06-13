try:
    with open('sample.txt', 'r') as file:
        print('Reading file content: ')
        for i, line in enumerate(file):
            if i==0:
                print('Line 1: ',line.strip())
            elif i==1:
                print('Line 2: ',line.strip())
                break    
except FileNotFoundError:
    print(f"Error: The file '{sample.txt}' does not exist.")
file.close()