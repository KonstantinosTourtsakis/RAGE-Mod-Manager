import os
import shutil
from pathlib import Path

#PATHS

#The following paths refer to the Mods folders paths
v = r"\GTA V Mods"
modsV = rf"{Path().absolute()}{v}"
rdr2 = r"\RDR2 Mods"
modsRDR2 = rf"{Path().absolute()}{rdr2}"
iv = r"\GTA IV Mods"
modsIV = rf"{Path().absolute()}{iv}"

#The following paths refer to the game directory:
filepath = modsV + r"\gtavpath.txt"
f = open(filepath, "r")
p = f.read()
f.close()
pathV = rf"{p}"

filepath = modsRDR2 + r"\rdr2path.txt"
f = open(filepath, "r")
p = f.read()
f.close()
pathRDR2 = rf"{p}"

filepath = modsIV + r"\gtaivpath.txt"
f = open(filepath, "r")
p = f.read()
f.close()
pathIV = rf"{p}"


# Lists that include the game files' names based on the Rockstar Games Launcher (RGL) version

RDR2rgl = ["12on7",
   "amd_ags_x64.dll",
   "anim_0.rpf",
   "appdata0_update.rpf",
   "bink2w64.dll",
   "common_0.rpf",
   "data_0.rpf",
   "dxilconv7.dll",
   "hd_0.rpf",
   "index.bin",
   "levels_0.rpf",
   "levels_1.rpf",
   "levels_2.rpf",
   "levels_3.rpf",
   "levels_4.rpf",
   "levels_5.rpf",
   "levels_6.rpf",
   "levels_7.rpf",
   "movies_0.rpf",
   "nvngx_dlss.dll",
   "oo2core_5_win64.dll",
   "packs_0.rpf",
   "packs_1.rpf",
   "RDR2.exe",
   "Redistributables",
   "rowpack_0.rpf",
   "shaders_x64.rpf",
   "textures_0.rpf",
   "textures_1.rpf",
   "update.rpf",
   "update_1.rpf",
   "update_2.rpf",
   "update_3.rpf",
   "update_4.rpf",
   "x64",
   "commandline.txt",

   "installscript.vdf", #Steam files
   "PlayRDR2.exe",
   "steam_api64.dll",

   ".egstore", #Epic Games files
   "EOSSDK-Win64-Shipping.dll",

   "rdr2path.txt"]


GTAVrgl = ["bink2w64.dll",
"common.rpf",
"d3dcompiler_46.dll",
"d3dcsx_46.dll",
"GFSDK_ShadowLib.win64.dll",
"GFSDK_TXAA.win64.dll",
"GFSDK_TXAA_AlphaResolve.win64.dll",
"GPUPerfAPIDX11-x64.dll",
"GTA5.exe",
"GTAVLanguageSelect.exe",
"GTAVLauncher.exe",
"index.bin",
"NvPmApi.Core.win64.dll",
"PlayGTAV.exe",
"ReadMe",
"Redistributables",
"update",
"version.txt",
"x64",
"x64a.rpf",
"x64b.rpf",
"x64c.rpf",
"x64d.rpf",
"x64e.rpf",
"x64f.rpf",
"x64g.rpf",
"x64h.rpf",
"x64i.rpf",
"x64j.rpf",
"x64k.rpf",
"x64l.rpf",
"x64m.rpf",
"x64n.rpf",
"x64o.rpf",
"x64p.rpf",
"x64q.rpf",
"x64r.rpf",
"x64s.rpf",
"x64t.rpf",
"x64u.rpf",
"x64v.rpf",
"x64w.rpf",
"commandline.txt",
"uninstall.exe",

"installscript.vdf", #Steam files
"steam_api64.dll",
"_CommonRedist",
"Installers",

".egstore", #Epic Games files
"ReadMe",
"EOSSDK-Win64-Shipping.dll",


"gtavpath.txt"]

#GTA IV list is based on the Complete Edition of the game (also on RGL)
GTAIVrgl = ["binkw32.dll",
"common",
"gtaEncoder.exe",
"GTAIV.exe",
"index.bin",
"Manuals",
"metadata.dat",
"movies",
"MTLX.dll",
"pc",
"Redistributables",
"TBoGT",
"TLAD",

"steam_api.dll", #Steam files
"installscript.vdf",
"PlayGTAIV.exe",

"gtaivpath.txt"]


#Int variables to print if there are mods installed/detected or mod in the backup folders
gtav = 0
rdr2 = 0
gtaiv = 0
#backup files. These are the files located in the backup folders. For example: GTA V Mods
backup_v = 0
backup_rdr2 = 0
backup_iv = 0



def CheckForMods(directory, list):
    directory = os.fsencode(directory)
    modsCounter = 0
    if os.path.exists(directory):
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename not in list:
                modsCounter = modsCounter + 1

    return modsCounter



def PrintInstalledMods(directory, list):
    print(str(directory))
    directory = os.fsencode(directory)
    if os.path.exists(directory):
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename not in list:
                print("\n  " + filename)
    else:
        e = input("Incorrect or nonexistent path. Please add your game folder's path in gamepath.txt file.")
        exit()
    a = input("\nProcess successfuly completed. Press any key to continue: ")



