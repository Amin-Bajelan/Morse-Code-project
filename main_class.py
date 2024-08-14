import json

while True:
    answer = input("you want encode or decode: ")

    empty_str = ""
    num = int(0)

    with open("data.json", "r") as Data:
        jason = json.load(Data)
        my_list = list(jason.keys())
        if answer == "encode" or answer == "Encode":

            text = input("Enter the text to be encoded: ")
            text = text.lower()
            list_text = [i for i in text]
            print(list_text)
            for i in list_text:
                if i == " ":
                    empty_str = empty_str + "   "
                else:
                    if num == 0:
                        empty_str = empty_str + jason[i]
                    else:
                        my_text = " " + str(jason[i])
                        empty_str = empty_str + my_text

                num = num + 1
            print(empty_str)

        elif answer == "decode" or answer == "Decode":
            with open("data.json", "r") as Data:
                text = input("Enter the text to be decoded: ")
                list_text = text.split()
                jason = json.load(Data)
                key_list = list(jason.values())
                val_list = list(jason.keys())
                empty_str = str(" ")
                num = int(0)
                for i in list_text:
                    for j in range(len(key_list)):
                        if str(i) == key_list[j]:
                            index_con = key_list.index(i)
                            if num == 0:
                                empty_str = val_list[index_con]
                            else:
                                empty_str = empty_str + val_list[index_con]
                            num = num + 1

                print(empty_str)



        else:
            print("\nPlease enter a valid number. ")

        continue_answer = input("If you wants to continue if Yes/No: ")
        if continue_answer == "No" or continue_answer == "no":
            break
