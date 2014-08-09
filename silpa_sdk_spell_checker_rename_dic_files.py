import os

dir_path = "./src/main/res/raw"

for filename in os.listdir(dir_path):
    new_filename = filename.lower()
    new_filename = new_filename.replace('-', '_')
    new_filename = "silpa_sdk_spell_check_dic_" + new_filename;

    os.rename(dir_path + "/" + filename, dir_path + "/" + new_filename)

