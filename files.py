import os

def list_files(path):
    print("Files in", path, ":")
    for file in os.listdir(path):
        print(file)

def create_file(path, filename):
    with open(os.path.join(path, filename), 'w') as f:
        f.write("")
    print("File", filename, "created in", path)

def delete_file(path, filename):
    os.remove(os.path.join(path, filename))
    print("File", filename, "deleted from", path)

def create_directory(path, dirname):
    os.mkdir(os.path.join(path, dirname))
    print("Directory", dirname, "created in", path)

def delete_directory(path, dirname):
    os.rmdir(os.path.join(path, dirname))
    print("Directory", dirname, "deleted from", path)

def change_directory(path):
    os.chdir(path)
    print("Changed to", path)

def main():
    current_path = os.getcwd()
    print("Current path:", current_path)

    while True:
        print("\n1. List files")
        print("2. Create file")
        print("3. Delete file")
        print("4. Create directory")
        print("5. Delete directory")
        print("6. Change directory")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_files(current_path)
        elif choice == "2":
            filename = input("Enter filename: ")
            create_file(current_path, filename)
        elif choice == "3":
            filename = input("Enter filename: ")
            delete_file(current_path, filename)
        elif choice == "4":
            dirname = input("Enter directory name: ")
            create_directory(current_path, dirname)
        elif choice == "5":
            dirname = input("Enter directory name: ")
            delete_directory(current_path, dirname)
        elif choice == "6":
            path = input("Enter path: ")
            change_directory(path)
            current_path = os.getcwd()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()