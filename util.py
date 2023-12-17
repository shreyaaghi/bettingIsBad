def writeToFile(filename, contents):
  with open(filename, 'w') as f:
    f.write('[\n')
    for item in contents:
      f.write('\t{\n')
      for key in item:
        f.write(f'\t\t\'{key}\': \'{item[key]}\',\n')
      f.write('\t},\n')
    f.write(']')

def createContents(contents):
  print(contents)