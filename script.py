# Declaring paths to files
fileReadNamePath = input('.kml file name')
fileSaveNamePath = input('name for saved file')

# Opening files
with open(fileReadNamePath, 'r', encoding='utf-8') as f:
    filelines = f.readlines()

    with open(fileSaveNamePath, 'w+', encoding='utf-8') as fCleared:
# Conditions
        for line in filelines:
            linename = line.lower().strip().startswith('<name>')
            linenumber = line.lower().strip().startswith('<phonenumber>')
            lineadress = line.lower().strip().startswith('<address>')

# Saving lines to file
            if linename:
                fCleared.write((line.strip().replace('<name>','').replace('</name>','')))
            elif lineadress:
                fCleared.write((line.strip().replace('<address>', '').replace('</address>', '')))
            elif linenumber:
                fCleared.write((line.strip().replace('<phoneNumber>', '').replace('</phoneNumber>', '')))
                fCleared.write('\n')