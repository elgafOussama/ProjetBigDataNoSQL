#!/bin/bash

sudo service mongod start
#sudo service mongod status

mongoimport -d db -c dbCollection --type CSV --file predict.csv --headerline


mongoexport -d db -c dbCollection -f "TARGET_p,NAME_FAMILY_STATUS,NAME_HOUSING_TYPE,OCCUPATION_TYPE" -q '{TARGET_p:1,CODE_GENDER:"F"}' -o res.json
mongoimport -d db -c dbFemalePret --file res.json
echo "Importer liste des Femmes qui ont un pret"


mongoexport -d db -c dbCollection -f "TARGET_p,NAME_FAMILY_STATUS,NAME_HOUSING_TYPE,OCCUPATION_TYPE" -q '{TARGET_p:0,CODE_GENDER:"F"}' -o res.json
mongoimport -d db -c dbFemaleNonPret --file res.json
echo "Importer liste des Femmes qui n'ont pas un pret"


mongoexport -d db -c dbCollection -f "TARGET_p,NAME_FAMILY_STATUS,NAME_HOUSING_TYPE,OCCUPATION_TYPE" -q '{TARGET_p:1,CODE_GENDER:"M"}' -o res.json
mongoimport -d db -c dbMalePret --file res.json
echo "Importer liste des Hommes qui ont un pret"

mongoexport -d db -c dbCollection -f "TARGET_p,NAME_FAMILY_STATUS,NAME_HOUSING_TYPE,OCCUPATION_TYPE" -q '{TARGET_p:0,CODE_GENDER:"M"}' -o res.json
mongoimport -d db -c dbMaleNonPret --file res.json
echo "Importer liste des Hommes qui n'ont pas un pret"


mongoexport -d db -c dbCollection -f "TARGET_p,NAME_FAMILY_STATUS,NAME_HOUSING_TYPE,OCCUPATION_TYPE" -q '{TARGET_p:1}' -o res.json
mongoimport -d db -c dbPersonnesPret --file res.json
echo "Importer liste des Personnes qui ont un pret"

mongoexport -d db -c dbCollection -f "TARGET_p,NAME_FAMILY_STATUS,NAME_HOUSING_TYPE,OCCUPATION_TYPE" -q '{TARGET_p:0}' -o res.json
mongoimport -d db -c dbPersonnesNonPret --file res.json
echo "Importer liste des Personnes qui n'ont pas un pret"


sudo rm res.json