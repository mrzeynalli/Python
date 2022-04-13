from pathlib import Path
import os


def text_file_reader():

    while True:

        directory_input = input("Please enter the folder path: ")

        docs_path = Path(r'%s' % directory_input)

        if not docs_path.exists():
            print("ERROR!")
            print("\nPlease put a valid path directory:\n")
            continue
        else:

            list_text_files = []

            for file in os.listdir(docs_path):
                if file[-4:] == '.txt':
                    list_text_files.append(file)

            dict_of_texts = {}

            for i in range(0, len(list_text_files)):
                dict_of_texts[i] = list_text_files[i]

            input_message = ""

            for i, a in dict_of_texts.items():
                if i != len(dict_of_texts):
                    input_message = input_message + str(i + 1) + " " + str(a) + "\n"
                else:
                    input_message = input_message + str(i + 1) + " " + str(a)

            while True:
                print("The texts files the speicifed folder contains are given below:")
                print(input_message)
                value_chosen = input("Enter the number pointing the text file you'd like to read: ")

                if not value_chosen.isnumeric():
                    print("\nPlease input a numeric value.\n")
                    continue
                elif int(value_chosen) < 1:
                    print("\nPlease choose a positive number.\n")
                    continue
                elif int(value_chosen) > len(list_text_files):
                    print("\nPlease choose a valid number.\n")
                    continue
                else:
                    print("\nThe ingredeient of a file named " + dict_of_texts[int(value_chosen) - 1] + "is given "
                                                                                                        "below:\n")
                    print(open(docs_path / dict_of_texts[int(value_chosen) - 1]).read())
                    break

            while True:
                doing_again = input("\nDo you want to run again? (Y/N) ")
                if doing_again.upper() == "Y":
                    print("\n")
                    break
                elif doing_again.upper() == "N":
                    print("\n")
                    break
                else:
                    print("ERROR! Please choose either Y (Yes) or N (No): ")
                    continue

            if doing_again.upper() == "N":
                break


text_file_reader()
