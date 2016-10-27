#!/usr/bin/python
f1 = "tr-heaploop.ref"
f2 = "tr-matmul.ref"

temp = []   # temp list to hold address/char pairs on each line
i = {}      # dict to hold instruction page/num times accessed pairs
d = {}      # dict to hold data page/num times accessed pairs

print("\nExercise 8: Analysis Program")
print("Enter a file name ('q' to quit): ", end="")
filename = input()

while filename != 'q':
    with open(filename, "r") as f:
        for line in f:
            temp = (line.strip()).split(",")
            temp[0] = temp[0][:-3]

            if temp[1] == 'I':
                if temp[0] in i:
                    i[temp[0]] += 1
                else:
                    i[temp[0]] = 0
            elif temp[1] in ('S', 'L', 'M'):
                if temp[0] in d:
                    d[temp[0]] += 1
                else:
                    d[temp[0]] = 0

        print("\nInstructions:")
        for key in i:
            print(key, i[key])

        print("\nData:")
        for key in d:
            print(key, d[key])

        # find most used page in instruction and data
        max_ipage = max(i.keys(), key=(lambda key: i[key]))
        max_dpage = max(d.keys(), key=(lambda key: d[key]))

        # print info required for readme.txt
        print()
        print("# of instruction pages: " + str(len(i.keys())))
        print("# of data pages: \t\t" + str(len(d.keys())))
        print("most accessed i-page: \t" + max_ipage + " " + str(i[max_ipage]))
        print("most accessed d-page: \t" + max_dpage + " " + str(d[max_dpage]))

    print("\nEnter a file name ('q' to quit): ", end="")
    filename = input()
