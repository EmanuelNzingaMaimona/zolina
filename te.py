#!/usr/bin/python3
from json import load, dump

'''
PROVINCE_CHOICES=[]

with open('provincias-cidades.json') as f:
    data = load(f)
    for t in data:
        PROVINCE_CHOICES.append(tuple((t['name'], t['name'])))
    PROVINCE_CHOICES=tuple(PROVINCE_CHOICES) 
print(PROVINCE_CHOICES)
'''
s = 'Cabinda'
MUNICIPE_CHOICES=[]
with open('staticfiles/provincias-cidades.json') as f:
    data = load(f)
    for t in data:
        if t['name'] == s:
            MUNICIPE_CHOICES.append(tuple((t['cities'],t['cities'])))
    MUNICIPE_CHOICES = tuple(MUNICIPE_CHOICES) 
        
print(MUNICIPE_CHOICES)