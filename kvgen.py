#developed by Balika4222
import sys
import os
os.system("cls")
from pickle import TRUE
TGREEN =  '\033[32m' # Green Text
TRED =  '\033[31m' # Red Text
TBLUE =  '\033[34m' # Blue Text
ENDC = '\033[m' # reset to the defaults

def restartSelf():
        os.execv(sys.executable, ['python'] + sys.argv)

print("---KV generator by Balika---")

mapname = input(TGREEN + "Input your map's name: " + ENDC)
while True:
    if mapname == "":
        mapname = input(TGREEN + "Input your map's name: " + ENDC)
    else:
        break

print("Your map name is: "+mapname+".")
print(TRED + "AVILABLE T PLAYER MODELS" + ENDC)
print("1-Anarchist")
print("2-Balkan")
print("3-LEET")
print("4-Phoenix")
print("5-Pirate")
print("6-Professional")
print("7-Separatist")

while True:
    try:
        tmodel = int(input(TGREEN + "Choose your T side player model [1-7]: " + ENDC))
        if tmodel < 1 or tmodel > 7:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-7.")

print(TBLUE + "AVILABLE CT PLAYER MODELS"+ ENDC)
print("1-FBI")
print("2-GIGN")
print("3-GSG")
print("4-IDF")
print("5-SAS")
print("6-SEALS")
print("7-SWAT")

while True:
    try:
        ctmodel = int(input(TGREEN + "Choose your CT side player model [1-7]: " + ENDC))
        if ctmodel < 1 or ctmodel > 7:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-7.")

if tmodel == 1: #anarchist
    tline = '		"tm_anarchist"""\n		"tm_anarchist_variantA"""\n		"tm_anarchist_variantB"""\n		"tm_anarchist_variantC"""\n		"tm_anarchist_variantD"""\n'
    tlinearm = 'models/weapons/t_arms_anarchist.mdl'

elif tmodel == 2: #balkan
    tline = '		"tm_balkan_variantA"""\n		"tm_balkan_variantB"""\n		"tm_balkan_variantC"""\n		"tm_balkan_variantD"""\n		"tm_balkan_variantE"""\n'
    tlinearm = 'models/weapons/t_arms_balkan.mdl'

elif tmodel == 3: #LEET
    tline = '		"tm_leet_variantA"""\n		"tm_leet_variantB"""\n		"tm_leet_variantC"""\n		"tm_leet_variantD"""\n		"tm_leet_variantE"""\n'
    tlinearm = 'models/weapons/t_arms_leet.mdl'

elif tmodel == 4: #Phoenix
    tline = '		"tm_phoenix"""\n		"tm_phoenix_variantA"""\n		"tm_phoenix_variantB"""\n		"tm_phoenix_variantC"""\n		"tm_phoenix_variantD"""\n'
    tlinearm = 'models/weapons/t_arms_phoenix.mdl'

elif tmodel == 5: #Pirate
    tline = '		"tm_pirate"""\n		"tm_pirate_variantA"""\n		"tm_pirate_variantB"""\n		"tm_pirate_variantC"""\n		"tm_pirate_variantD"""\n'
    tlinearm = 'models/weapons/t_arms_pirate.mdl'

elif tmodel == 6: #Professional
    tline = '		"tm_professional"""\n		"tm_professional_var1"""\n		"tm_professional_var2"""\n		"tm_professional_var3"""\n		"tm_professional_var4"""\n'
    tlinearm = 'models/weapons/t_arms_professional.mdl'

elif tmodel == 7: #Separatist
    tline = '		"tm_separatist"""\n		"tm_separatist_variantA"""\n		"tm_separatist_variantB"""\n		"tm_separatist_variantC"""\n		"tm_separatist_variantD"""\n'
    tlinearm = 'models/weapons/t_arms_separatist.mdl'

#end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  end of T models list ------  

if ctmodel == 1: #FBI
    ctline = '		"ctm_fbi"""\n		"ctm_fbi_variantA"""\n		"ctm_fbi_variantB"""\n		"ctm_fbi_variantC"""\n		"ctm_fbi_variantD"""\n'
    ctlinearm = 'models/weapons/ct_arms_fbi.mdl'

elif ctmodel == 2: #GIGN
    ctline = '		"ctm_gign"""\n		"ctm_gign_variantA"""\n		"ctm_gign_variantB"""\n		"ctm_gign_variantC"""\n		"ctm_gign_variantD"""\n'
    ctlinearm = 'models/weapons/ct_arms_gign.mdl'

elif ctmodel == 3: #GSG
    ctline = '		"ctm_gsg9"""\n		"ctm_gsg9_variantA"""\n		"ctm_gsg9_variantB"""\n		"ctm_gsg9_variantC"""\n		"ctm_gsg9_variantD"""\n'
    ctlinearm = 'models/weapons/ct_arms_gsg9.mdl'

elif ctmodel == 4: #IDF
    ctline = '		"ctm_idf"""\n		"ctm_idf_variantB"""\n		"ctm_idf_variantC"""\n		"ctm_idf_variantD"""\n		"ctm_idf_variantE"""\n		"ctm_idf_variantF"""\n'
    ctlinearm = 'models/weapons/ct_arms_idf.mdl'

elif ctmodel == 5: #SAS
    ctline = '		"ctm_sas"""\n		"ctm_sas_variantA"""\n		"ctm_sas_variantB"""\n		"ctm_sas_variantC"""\n		"ctm_sas_variantD"""\n		"ctm_sas_variantE"""\n'
    ctlinearm = 'models/weapons/ct_arms_sas.mdl'

elif ctmodel == 6: #SEALS
    ctline = '		"ctm_st6"""\n		"ctm_st6_variantA"""\n		"ctm_st6_variantB"""\n		"ctm_st6_variantC"""\n		"ctm_st6_variantD"""\n'
    ctlinearm = 'models/weapons/ct_arms_st6.mdl'

elif ctmodel == 7: #SWAT
    ctline = '		"ctm_swat"""\n		"ctm_swat_variantA"""\n		"ctm_swat_variantB"""\n		"ctm_swat_variantC"""\n		"ctm_swat_variantD"""\n'
    ctlinearm = 'models/weapons/ct_arms_swat.mdl'

finalprint = '"'+mapname+'"\n' '{\n' '    "name"  ' '"'+mapname+'"\n' '    "imagename"     ' '"'+mapname+'"\n'  '    "t_arms"    '  '"'+tlinearm+'"\n'	'   "ct_arms"   '	'"'+ctlinearm+'"\n'	    '   "t_models"\n' '    {\n' +tline+ '}\n' 	'   "ct_models"\n' '    {\n' +ctline+ '    }\n' '}\n' "//---KV generator by Balika---"

with open(mapname + '.kv', 'w') as outputTxt:
    outputTxt.write(finalprint)
print(".kv file exported!")

sysrestart = str(input('Press ENTER to exit or type R to restart '))
if sysrestart.upper() == "R":
    restartSelf()