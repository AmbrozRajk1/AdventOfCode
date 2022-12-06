import re
content = open("day5_regex.txt", encoding="utf8").read()

content = re.sub("move |^[^m]*","",content)
content = re.sub(" to | from ","|",content)
print(content)