def TransferMods(directory, destination, list, install):
    if not os.path.exists(directory):
        print("Incorrect or nonexistent path. Check your game paths.\n")
        e = input("Press any key to exit...")
        exit()

    sum = 0
    if install:
        text = "Installing "
    else:
        text = "Removing "

    print("Transfering files from (" + str(directory) + ") to (" + str(destination) + ")\n")
    directory = os.fsencode(directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename not in list:
            d1 = os.fsdecode(directory)
            if os.path.exists(directory) and os.path.exists(destination):
                name = '\\' + filename

                if os.path.exists(r'%s' %destination +  name):
                    print(filename + " already exists in the destination folder. The file was deleted instead.")
                    os.remove(r'%s' %d1 +  name)
                    #z = input("\n\nPress any key to continue transfering files/mods")
                else:
                    print("  " + text + filename)
                    shutil.move(r'%s' %d1 +  name, r'%s' %destination)
                    sum = sum + 1

            else:
                e = input("Incorrect or nonexistent path. Please add your game folder's path in gamepath.txt file.")
                exit()

    if install:
        print(" ")
        print("Finished transfering files. " + str(sum) + " file(s) were installed")
        print(" ")
    else:
        print(" ")
        print("Finished transfering files. " + str(sum) + " file(s) were removed")
        print(" ")
    print(" ")
    a = input("Process successfuly completed. Press any key to continue: ")



def PrintGameHeader(choic):
    if choic == 1:
        print("---------------------------- GTA V -----------------------------\n")
    elif choic == 2:
        print("--------------------- Red Dead Redemption 2 --------------------\n")
    elif choic == 3:
        print("--------------------------- GTA IV -----------------------------\n")



#------------------------ Main ----------------------
gtav = CheckForMods(pathV, GTAVrgl)
rdr2 = CheckForMods(pathRDR2, RDR2rgl)
gtaiv = CheckForMods(pathIV, GTAIVrgl)

backup_v = CheckForMods(modsV, GTAVrgl)
backup_rdr2 = CheckForMods(modsRDR2, RDR2rgl)
backup_iv = CheckForMods(modsIV, GTAIVrgl)

print(" ")
print("-------------------------------------- RAGE Mod Manager ---------------------------------------\n")
print("          GAME                                MODS INSTALLED             BACKUP FOLDER         \n")
print("  1) GTA V" + "                                         " + str(gtav) + "                          " + str(backup_v) + "\n")
print("  2) Red Dead Redemption 2" + "                         " + str(rdr2) + "                          " + str(backup_rdr2) + "\n")
print("  3) GTA IV" + "                                        " + str(gtaiv) + "                          " + str(backup_iv) + "\n")
print("  4) Exit\n")
print("-----------------------------------------------------------------------------------------------")
print(" ")
choice = int(input("Select a game or Exit: "))
os.system("cls")

while choice != 4:
    print(" ")
    PrintGameHeader(choice)
    print("  1) Remove mods from game folder\n")
    print("  2) Install mods to game folder\n")
    print("  3) Display currently installed mods\n")
    print("  4) Go back to main menu\n")
    print("----------------------------------------------------------------")
    print(" ")
    option = int(input("Select an option: "))
    os.system("cls")

    if choice == 1:
        if option == 1:
            TransferMods(pathV, modsV, GTAVrgl, False)
        elif option == 2:
            TransferMods(modsV, pathV, GTAVrgl, True)
        elif option == 3:
            PrintInstalledMods(pathV, GTAVrgl)
        elif option == 4:
            print("Going back to main menu...")
        else:
            a = input("Invalid option. Press enter to exit: ")
            exit()
    elif choice == 2:
        if option == 1:
            TransferMods(pathRDR2, modsRDR2, RDR2rgl, False)
        elif option == 2:
            TransferMods(modsRDR2, pathRDR2, RDR2rgl, True)
        elif option == 3:
            PrintInstalledMods(pathRDR2, RDR2rgl)
        elif option == 4:
            print("Going back to main menu...")
        else:
            a = input("Invalid option. Press enter to exit: ")
            exit()
    elif choice == 3:
        if option == 1:
            TransferMods(pathIV, modsIV, GTAIVrgl, False)
        elif option == 2:
            TransferMods(modsIV, pathIV, GTAIVrgl, True)
        elif option == 3:
            PrintInstalledMods(pathIV, GTAIVrgl)
        elif option == 4:
            print("Going back to main menu...")
        else:
            a = input("Invalid option. Press enter to exit: ")
            exit()
    else:
        a = input("Invalid game option. Press enter to exit: ")
        exit()

    os.system("cls")
    print(" ")
    gtav = CheckForMods(pathV, GTAVrgl)
    rdr2 = CheckForMods(pathRDR2, RDR2rgl)
    gtaiv = CheckForMods(pathIV, GTAIVrgl)

    backup_v = CheckForMods(modsV, GTAVrgl)
    backup_rdr2 = CheckForMods(modsRDR2, RDR2rgl)
    backup_iv = CheckForMods(modsIV, GTAIVrgl)
    print(" ")
    print("-------------------------------------- RAGE Mod Manager ---------------------------------------\n")
    print("          GAME                                MODS INSTALLED             BACKUP FOLDER         \n")
    print("  1) GTA V" + "                                         " + str(gtav) + "                          " + str(backup_v) + "\n")
    print("  2) Red Dead Redemption 2" + "                         " + str(rdr2) + "                          " + str(backup_rdr2) + "\n")
    print("  3) GTA IV" + "                                        " + str(gtaiv) + "                          " + str(backup_iv) + "\n")
    print("  4) Exit\n")
    print("-----------------------------------------------------------------------------------------------")
    print(" ")
    choice = int(input("Select a game or Exit: "))
    os.system("cls")

exit()
