
def main():

    def charCount(words):
        countDict ={}
        loweredString = words.lower()
        print(loweredString)
        print(countDict)

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        tempString = str(file_contents)
        words = tempString.split()
        #counter = 0
        #for i in words:
        #    counter += 1
        #print(counter)




charCount(words)

main()
