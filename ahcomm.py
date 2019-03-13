import sys

fin = sys.argv[1]
	
## Extract filename and extension from fin
title, ext = fin.split(".")

author = input("Enter author of file: ")
purpose = input("Enter purpose of file: ")
date = input("Enter the version date of file: ")

f = open(fin, "r")
code = f.read()
f.close()

f = open(fin, "w")

if (ext == "m"): ## MATLAB file 
	csymb = "%"
elif (ext == "c"): ## C file
	csymb = "//"
elif (ext == "py"): ## Python file
	csymb = "##"

tot_length = 71
f.write(csymb + (tot_length - 1) * '*' + '\n')
f.write(csymb + (tot_length - 3) * ' ' + "**\n")

title_str = " Title: " + title + "." + ext
author_str =  " Author: " + author

str_list = [title_str, author_str]

purpose_words = purpose.split(" ")



date_str = " Date: " + date

for string in str_list:
	f.write(csymb + string + (tot_length - len(string) - 3) * ' ' + "**\n")
	f.write(csymb + (tot_length - 3) * ' ' + "**\n")

f.write(csymb + (tot_length - 1) * '*' + '\n')

f.write(code)
f.close()
