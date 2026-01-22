text="PythonProgramming"

#string indexing
print("first character:",text[0])
print("fifth character:",text[5])
print("last character:",text[-1])
print("second last character:",text[-2])

#string slicing
print("first 6 characters:",text[0:6])
print("substring:",text[6:-1])
print("index 2 to 8:",text[2:9])
print("without first character:",text[1:])
print("without last character:",text[:-1])

#step slicing
print("every second character:",text[::2])
print("reverse order:",text[::-1])

#length of string
print("length of string:",len(text))