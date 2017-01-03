import os
import string
from decimal import *
getcontext()

# Prompt the user for the path to a file
# Trying to open a file in read mode when the file doesn't exist will cause 
# program to crash!
# If the file doesn't exist, display an error message and quit the program
def file_data_and_path(filename):
    if os.path.isfile(filename):
       path = os.path.dirname(filename)
       with open(filename, "rU") as f:
            lines = f.readlines()
       return lines, path
    else:
       print ("Error: cannot fine "), filename
       return None, None






# Main function of the program
# Prompt user to input the path of the input file
f_name = raw_input("Path to a file to parse: ").strip()

lines, path = file_data_and_path(f_name)
if lines != None and path != None:

   # Read the file, line by line, and count how many times each letter occurs.
   # TO determine whether a string contains only letters, use isalpha().
   # Use any sort of structure to store the letter counts
   # Ignore upper/lower case of letter
   
   # Initialized index for 26 kidns of characters
   sumA = 0
   sumB = 0
   sumC = 0
   sumD = 0
   sumE = 0
   sumF = 0
   sumG = 0
   sumH = 0
   sumI = 0
   sumJ = 0
   sumK = 0
   sumL = 0
   sumM = 0
   sumN = 0
   sumO = 0
   sumP = 0
   sumQ = 0
   sumR = 0
   sumS = 0
   sumT = 0
   sumU = 0
   sumV = 0
   sumW = 0
   sumX = 0
   sumY = 0
   sumZ = 0


   for i in range(len(lines)):
       for j in range(len(lines[i])):
           if lines[i][j].lower() == 'a':
              sumA += 1
           elif lines[i][j].lower() == 'b':
              sumB += 1
           elif lines[i][j].lower() == 'c':
              sumC += 1
           elif lines[i][j].lower() == 'd':
              sumD += 1
           elif lines[i][j].lower() == 'e':
              sumE += 1
           elif lines[i][j].lower() == 'f':
              sumF += 1
           elif lines[i][j].lower() == 'g':
              sumG += 1
           elif lines[i][j].lower() == 'h':
              sumH += 1
           elif lines[i][j].lower() == 'i':
              sumI += 1
           elif lines[i][j].lower() == 'j':
              sumJ += 1
           elif lines[i][j].lower() == 'k':
              sumK += 1
           elif lines[i][j].lower() == 'l':
              sumL += 1
           elif lines[i][j].lower() == 'm':
              sumM += 1
           elif lines[i][j].lower() == 'n':
              sumN += 1
           elif lines[i][j].lower() == 'o':
              sumO += 1
           elif lines[i][j].lower() == 'p':
              sumP += 1
           elif lines[i][j].lower() == 'q':
              sumQ += 1
           elif lines[i][j].lower() == 'r':
              sumR += 1
           elif lines[i][j].lower() == 's':
              sumS += 1
           elif lines[i][j].lower() == 't':
              sumT += 1
           elif lines[i][j].lower() == 'u':
              sumU += 1
           elif lines[i][j].lower() == 'v':
              sumV += 1
           elif lines[i][j].lower() == 'w':
              sumW += 1
           elif lines[i][j].lower() == 'x':
              sumX += 1
           elif lines[i][j].lower() == 'y':
              sumY += 1
           elif lines[i][j].lower() == 'z':
              sumZ += 1
           else: 
              continue


total = 0                           # Initialize the total number of the indexes

# Calculate and display the relative frequency of each letter
total += sumA + sumB + sumC + sumD + sumE + sumF + sumG + sumH + sumI +sumJ + sumK + sumL + sumM + sumN+ sumO + sumP + sumQ + sumR + sumS + sumT+ sumU + sumV + sumW + sumX + sumY + sumZ

print sumA, total

print "A: ", Decimal(sumA)/Decimal(total)
print "B: ", Decimal(sumB)/Decimal(total)
print "C: ", Decimal(sumC)/Decimal(total)
print "D: ", Decimal(sumD)/Decimal(total)
print "E: ", Decimal(sumE)/Decimal(total)
print "F: ", Decimal(sumF)/Decimal(total)
print "G: ", Decimal(sumG)/Decimal(total)
print "H: ", Decimal(sumH)/Decimal(total)
print "I: ", Decimal(sumI)/Decimal(total)
print "J: ", Decimal(sumJ)/Decimal(total)
print "K: ", Decimal(sumK)/Decimal(total)
print "L: ", Decimal(sumL)/Decimal(total)
print "M: ", Decimal(sumM)/Decimal(total)
print "N: ", Decimal(sumN)/Decimal(total)
print "O: ", Decimal(sumO)/Decimal(total)
print "P: ", Decimal(sumP)/Decimal(total)
print "Q: ", Decimal(sumQ)/Decimal(total)
print "R: ", Decimal(sumR)/Decimal(total)
print "S: ", Decimal(sumS)/Decimal(total)
print "T: ", Decimal(sumT)/Decimal(total)
print "U: ", Decimal(sumU)/Decimal(total)
print "V: ", Decimal(sumV)/Decimal(total)
print "W: ", Decimal(sumW)/Decimal(total)
print "X: ", Decimal(sumX)/Decimal(total)
print "Y: ", Decimal(sumY)/Decimal(total)
print "Z: ", Decimal(sumZ)/Decimal(total)
