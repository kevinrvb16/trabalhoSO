from fifo import Fifo
from secondchance import SecondChance

def main():
    readReferenceFile = open("./referencedpages.txt", "r")
    referencedpages = []
    for line in readReferenceFile:
        referencedpages = line.split(', ')
    readReferenceFile.close()
    Fifo(referencedpages)
    print("--------------------------------end FIFO--------------------------------")
    SecondChance(referencedpages)
    print("--------------------------------end second chance--------------------------------")

main()
