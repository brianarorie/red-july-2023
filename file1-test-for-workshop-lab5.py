def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("file2-test-for-workshop-lab5.txt")

if __name__=="__main__":
    main()
