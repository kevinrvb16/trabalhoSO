from secondchance import SecondChance
from fifo import Fifo
from nru import NRU
from lru import LRU

def main():
    readReferenceFile = open("./referencedpagestest1.txt", "r")
    referencedpages = []
    for line in readReferenceFile:
        referencedpages = line.split(', ')
    readReferenceFile.close()

    Fifo(referencedpages)
    print("-----------------------------END FIFO-------------------------------")
    SecondChance(referencedpages)
    print("-----------------------------END SECONDCHANCE-------------------------------")
    NRU(referencedpages)
    print("-----------------------------END NRU-------------------------------")
    LRU(referencedpages)
    print("-----------------------------END LRU-------------------------------")

main()
