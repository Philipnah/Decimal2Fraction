print("\nUse . as comma")
inputString = input("Enter a decimal number: ")

DecimalNumbers = inputString.split(".")


def GCF(num, divider):
	while num != divider:
		if num < divider:
			divider = divider - num
		elif num > divider:
			num = num - divider
	return num


# The following variable is the number raised to the power of ten times the amount of decimal numbers in the original number
powerUp = float(inputString)*10**len(DecimalNumbers[1])
powerUpDivider = 10**len(DecimalNumbers[1])



cal = powerUp/GCF(powerUp, powerUpDivider)
cal2 = powerUpDivider/GCF(powerUp, powerUpDivider)

# Start: spacing, turn float to string the chop off ".0"
print("\n" + str(cal).split(".")[0] + "/" + str(cal2).split(".")[0])