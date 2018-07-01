import datetime

class TrainingMachine:

    def __init__(self, filepath):

        self.trainedLeaders, self.columnCodes = self.initializeFromFile(filepath)

    def initializeFromFile(self, path, rowstoskip=7):

        try:
            file = open(path)

        except(FileNotFoundError):
            print("File Not Found, Exiting")
            exit(1)

        columnDictionary = {}

        index = 0

        for line in file:

            if index <= rowstoskip:
                # Skip the empty rows prior to the header row
                index += 1
                continue

            elif index == rowstoskip + 1:
                # this creates the dictionary using the codes from the header row in the csv

                listOfDictionaryColumnCodes = line.split(",")
                print(listOfDictionaryColumnCodes)

                for entry in listOfDictionaryColumnCodes:
                    columnDictionary[entry] = []

                index += 1

            else:
                # This is the main case, which loads all of the data into the dictionary
                listOfLineElements = line.split(",")

                # print(len(listOfLineElements))
                # print(len(listOfDictionaryColumnCodes))
                # print(listOfDictionaryColumnCodes)
                # print(listOfLineElements)

                for i in range(len(listOfLineElements)):
                    columnCode = listOfDictionaryColumnCodes[i]
                    lineElement = listOfLineElements[i]

                    columnDictionary[columnCode].append(lineElement)

        return columnDictionary, listOfDictionaryColumnCodes

    def genReport(self, unit=None, district=None):

        # percent not trained
        yes = self.trainedLeaders["Trained"].count("YES")
        no = self.trainedLeaders["Trained"].count("NO")

        print("Training Report " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        print("Total percent trained is " + str(yes / (yes + no) * 100))

        currentUnit = None
        currentDistrict = None

        for i in range(len(self.trainedLeaders["District"])):
            if currentDistrict != self.trainedLeaders["District"][i]:
                currentDistrict = self.trainedLeaders["District"][i]
                print("\nShowing results from district" + currentDistrict + ": ")

            if currentUnit != self.trainedLeaders["Unit"][i]:
                currentUnit = self.trainedLeaders["Unit"][i]
                print("\nShowing results from " + currentUnit + ": ")

            if self.trainedLeaders["Trained"][i] == "NO":
                print(self.trainedLeaders["Email"][i])