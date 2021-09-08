from fifo import Fifo
from secondchance import SecondChance
from nru import NRU

def main():
    readReferenceFile = open("./referencedpages.txt", "r")
    referencedpages = []
    for line in readReferenceFile:
        referencedpages = line.split(', ')
    readReferenceFile.close()
    Fifo(referencedpages)
    print("--------------------------------END FIFO--------------------------------")
    SecondChance(referencedpages)
    print("--------------------------------END second chance--------------------------------")
    NRU(referencedpages)
    print("--------------------------------END NRU--------------------------------")

main()
