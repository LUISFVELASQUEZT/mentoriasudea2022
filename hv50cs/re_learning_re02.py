import re

valid = re.compile(r"^[a2-9tjqk]{5}$")

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())



print(displaymatch(valid.match("akt5q")))  # Valid.

print(displaymatch(valid.match("akt5e")))  # Invalid.
print(displaymatch(valid.match("akt")))    # Invalid.
print(displaymatch(valid.match("727ak")))  # Valid.
