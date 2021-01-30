import os


#PATHS

#The following paths refer to the game directory:
pathV = 'K:\Rockstar Games\Grand Theft Auto V'
pathRDR2 = 'K:\Rockstar Games\Red Dead Redemption 2'
pathIV = 'K:\Rockstar Games\Grand Theft Auto IV'

#The following paths refer to the folders
#where all mods will be transfered/saved
modsV = 'K:\RAGE Mod Manager\GTA V Mods'
modsRDR2 = 'K:\RAGE Mod Manager\RDR2 Mods'
modsIV = 'K:\RAGE Mod Manager\GTA IV Mods'




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
   "x64"]


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
"x64w.rpf"]

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
"TLAD"]


def TransferMods(directory, dest, list, install):
    sum = 0
    if install:
        text = "Installing "
    else:
        text = "Removing "

    directory = os.fsencode(directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename not in list:
            d1 = os.fsdecode(directory)
            print(text + filename)
            name = '\\' + filename
            os.rename(r'%s' %d1 +  name, r'%s' %dest + name)
            sum = sum + 1
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



print(" ")
print("1) GTA V")
print("2) Red Dead Redemption 2")
print("3) GTA IV")
print("4) Exit")
print(" ")
choice = int(input("Select a game or Exit: "))
os.system("cls")

while choice != 4:
    print(" ")
    print("1) Remove mods from game folder")
    print("2) Install mods to game folder")
    print(" ")
    option = int(input("Select an option: "))
    os.system("cls")

    if choice == 1:
        if option == 1:
            TransferMods(pathV, modsV, GTAVrgl, False)
        elif option == 2:
            TransferMods(modsV, pathV, GTAVrgl, True)
        else:
            a = input("Invalid option. Press enter to exit: ")
            exit()
    elif choice == 2:
        if option == 1:
            TransferMods(pathRDR2, modsRDR2, RDR2rgl, False)
        elif option == 2:
            TransferMods(modsRDR2, pathRDR2, RDR2rgl, True)
        else:
            a = input("Invalid option. Press enter to exit: ")
            exit()
    elif choice == 3:
        if option == 1:
            TransferMods(pathIV, modsIV, GTAIVrgl, False)
        elif option == 2:
            TransferMods(modsIV, pathIV, GTAIVrgl, True)
        else:
            a = input("Invalid option. Press enter to exit: ")
            exit()
    else:
        a = input("Invalid game option. Press enter to exit: ")
        exit()

    os.system("cls")
    print(" ")
    print("1) GTA V")
    print("2) Red Dead Redemption 2")
    print("3) GTA IV")
    print("4) Exit")
    print(" ")
    choice = int(input("Select a game or Exit: "))
    os.system("cls")

exit()
