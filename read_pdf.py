#!/usr/bin/python3
import textract
import re

text = textract.process("offer_letter.pdf", method="pdfminer")


new_text = text.decode("utf-8")

# split lines into list
lines = new_text.split("\n")

print(lines)


def get_name(line):
    pattern = r"Dear [a-zA-d]+,"

    if re.match(pattern, line):
        return True
    else:
        return False


def get_salary(line):
    pattern = r"•  Gross base monthly salary: [0-9]+[,]*[0-9]+ LKR"

    if re.match(pattern, line):
        return True
    else:
        return False


filtered = list(filter(get_name, lines))

filtered1 = list(filter(get_salary, lines))

print(filtered1)
