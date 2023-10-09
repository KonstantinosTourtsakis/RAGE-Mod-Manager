import os
import shutil
from pathlib import Path
import json




config = {}




def set_game_dir(game):
	global config
	output = "Set path for " + game + " or type 'none' to skip it: "
	path = input(output)
	index = 0
	for char in path:
	    if char == "\\":
	        path = path[:index] + "\\" + path[index + 1:]
	    index = index + 1
	print(path)
	config[game]["game_directory"] = path

	with open("config.json", "w") as outfile:
		outfile.write(json.dumps(config, indent=4))


def read_game_directories():
    global config
    with open("config.json", "r") as openfile:
    	config = json.load(openfile)


def check_game_directories():
    global config
    for game in config:
        if config[game]["game_directory"] == "":
            set_game_dir(game)


def delete_this(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' was deleted successfully.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory '{path}' and its contents were deleted successfully.")
        else:
            print(f"'{path}' is neither a file nor a directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


class Game:
	path = ""
	backup_dir = ""
	count_installed = 0
	count_backup = 0
	files = []
	header = ""
	conf = ""

	def __init__(self, config, header):
		self.conf = config
		self.header = header


	def count_mods(self, directory):
	    directory = os.fsencode(directory)
	    counter = 0
	    if os.path.exists(directory):
	        for file in os.listdir(directory):
	            filename = os.fsdecode(file)
	            if filename not in self.files:
	                counter = counter + 1

	    return counter

	def print_installed_mods(self):
	    print(str(self.path))
	    directory = os.fsencode(self.path)
	    if os.path.exists(directory):
	        for file in os.listdir(directory):
	            filename = os.fsdecode(file)
	            if filename not in self.files:
	                print("\n  " + filename)
	    else:
	        e = input("Incorrect or nonexistent path. Please add your game folder's path and make sure the appropriate mods folder exist (ex: GTA V Mods)")
	        exit()
	    a = input("\nProcess successfuly completed. Press any key to continue: ")


	def delete_mods(self, directory):
		if not os.path.exists(directory):
			print("Incorrect or nonexistent path. Check your game paths.\n")
			e = input("Press any key to exit...")
			exit()

		direct = os.fsencode(directory)
		for file in os.listdir(direct):
			filename = os.fsdecode(file)
	        
			if not os.access(directory + "\\" + filename, os.W_OK):
				print("No access to file", directory + filename)
				os.system("pause")
				return

			# If file is a mod
			if filename not in self.files:
				print("Deleting " + filename)
				delete_this(directory + "\\" + filename)
		print(" ")
		os.system("pause")

read_game_directories()
check_game_directories()

gtav = Game("Grand Theft Auto V", "---------------------------- GTA V -----------------------------\n")
rdr2 = Game("Red Dead Redemption 2", "--------------------- Red Dead Redemption 2 --------------------\n")
gtaiv = Game("Grand Theft Auto IV", "--------------------------- GTA IV -----------------------------\n")


def update_directories():
	global gtav
	global gtaiv
	global rdr2
	gtav.path = config["Grand Theft Auto V"]["game_directory"]
	gtav.backup_dir = config["Grand Theft Auto V"]["backup_directory"]

	rdr2.path = config["Red Dead Redemption 2"]["game_directory"]
	rdr2.backup_dir = config["Red Dead Redemption 2"]["backup_directory"]

	gtaiv.path = config["Grand Theft Auto IV"]["game_directory"]
	gtaiv.backup_dir = config["Grand Theft Auto IV"]["backup_directory"]

update_directories()



gtaiv.files = ["binkw32.dll",
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
"uninstall.exe",
"steam_api.dll", #Steam files
"installscript.vdf",
"PlayGTAIV.exe"]

rdr2.files = ["12on7",
"NvLowLatencyVk.dll",
"RDR2.exe",
"Redistributables",
"amd_ags_x64.dll",
"anim_0.rpf",
"appdata0_update.rpf",
"bink2w64.dll",
"common_0.rpf",
"data_0.rpf",
"dxilconv7.dll",
"ffx_fsr2_api_dx12_x64.dll",
"ffx_fsr2_api_vk_x64.dll",
"ffx_fsr2_api_x64.dll",
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
"rowpack_0.rpf",
"shaders_x64.rpf",
"textures_0.rpf",
"textures_1.rpf",
"uninstall.exe",
"update_1.rpf",
"update_2.rpf",
"update_3.rpf",
"update_4.rpf",
"x64",
"installscript.vdf", #Steam files
"PlayRDR2.exe",
"steam_api64.dll",
".egstore", #Epic Games files
"EOSSDK-Win64-Shipping.dll" ]


gtav.files = ["GFSDK_ShadowLib.win64.dll",
"GFSDK_TXAA.win64.dll",
"GFSDK_TXAA_AlphaResolve.win64.dll",
"GPUPerfAPIDX11-x64.dll",
"GTA5.exe",
"GTAVLanguageSelect.exe",
"GTAVLauncher.exe",
"NvPmApi.Core.win64.dll",
"PlayGTAV.exe",
"ReadMe",
"Redistributables",
"bink2w64.dll",
"common.rpf",
"d3dcompiler_46.dll",
"d3dcsx_46.dll",
"fvad.dll",
"index.bin",
"libcurl.dll",
"opus.dll",
"opusenc.dll",
"toxmod.dll",
"uninstall.exe",
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
"zlib1.dll",
"installscript.vdf", #Steam files
"steam_api64.dll",
"_CommonRedist",
"Installers",
".egstore", #Epic Games files
"ReadMe",
"EOSSDK-Win64-Shipping.dll"]






#------------------------ Main ----------------------
current_game = Game("", "")




def transfer_mods(directory, destination, list, install):
    if not os.path.exists(directory):
        print("Incorrect or nonexistent path. Check your game paths.\n")
        e = input("Press any key to exit...")
        exit()

    if not os.access(directory, os.W_OK):
        print("Doesn't have write access to", directory)
        os.system("pause")
        return
    else:
        print("Does have write access to", directory)

    sum = 0
    if install:
        text = "Installing "
    else:
        text = "Removing "

    print("Transfering files from (" + str(directory) + ") to (" + str(destination) + ")\n")
    direct = os.fsencode(directory)
    for file in os.listdir(direct):
        filename = os.fsdecode(file)
        #print("FILESSSS: " + directory + "\\" + filename)
        if not os.access(directory + "\\" + filename, os.W_OK):
            print("No access to file", directory + filename)
            os.system("pause")
            return

        if filename not in list:
            d1 = os.fsdecode(direct)
            if os.path.exists(direct) and os.path.exists(destination):
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
                e = input("Incorrect or nonexistent path. Please add your game folder's path and make sure the appropriate mods folder exist (ex: GTA V Mods)")
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


choice = 0
option = 0

def main_menu():
	os.system("cls")
	print(" ")
	global gtav 
	global rdr2 
	global gtaiv 
	global choice 

	gtav.count_installed = gtav.count_mods(gtav.path)
	rdr2.count_installed = rdr2.count_mods(rdr2.path)
	gtaiv.count_installed = gtaiv.count_mods(gtaiv.path)

	gtav.count_backup = gtav.count_mods(gtav.backup_dir)
	rdr2.count_backup = rdr2.count_mods(rdr2.backup_dir)
	gtaiv.count_backup = gtaiv.count_mods(gtaiv.backup_dir)

	print(" ")
	print("-------------------------------------- RAGE Mod Manager ---------------------------------------\n")
	print("          GAME                                MODS INSTALLED             BACKUP FOLDER         \n")
	print("  1) GTA V" + "                                         " + str(gtav.count_installed) + "                          " + str(gtav.count_backup) + "\n")
	print("  2) Red Dead Redemption 2" + "                         " + str(rdr2.count_installed) + "                          " + str(rdr2.count_backup) + "\n")
	print("  3) GTA IV" + "                                        " + str(gtaiv.count_installed) + "                          " + str(gtaiv.count_backup) + "\n")
	print("  4) Exit\n")
	print("-----------------------------------------------------------------------------------------------")
	print(" ")
	choice = int(input("Select a game or Exit: "))
	os.system("cls")



def option_menu():
	global current_game
	global option
	print(" ")
	print(current_game.header)
	print("  1) Remove mods from game folder\n")
	print("  2) Install mods to game folder\n")
	print("  3) Display currently installed mods\n")
	print("  4) Set game directory location\n")
	print("  5) Delete installed mods\n")
	print("  6) Delete mods backup\n")
	print("  7) Go back to main menu\n")
	print("----------------------------------------------------------------")
	print(" ")
	option = int(input("Select an option: "))
	os.system("cls")




main_menu()
while choice != 4:
    

    if choice == 1:
    	current_game = gtav
    elif choice == 2:
    	current_game = rdr2
    elif choice == 3:
    	current_game = gtaiv
    else:
        a = input("Invalid game option. Press enter to exit: ")
        exit()

    option_menu()
    if option == 1:
    	# Transfer mods from game directory to backup directory
    	transfer_mods(current_game.path, current_game.backup_dir, current_game.files, False)
    elif option == 2:
    	# Transfer mods from backup directory to game directory
    	transfer_mods(current_game.backup_dir, current_game.path, current_game.files, True)
    elif option == 3:
    	# Print installed mods
    	current_game.print_installed_mods()
    elif option == 4:
    	# Set game path
    	set_game_dir(current_game.conf)
    	read_game_directories()
    	update_directories()
    elif option == 5:
    	# Delete mods from game directory
    	current_game.delete_mods(current_game.path)
    elif option == 6:
    	# Delete mods from backup directory
    	current_game.delete_mods(current_game.backup_dir)
    elif option == 7:
    	print("Going back to main menu...")
    else:
    	a = input("Invalid option. Press enter to exit: ")
    	exit()
    
    main_menu()

exit()