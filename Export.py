import os
import pycdlib

# you can use this file to extract the contents of your (legally acquired) Budokai3 iso.
# this is really only useful for modding reasons. It is NOT recommended to extract the files otherwise.
# SLUS_209.98 mentions many items that aren't used in the final game, such as...
# Yamhan (Yamcha + Tien fusion), Gokule (Goku + Hercule fusion), Buu with Various Absorptions, Guldo/Jeice/Burter/Dodoria/Zerbon/Android 19
# These are probably reused from Budokai 2
# TOUR MODE might refer to Dragon World...
# todo: investigate modding them back in

path = 'Dragon Ball Z - Budokai 3.iso' # replace with path to your iso

def extract_iso(iso_path, destination_path):
    iso = pycdlib.PyCdlib()
    iso.open(iso_path)

    os.makedirs(destination_path, exist_ok=True)

    for root, dirs, files in iso.walk(iso_path="/"):

        current_dest_path = str(os.path.join(destination_path, root.lstrip('/')))

        for d in dirs:
            os.makedirs(os.path.join(current_dest_path, d), exist_ok=True)

        for f in files:
            source_file_path = str(os.path.join(root, f))
            # all files are given the ";1" designation, which in the ISO format, implies "Version 1" . Therefore it's not required
            f = f[0:-2]
            dest_file_path = os.path.join(current_dest_path, f)

            with open(dest_file_path, 'wb') as dest_file:
                iso.get_file_from_iso(local_path=dest_file_path, iso_path=source_file_path)

    iso.close()

export_path = "export"
print(os.path.curdir)
extract_iso(path, export_path)
