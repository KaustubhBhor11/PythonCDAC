import re
import warnings

warnings.filterwarnings('ignore')

# 1.
s = "hello world how are you hello again"
x = re.findall("a[a-z]+", s)
print(x)

# 2.
s = "hello world how are you hello again ks341, har56"
x = re.findall("[a-zA-Z]+[0-9]+", s)
print(x)

# 3. Find and substitute
x = re.sub("[0-9]+", "", s)
print(x)

string1 = "my number is 123-456-45. I live at 41150 pin code , my birth date is 12-09-20."
xc = re.findall("[0-9]{3}-[0-9]{3}-[0-9]{2}", string1)

string2 = '''my number is +67-1234567890. I live at 41150 pin code , my birth date is 12-09-20.
my number is +91-1234567890. I live at 41150 pin code , my birth date is 22-4-24.
my number is +87-1234567890. I live at 41150 pin code , my birth date is 14-10-22.'''
international_number = re.findall("\+[0-9]{2}-[0-9]{10}", string2)
print(international_number)
