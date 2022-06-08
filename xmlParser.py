import glob
import csv
import xml.etree.ElementTree as ET

# Folder with files to iterate through
folderPath = './xml'

# Return list of all the files in folder
filePaths = list(glob.glob(folderPath + "/*"))

# Reorder the list of filenames
myList = []
orderedList = []

# Extract phs numbers from all the files so they can be sorted
for file in filePaths:
    file = file.replace("./xml/","")
    file = file.replace(".xml","")
    myList.append(int(file))

# Sort the list of integers
myList.sort()

# Add extension and path information
for file in myList:
    # Pad numbers with leading zeros
    file = str(file).zfill(6)
    orderedList.append("./xml/" + file + ".xml")

# Output csv file
csvFile = "./phsNumParticipants.csv"

with open(csvFile, "w") as writeFile:
    fieldnames = ["filename","phs","num_participants"]
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames)

    writer.writeheader()

    # Parse phs and num_participants from each file
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