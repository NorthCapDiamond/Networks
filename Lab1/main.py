from code_methods.ami import *
from code_methods.manchester_diff import *
from code_methods.manchester_two import *
from code_methods.nrz import *
from code_methods.rz import *
from coding.fbfb import *
from coding.to_hex import *
from coding.scrambling import *


while True:
	try:
		file = open(input("Enter filename!\n"))
		break
	except: 
		print("No such File exceprion... Try again")


#file = open("signals", "r")



my_signals = [int(x) for x in file.read().split(" ")]
tmp = my_signals

print("Signals:")
print(*my_signals)

print("Length:", str(len(my_signals)))
C = int(input("Enter C value (MBits/s)\n"))
#C = 100

command = input("Enter your command or help\n")

while(command!="exit"):
	match command:
		case "help":
			print("Type the command from this list:\n")
			print("nrz")
			print("manchester_diff")
			print("manchester_two")
			print("rz")
			print("ami")
			print("exit")
			print("4b5b")
			print("restore")
			print("scrambling")
			
		case "nrz":
			nrz(my_signals, C)

		case "manchester_diff":
			manchester_diff(my_signals, C)

		case "manchester_two":
			manchester_two(my_signals, C)

		case "rz":
			rz(my_signals, C)

		case "ami":
			ami(my_signals, C)

		case "4b5b":
			my_signals = fb2fb_converter(my_signals)

		case "restore":
			my_signals = tmp

		case "to_hex":
			two2hex(my_signals)

		case "scrambling":
			my_signals = scramble(my_signals, 7, 9)



	command = input("Enter your command or help\n")
print("Bye!!")
