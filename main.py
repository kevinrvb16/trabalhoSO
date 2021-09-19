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

    print("-----------------------------START FIFO------------------------------")
    Fifo(referencedpages)
    print("-----------------------------END FIFO------------------------------\n")
    print("-----------------------------START SECOND CHANCE---------------------")
    SecondChance(referencedpages)
    print("-----------------------------END SECOND CHANCE---------------------\n")
    print("-----------------------------START NRU-------------------------------")
    NRU(referencedpages)
    print("-----------------------------END NRU-------------------------------\n")
    print("-----------------------------START LRU-------------------------------")
    LRU(referencedpages)
    print("-----------------------------END LRU-------------------------------\n")

main()
