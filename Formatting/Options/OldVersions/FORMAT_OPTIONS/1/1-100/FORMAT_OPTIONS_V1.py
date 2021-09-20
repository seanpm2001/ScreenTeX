# Start of script
# Text formatting options for ScreenTeX

def end():
  print ("Program has ended")
  x = int(0 / x)
  print (x) # This will either cause a forkbomb or crash the program via syntax error, it is in place until I can find a proper way of qutting the program
  return end()
# Boolean section
richTextBool = bool("true")
textColorBool = bool("false")
print ("Text formatting options for screenTeX")
print ("Current layout:")
print ("Rich Text: " + str(richTextBool) + " ID: RT")
print ("Colored Text: " + str(textColorBool) + " ID: CT")
changeCC = str(input("Change an option by inputing one of the provided codes"))
changeCC == changeCC.upper()
if (changeCC == "RT"):
  print ("What would you like to change this option to:")
  print ("True | False")
  changeRT = str(input(">>>"))
  changeRT == changeRT.upper()
  if (changeRT == "TRUE"):
    richTextBool = bool("true")
  elif (changeRT == "FALSE"):
    richTextBool = bool("false")
  else:
    print ("Invalid input, please enter either 'true' or 'false'")
elif (changeCC = "CT"):
  print ("What would you like to change this option to:")
  print ("True | False")
  changeCT = str(input(">>>"))
  changeCT == changeCT.upper()
  if (changeCT == "TRUE"):
    textColorBool = bool("true")
  elif (changeCT == "FALSE"):
    textColorBool = bool("false")
  else:
    print ("Invalid input, please enter either 'true' or 'false'")
else:
  print ("Invalid input, please enter a valid ID.")
noMore = input("The program would like to quit. Press [ENTER] to exit the formatting options module")
break
end()
""" File info
File type: Python 3.9 source code (*.py)
File version: 1 (Monday, September 20th at 1:14 pm)
Line count (including blank lines and compiler line): 51
"""
# End of script
