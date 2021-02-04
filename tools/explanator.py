#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 1-13: Name
15-18: HexNbr
20-28: UWP
   31: Bases
33-47: Codes & Comments
   49: Zone
52-54: PBG
56-57: Allegiance
59-74: Stellar Data
'''

import json
import locale
locale.setlocale(locale.LC_ALL, '')

database = "UWP.json"
data = json.loads(open(database, encoding="utf8").read())

def print_world_description(uwp, codes, base, p):
	starport_class, dimension, atmosphere, idrography, population, government, law_lev, hyphen, tech_lev = list(uwp)
	print("## Astroporto:", file=text_file)
	for r in data['Astroporto']:
		if r['Classe'] == starport_class:
			print("**Classe**: {} - {}  " .format(r['Classe'], r['Descrizione']) , file=text_file)
			print("  - _Miglior Carburante_: {}  " .format(r['Miglior Carburante']) , file=text_file)
			print("  - _Manutenzione Annuale_: {}  " .format(r['Manutenzione Annuale']) , file=text_file)
			print("  - _Potenziale del Cantiere Navale_: {} \n" .format(r['Potenziale del Cantiere Navale']) , file=text_file)
#			print("**Basi Possibili**: ", r['Basi Possibili'] , file=text_file)

	print("## Dimensione:", file=text_file)
	for r in data['Dimensione']:
		if r['Cifra'] == dimension:
			print("**Diametro Planetario**: {}  " .format(r['Dimensioni']) , file=text_file)
			print("**Gravità di Superficie (g)**: {} \n" .format(r['Gravità di Superficie (g)']) , file=text_file)

	print("## Atmosfera:", file=text_file)
	for r in data['Atmosfera']:
		if r['Cifra'] == atmosphere:
			print("**Tipo**: {}  " .format(r['Atmosfera']), file=text_file)
			print("**Pressione**: {}  " .format(r['Pressione']), file=text_file)
			print("**Attrezzatura Necessaria alla Sopravvivenza** : {} \n" .format(r["Attrezzatura necessaria alla Sopravvivenza"]), file=text_file)

	print("## Idrografia:", file=text_file)
	for r in data['Idrografia']:
		if r['Cifra'] == idrography:
			print("**Percentuale Idrografica**: {}  " .format(r['Percentuale Idrografica']), file=text_file)
			print("**Descrizione**: {} \n" .format(r['Descrizione']), file=text_file)

	print("## Popolazione:", file=text_file)
	if population == "A":
		population = "10"
	elif population == "B":
		population = "11"
	elif population == "C":
		population = "12"
	elif population == "D":
		population = "13"
	elif population == "E":
		population = "14"
	elif population == "F":
		population = "15"
	pop = int(p)*10**int(population)
	print("**Numero di Abitanti**: {:n} \n" .format(pop), file=text_file)
	#for r in data['Popolazione']:
	#	if r['Cifra'] == population:
	#		print("Popolazione: ", r['Popolazione'])
	#		print("**Numero di Abitanti**: {}  " .format(r['Numero di Abitanti']), file=text_file)
	#		print("Descrizione della popolazione: ", r['Descrizione'])

	print("## Governo:", file=text_file)
	for r in data['Governo']:
		if r['Tipo'] == government:
			print("**Descrizione**: {} \n" .format(r['Governo']), file=text_file)

	print("## Livello Tecnologico:", file=text_file)
	for r in data['LT']:
		if r['LT'] == law_lev:
			print("**Descrizione**: {} - {}" .format(r['LT'], r['Descrittore']) , file=text_file)
			print("**Caratteristiche Principali**: {} \n" .format(r['Caratteristiche principali']), file=text_file)

	print("## Livello di Legge:", file=text_file)
	for r in data['LL']:
		if r['Cifra'] == tech_lev:
			print("**Descrizione**:  {} - {}  " .format(r['Cifra'],r['Descrizione']) , file=text_file)
			print("**Attività Non Permesse**: {} \n" .format(r['Attività non permesse']), file=text_file)

	print("## Classificazioni: ", file=text_file)
	for code in codes:
		for r in data['CC']:
			if r['Codice'] == code:
				print("  - {}" .format(r['Classificazione']), file=text_file)
	print("\n", file=text_file)

	print("## Basi: ", file=text_file)
	if base:
		for r in data['Base']:
			if r['Codice'] == base:
				print(" {}" .format(r['Descrizione']), file=text_file)
	else:
		print("Nessuna base presente", file=text_file)
	print("\n", file=text_file)
text_file = open("Output.md", "w", encoding="utf8")

with open('lambda_zagreus.sec') as f:
    for _ in range(13):
        next(f)
    for line in f:
        name = line[0:13].strip()
        hex = line[14:18].strip()
        uwp = line[19:28].strip()
        base = line[29].strip()
        codes = line[31:47].strip().split()
        zone = line[48].strip()
        p, b, g = list(line[51:54].strip())
        allegiance = line[55:57].strip()
        stellar_data = line[58:74].strip()

        print("# " + name + " (" + hex + ") - " + uwp, file=text_file)
        print("## Descrizione del sistema:", file=text_file)
        print("**Classificazione stellare**: {}  " .format(stellar_data), file=text_file)
        print("**Numero di fasce di asteroidi**: {}  " .format(b), file=text_file)
        print("**Numero di giganti gassosi**: {} \n" .format(g), file=text_file)
        print_world_description(uwp, codes, base, p)
        print("\n", file=text_file)

text_file.close()