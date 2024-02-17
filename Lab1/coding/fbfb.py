
def fb2fb_converter(signal):
	groups = []
	cur = ""
	for i, el in enumerate(signal):
		cur+=(str(el))
		if not((i+1)%4):
			match cur:
				case "0000":
					groups += [1,1,1,1,0]
				case "0001":
					groups += [0,1,0,0,1]
				case "0010":
					groups += [1,0,1,0,0]
				case "0011":
					groups += [1,0,1,0,1]
				case "0100":
					groups += [0,1,0,1,0]
				case "0101":
					groups += [0,1,0,1,1]
				case "0110":
					groups += [0,1,1,1,0]
				case "0111":
					groups += [0,1,1,1,1]
				case "1000":
					groups += [1,0,0,1,0]
				case "1001":
					groups += [1,0,0,1,1]
				case "1010":
					groups += [1,0,1,1,0]
				case "1011":
					groups += [1,0,1,1,1]
				case "1100":
					groups += [1,1,0,1,0]
				case "1101":
					groups += [1,1,0,1,1]
				case "1110":
					groups += [1,1,1,0,0]
				case "1111":
					groups += [1,1,1,0,1]
			cur = ""
	print(groups)
	print("New size is", len(groups), "Bits")
	print("Redundancy is 25%")
	return groups
