# This code returns a string which graphs a piecewise function on Desmos; it can be used for music or something idk.
counter = int(input("Enter the starting x value for your function: "))
notes = []
length = []

while True:
    cmd = int(input("""Enter an option:
(1) Give Desmos code for piecewise function.
(2) Give note\n"""))
    if cmd == 1:
        break
    elif cmd == 2:
        try:
            notes.append(int(input("Enter a note number: ")))
            length.append(int(input("Enter a length number: ")))
        except Exception as err:
            pass
    else:
        print("Invalid option, try again.")

interval = []

for i in range(len(length)):
    interval.append([counter,(counter+length[i])])
    counter = counter+length[i]

piecewise_function = "{"
for i in range(len(notes)):
    piecewise_function = piecewise_function + (f"{interval[i][0]}<=x<={interval[i][1]}:{notes[i]},")
piecewise_function = piecewise_function[:-1] + "}"

print(piecewise_function)
