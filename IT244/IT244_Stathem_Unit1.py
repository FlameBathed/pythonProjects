# Submission by Elijah Stathem for IT244 - Python Programming taught by Md Johirul Islam

string1 = " Python was created in the 1890's by Guido van Rossum. "
string2 = " Python is maintained as an 'open source' project by a group that is called the Python Software Foundation. "
string3 = " He is affectionately known as Python's \"Benevolent Dictator for Life.\" "

"""
Going to attempt two codes with the same data set two ways resulting
in the same product to explore how and where string functions may 
be applied.
"""

concatenatedString = string1.replace("8", "9").lstrip() + string3.lstrip() + string2.lstrip()
print(concatenatedString)
"""
the code above developed after the code below and took several 
testing steps of adding functions to the line to achieve the final
result 
"""
string1 =string1.lstrip()
string2 =string2.lstrip()
string3 =string3.lstrip()
string1 =string1.replace("8", "9")
concatenatedString = string1 + string3 + string2
# print(concatenatedString)
"""
made the command above a comment to prevent double printing for
the final submission.
"""