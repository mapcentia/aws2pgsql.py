#!/usr/bin/env python
import sys, csv
args =sys.argv
filesource = args[1]
sql = "DROP TABlE " + args[2] + ";"+\
		"BEGIN;" +\
		"CREATE TABLE " + args[2] + " (" +\
		"id varchar," +\
		"status int," +\
		"oprettet varchar," +\
		"aendret varchar," +\
		"vejkode varchar," +\
		"vejnavn varchar," +\
		"adresseringsvejnavn varchar," +\
		"husnr varchar," +\
		"supplerendebynavn varchar," +\
		"postnr varchar," +\
		"postnrnavn varchar," +\
		"stormodtagerpostnr varchar," +\
		"stormodtagerpostnrnavn varchar," +\
		"kommunekode varchar," +\
		"kommunenavn varchar," +\
		"ejerlavkode varchar," +\
		"ejerlavnavn varchar," +\
		"matrikelnr varchar," +\
		"esrejendomsnr varchar," +\
		"etrs89koordinat_oest varchar," +\
		"etrs89koordinat_nord varchar," +\
		"wgs84koordinat_bredde varchar," +\
		"wgs84koordinat_laengde varchar," +\
		"noejagtighed varchar," +\
		"kilde varchar," +\
		"tekniskstandard varchar," +\
		"tekstretning varchar," +\
		"adressepunktaendringsdato varchar," +\
		"ddkn_m100 varchar," +\
		"ddkn_km1 varchar," +\
		"ddkn_km10 varchar," +\
		"regionskode varchar," +\
		"regionsnavn varchar," +\
		"jordstykke_ejerlavnavn varchar," +\
		"kvh varchar," +\
		"sognekode varchar," +\
		"sognenavn varchar," +\
		"politikredskode varchar," +\
		"politikredsnavn varchar," +\
		"retskredskode varchar," +\
		"retskredsnavn varchar," +\
		"opstillingskredskode varchar," +\
		"opstillingskredsnavn varchar," +\
		"zone varchar," +\
		"jordstykke_ejerlavkode varchar," +\
		"jordstykke_matrikelnr varchar," +\
		"jordstykke_esrejendomsnr varchar," +\
		"the_geom geometry(Point,4326)," +\
		"gid SERIAL PRIMARY KEY" +\
		");" +\
		"COMMIT;"
print sql
#sys.exit()
#print "BEGIN;"
with open(filesource, 'rb') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    i = 1
    for row in reader:
	if i>1:
		statement = "INSERT INTO " + args[2] + " " + \
				    "VALUES ('%s',%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',ST_geomfromtext('POINT(%s %s)',4326));" % (tuple([w.replace("'","''") for w in row[0:47]]) + (row[22],row[21]))
		print statement
	i = i + 1
#print "COMMIT"
