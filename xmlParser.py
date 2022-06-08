import glob
import csv
import xml.etree.ElementTree as ET

folderPath = './xml'
# Grab list of all the files in folder
filePaths = list(glob.glob(folderPath + "/*"))

# Reorder the list of filenames
myList = []
orderedList = []

for file in filePaths:
    file = file.replace("./xml/","")
    file = file.replace(".xml","")
    myList.append(int(file))

# Sort the list
myList.sort()

for file in myList:
    # Pad numbers with leading zeros
    file = str(file).zfill(6)
    orderedList.append("./xml/" + file + ".xml")

# Output csv files with phs and num_participants
csvFile = "./phsNumParticipants.csv"

with open(csvFile, "w") as writeFile:
    fieldnames = ["filename","phs","num_participants"]
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames)

    # Store the column headers and print them in newFile
    writer.writeheader()

    for file in orderedList:
        mytree = ET.parse(file)
        myroot = mytree.getroot()
        filename = str(file)[6:]
        phs = "phs" + myroot[0].attrib["phs"].zfill(6)
        try:
            num_participants = myroot[0].attrib["num_participants"]
            writer.writerow({'filename':filename,'phs':phs,'num_participants':num_participants})
        except:
            num_participants = "Not found"
            writer.writerow({'filename':filename,'phs':phs,'num_participants':num_participants})