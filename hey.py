from missiontype import Missiontype
from missiontarget import Missiontarget
from missionprogram import Missionprogram
h=open("mydb.txt")
i=open("mydb1.txt")
j=open("mydb2.txt")
for x in h.readlines():
    Missiontype().create({"name":x,"pic":""})
for x in i.readlines():
    Missiontarget().create({"name":x,"pic":""})
for x in j.readlines():
    Missionprogram().create({"name":x,"pic":""})
