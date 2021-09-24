try:
    print("Read line by line\n----------------\n")
    with open('test.txt')  as file:
        for line in file:
            print(line)

    print("Write file\n----------------\n")

    file_write = open('test.txt', 'a')
    file_write.write('testetstetette\nnoivo testeopkposdkfpasdf\n')
    file_write.close()
    
    print("Read file\n----------------\n")
    file_read = open('test.txt', 'r')
    print(file_read.read())

except Exception as error:
    print('Deu ruim', error)