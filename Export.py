import os
import pycdlib

# you can use this file to extract the contents of your (legally acquired) Budokai3 iso.
# this is really only useful for modding reasons. It is NOT recommended to extract the files otherwise.

path = 'Dragon Ball Z - Budokai 3.iso' # replace with path to your iso

def extract_iso(iso_path, destination_path):
    iso = pycdlib.PyCdlib()
    iso.open(iso_path)

    os.makedirs(destination_path, exist_ok=True)

    for root, dirs, files in iso.walk(iso_path="/"):
        from pycdlib import pycdlibexception
        print("Dirname:", root, ", Dirlist:", dirs, ", Filelist:", files)

        current_dest_path = str(os.path.join(destination_path, root.lstrip('/')))

        for d in dirs:
            os.makedirs(os.path.join(current_dest_path, d), exist_ok=True)

        for f in files:
            source_file_path = str(os.path.join(root, f))
            print("file path on iso should be...", source_file_path)
            # all files are given the ";1" designation, which in the ISO format, implies "Version 1" . Therefore it's not required
            # f = f[0:-2]
            print(f'f is {f}')
            dest_file_path = os.path.join(current_dest_path, f)

            with open(dest_file_path, 'wb') as dest_file:
                try: 
                    iso.get_file_from_iso(local_path=dest_file_path, iso_path=source_file_path)
                except pycdlibexception.PyCdlibException as e:
                    print(f'File that errored was: {dest_file.name}')
                    print(f'error was: {e}')
    iso.close()

export_path = "export"
print(os.path.curdir)
extract_iso(path, export_path)