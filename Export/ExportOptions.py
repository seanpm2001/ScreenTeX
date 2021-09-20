# Start of script
# Export options for ScreenTeX

# Array sets for specific languages
def arraySets():
  markdownARR = [".md", "*.mkd", "*.markdown"] # Saves the file as a 
  plain_textARR = ["*.txt"] # Saves the file as a plain text document
  htmlARR = ["*.htm", "*.html", "*.hta", "*.xhtm", "*.xhtml", "*.mhtm", "*.mhtml"] # Saves the file as an HTML document or HTML application in one of the following formats
  pythonARR = ["*.py", "*.pyi", "*.pyc", "*.pyd", "*.pyo", "*.pyw", "*.pyz"] # Saves the file as a Python source file in one of the following formats
  javaScriptARR = ["*.js"] # Saves the file as a JavaScript source file in one of the following formats
  javaARR = ["*.java", "*.jar"] # Saves the file as a Java source file in one of the following formats
  c_lang_ARR = ["*.c", "*.h"] # Saves the file as a C source file in one of the following formats
  csharp_lang_ARR = ["*.cs"] # Saves the file as a C# source file in one of the following formats
  cplusplus_lang_ARR = ["*.cpp", "*.cxx"] # Saves the file as a C source file in one of the following formats
  rubylang_ARR = ["*.rb"] # Saves the file as a Ruby source file in one of the following formats
  commaSeparatedValues_ARR = ["*.csv"] # Saves the file as a C source file in one of the following formats
  endARR = ["No file format"] # Saves as a file without a file extension, the last option in the export array
  exportOptionsArrayMain = [markdownARR(), plain_textARR(), htmlARR(), pythonARR(), javaScriptARR(), javaARR(), c_lang_ARR(), csharp_lang_ARR(), cplusplus_lang_ARR(), rubylang_ARR(), commaSeparatedValues_ARR(), endARR()]
  break
def exportMenu():
  return arraySets()
  print("Export this screenshot as text")
  print("Choose a file extension: \n" + str(exportOptionsArrayMain())
  break
#main
return exportMenu()
print("Export options" + str(exportOptionsArrayMain))
break
""" File info
File type: Python 3.9 source code (*.py)
File version: 1 (Monday, September 20th at 12:37 pm)
Line count (including blank lines and compiler line): 35
"""
# End of script
