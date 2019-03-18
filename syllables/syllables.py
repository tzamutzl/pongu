#! /usr/bin/etc/ env

# Program, ktory vrati vsetky mozne slabiky v pongu
import random

#definujeme premenne
raz = 'ʔ'
vs = ['i','ø','ə','a','ɔ','u'] #vocals short
vl = ['iː','øː','aː','ɔː','uː'] #vocals long
c1 = ['p','t','c','k','ɸ','s','ʃ','ɕ','x','w','j','l','ʎ','m','n','ɲ','ŋ'] #consonant
c2 = ['p','t','c','k','ɸ','s','ʃ','ɕ','x'] #nonvibrant cons.
r  = ['j','w','l','ʎ','m','n','ɲ','ŋ'] #vibrant
m  = ['m','n','ɲ','ŋ'] #nasal
rs = ['l','ʎ','m','n','ɲ','ŋ'] #vibrant short sylabic
rl = ['lː','ʎː','mː','nː','ɲː','ŋː'] #vibrant long sylabic

#TVORBA SLABIK
# I. a) ʔV, ʔV:
RazV = [raz+fonem for fonem in vs]
RazVl = [raz+fonem for fonem in vl]

# I. b) ʔVC
RazVC = []
for segment in RazV:
    for cons in c1:
        RazVC.append(segment+cons)

RazVlC = []
for segment in RazVl:
    for cons in c1:
        RazVlC.append(segment+cons)
        
# II. a) CV, CV:
CV = []
for segment in c1:
    for vocal in vs:
        CV.append(segment+vocal)
        
CVl = []
for segment in c1:
    for vocal in vl:
        CVl.append(segment+vocal)
        
# II. b) CVC, CV:C
CVC = []
for segment in CV:
    for cons in c1:
        CVC.append(segment+cons)
        
CVlC = []
for segment in CVl:
    for cons in c1:
        CVC.append(segment+cons)
        
# III. a) R:C
RlC = []
for segment in rl:
    for cons in c2:
        CVC.append(segment+cons)
        
# III. b) CRC
CRC = []
for seg1 in c2:
    for seg2 in rs:
        for seg3 in c2:
            CRC.append(seg1+seg2+seg3)
            
# III. b) CR:C
CRlC = []
for seg1 in c2:
    for seg2 in rl:
        for seg3 in c2:
            CRC.append(seg1+seg2+seg3)
            
# INVENTAR SLABIK

slabiky = {
    "RazV": RazV,
    "RazVl": RazVl,
    "RazVC": RazVC,
    "RazVlC": RazVlC,
    "CV": CV,
    "CVl": CVl,
    "CVC": CVC,
    "CVlC": CVlC,
    "RlC": RlC,
    "CRC": CRC,
    "CRlC": CRlC
}
syltype = [
    "RazV",
    "RazVl",
    "RazVC",
    "RazVlC",
    "CV",
    "CVl",
    "CVC",
    "CVlC",
    "RlC",
    "CRC",
    "CRlC"
]

# KOMBINOVANIE SLABIK

def sylab():
    return random.choice(slabiky[random.choice(syltype)])

def slovo(syl=2):
    w = ''
    for i in range(syl):
        prav = True
        while prav:
            s = sylab()
            if w == '': prav = False # na zaciatku slova moze byt akakolvek slabika
            if not (w != '' and s.startswith('ʔ')): prav = False # v strede slova nemoze byt slabika typu ʔV, ʔV:
            if not (w[-1] in m and s[0] in m): prav = False # nemozu byt vedla seba dve nazaly
            if not ( (w[-1] in vs or w[-1] == 'ː') and s[0] in rs): prav = False          
        w += s
    return w
