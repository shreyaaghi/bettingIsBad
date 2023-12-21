import json
def writeToFile(filename, contents):
  with open(filename, 'w') as f:
    f.write(createContents(contents))

def createContents(contents):
  c = ""
  c += "[\n"
  num_items = len(contents)

  for i, content in enumerate(contents):
    c += "\t{\n"
    num_keys = len(content)

    for j, (key, value) in enumerate(content.items()):
      c += f"\t\t\"{key}\": \"{value}\""
      if j < num_keys - 1:
        c += ","
      c += "\n"
    c += "\t}"

    if i < num_items - 1:
      c += ","
    c += "\n"
  c += "]\n"

  return c

def readFile(filename):
  with open(filename, 'r') as f:
    return json.load(f)