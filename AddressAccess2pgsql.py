#!/usr/bin/env python
import sys, csv
args =sys.argv
filesource = args[1]
sql = "DROP TABlE " + args[2] + ";"+\
		"BEGIN;" +\
		"CREATE TABLE " + args[2] + " (" +\
		"gid SERIAL PRIMARY KEY," +\
		"AddressAccessIdentifier varchar," +\
		"VersionId varchar," +\
		"BuildingName varchar," +\
		"MunicipalityCode varchar," +\
		"StreetCode varchar," +\
		"StreetName varchar," +\
		"StreetBuildingIdentifier varchar," +\
		"DistrictSubdivisionIdentifier varchar," +\
		"PostCodeIsdentifier varchar," +\
		"DistrictName varchar," +\
		"CadastralDistrictIdentifier varchar," +\
		"CadastralDistrictName varchar," +\
		"LandParcelIdentifier varchar," +\
		"MunicipalRealPropertyIdentifier varchar," +\
		"the_geom geometry(Point,25832)" +\
		");" +\
		"COMMIT;"
print sql
#sys.exit()
#print "BEGIN;"
with open(filesource, 'rb') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    i = 1
    for row in reader:
	if i>1:
		statement = "INSERT INTO " + args[2] + " " + \
				    "(" +\
				    "AddressAccessIdentifier," + \
				    "VersionId," + \
				    "BuildingName," +\
				    "MunicipalityCode," +\
				    "StreetCode," +\
				    "StreetName," +\
				    "StreetBuildingIdentifier," +\
				    "DistrictSubdivisionIdentifier," +\
				    "PostCodeIsdentifier," +\
				    "DistrictName," +\
				    "CadastralDistrictIdentifier," +\
				    "CadastralDistrictName," +\
				    "LandParcelIdentifier," +\
				    "MunicipalRealPropertyIdentifier," +\
				    "the_geom" +\
				    ") " + \
				    "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',ST_geomfromtext('POINT(%s %s)',25832));" % (tuple([w.replace("'","''") for w in row[0:14]]) + tuple(row[17:19]))
		print statement
	i = i + 1
#print "COMMIT"
