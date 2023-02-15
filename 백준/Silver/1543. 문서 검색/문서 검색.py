import sys

doc = sys.stdin.readline().rstrip()
doc = doc.replace(sys.stdin.readline().rstrip(), '@')
print(doc.count('@'))