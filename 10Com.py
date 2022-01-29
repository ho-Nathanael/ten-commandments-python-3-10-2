#Ten Commandments (Exodus 20)
#I used e-Sword
#KJV
#Python 3.10.2
#29/01/2022

import sys

def start():
    print()
    print("THE TEN COMMANDMENTS")
    print("EXODUS 20")
    print()
    print("Type 's()' to start, 'q()' to quit")
    print()
    print("Visit sabbathtruth.com")
    print()
    print("------------------------------")
    print()

start()
print("... PREAMBLE ...")
print()
print("I am the LORD thy God, which have brought thee out of the land of Egypt, out of the house of bondage.")
print()
print("Exodus 20:2")
print()
print("------------------------------")

def  q():
    quit()
    
def s():
    print()
    com = int(input("Input Commandment Number from 1 to 10:  "))
    ten_com = ("Thou shalt have no other gods before me. (Exodus 20:3)","Thou shalt not make unto thee any graven image, or any likeness of any thing that is in heaven above, or that is in the earth beneath, or that is in the water under the earth: thou shalt not bow down thyself to them, nor serve them: for I the LORD thy God am a jealous God, visiting the iniquity of the fathers upon the children unto the third and fourth generation of them that hate me; and shewing mercy unto thousands of them that love me, and keep my commandments. (Exodus 20:4-6)","Thou shalt not take the name of the LORD thy God in vain; for the LORD will not hold him guiltless that taketh his name in vain. (Exodus 20:7)","Remember the sabbath day, to keep it holy. Six days shalt thou labour, and do all thy work: but the seventh day is the sabbath of the LORD thy God: in it thou shalt not do any work, thou, nor thy son, nor thy daughter, thy manservant, nor thy maidservant, nor thy cattle, nor thy stranger that is within thy gates: for in six days the LORD made heaven and earth, the sea, and all that in them is, and rested the seventh day: wherefore the LORD blessed the sabbath day, and hallowed it. (Exodus 20:8-11)","Honour thy father and thy mother: that thy days may be long upon the land which the LORD thy God giveth thee. (Exodus 20:12)","Thou shalt not kill. (Exodus 20:13)","Thou shalt not commit adultery. (Exodus 20:14)","Thou shalt not steal. (Exodus 20:15)","Thou shalt not bear false witness against thy neighbour. (Exodus 20:16)","Thou shalt not covet thy neighbour's house, thou shalt not covet thy neighbour's wife, nor his manservant, nor his maidservant, nor his ox, nor his ass, nor any thing that is thy neighbour's. (Exodus 20:17)")
    rom = ("I","II","III","IV","V","VI","VII","VIII","IX","X")
    print()
    print("---------------COMMANDMENT---------------")
    print()
    print("...",rom[com - 1],"...")
    print()
    print(ten_com[com - 1])
    print()
    print("---------------COMMANDMENT---------------")
    start()

#END
