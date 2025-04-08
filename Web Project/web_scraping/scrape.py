import requests
import bs4
import re
we=requests.get('https://en.wikipedia.org/wiki/Robotics')
# pattern="<h2[^>]*>(.*?)<\/h2>"
# pattern="<h2[^>]*>([^<]*)<\/h2>"
pattern="<h2[^>]*>([^<]*)(?:(?!<\/h2>).)*<\/h2>"
headings=re.findall(pattern,str(we.content))
print(headings)