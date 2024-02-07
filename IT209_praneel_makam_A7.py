# Name: Praneel Makam
# This program defines a class FCPDCrime, which extends the built-in list class.
# The purpose of the class is to process and analyze crime data from a CSV file
# downloaded from the Fairfax County Police site. It provides methods to load
# the data, print crime reports, retrieve incident lines for a specific Zip Code,
# and generate statistics such as counts of crimes by Zip Code and crime type.

# Import necessary modules for working with CSV files, file paths, and collections.
import csv
from collections import Counter
import os

# Determine the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the CSV file
file_path = os.path.join(script_directory, '/Users/pmakamjr/GMU Classes/IT 209/Assignments/Assignment 7/CrimeReports.csv')

# Define the FCPDCrime class, which extends the list class
class FCPDCrime(list):
    def __init__(self, name='Fairfax County Police Crime Report'):
        super().__init__()
        self.name = name

    # Load method reads and loads data from a CSV file into the FCPDCrime object
    def load(self, file='/Users/pmakamjr/GMU Classes/IT 209/Assignments/Assignment 7/CrimeReports.csv'):
        file_path = os.path.join(script_directory, file)
        try:
            with open(file_path, 'r', newline="") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    self.append(row)
            return len(self)  # Return the number of lines read
        except FileNotFoundError as e:
            print("File not found:", e)
            return 0

    # PrintCrimes method displays a formatted report of all lines in the downloaded report
    def printCrimes(self, zip='all'):
        print(f'{self.name}:\nFCPD Police Crime Statistics for the week 2023-04-01 through 2023-04-08')
        for line in self:
            if zip == 'all' or line[-1] == zip:
                print(line)

    # ZipCodeList method returns a list of all incident report lines for a selected Fairfax County ZipCode
    def zipCodeList(self, zip_code='22030'):
        return [line for line in self if line[-1] == zip_code]

#     # CountByZip method displays a report of the number of crimes reported by Zip Code in sorted format
    def countByZip(self):
        zip_counts = {}
        for line in self:
            zip_code = line[-1]
            zip_counts[zip_code] = zip_counts.get(zip_code, 0) + 1
        sorted_zip_counts = sorted(zip_counts.items(), key=lambda x: x[1], reverse=True)
        print('Count of number of reports by Zip Code, sorted by frequency\n')
        print('FCPD Police Crime Statistics for the week 2023-04-01 through 2023-04-08\n')
        for zip_code, count in sorted_zip_counts:
            percentage = (count / len(self)) * 100
            print(f'{zip_code}    {count}    {percentage:.2f}%')

#     # CountByCrime method displays a list of reported numbers for each type of crime
    def countByCrime(self, select='all'):
        crime_counts = {}
        for crime in self:
            if select == 'all' or crime[-1] == select:
                crime_code = crime[1]
                crime_counts[crime_code] = crime_counts.get(crime_code, 0) + 1
        sorted_crimes = sorted(crime_counts.items(), key=lambda x: x[1], reverse=True)
        print(f"List of crimes by code, sorted by frequency, for {'all' if select == 'all' else f'Zip Code {select}'}\n")
        print(f"{self.name}\n")
        for crime, count in sorted_crimes:
            percentage = count / len(self) * 100
            description = [item[2] for item in self if item[1] == crime][0]
            print(f'{crime:<15}    {count:<10}    {percentage:.2f}%    {description}')

FC = FCPDCrime(name=' Fairfax County Police Crime Report :')
lines_read = FC.load(file='/Users/pmakamjr/GMU Classes/IT 209/Assignments/Assignment 7/CrimeReports.csv')
print(f"Loaded {lines_read} lines from the data file.")

# Demonstrate all methods
FC.printCrimes()
input("Press Enter to continue...")

ZL = FC.zipCodeList(zip_code='22030')
for c in ZL:
    print(c)
input("Press Enter to continue...")

FC.countByZip()
input("Press Enter to continue...")

FC.countByCrime(select = "all")