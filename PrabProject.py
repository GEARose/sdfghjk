# G.E Ashton Rose
# 9/12/2024
# Sorry I hate writing documentation
import os
def main():
    file_name =input("Type a file name: ")
    number = 0
    reps = 0
    try:
        with open(file_name,'r') as file:
            lines=file.readlines()
            for row in lines:
                word = "X-DSPAM-Confidence"
                if row.find(word) != -1:
                    split=(row.rsplit()[1])
                    number += float(split.rstrip("/n"))
                    reps += 1

        average = number/reps
        #print(average)
        f = open("new1.txt","w")
        f.write(str(average))
        f.close()
        f = open("new1.txt","r")
        print(f.read())

    except FileNotFoundError: 
        print(f"The file '{file_name}' does not exist.") 
    except Exception as e: 
        print(f"An error occurred while trying to read the file: {e}")
main()