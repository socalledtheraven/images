import os, re, itertools, shutil
import zipfile

def unzip(file):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall("./furf") # extracts the starting furf zip


def flatten(directory):
    all_files = []
    for root, _dirs, files in itertools.islice(os.walk(directory), 1, None):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    for filename in all_files:
        shutil.copy2(filename, directory)
        os.remove(filename)  # flattens all files to the same folder


def main(path):
    directory = os.fsencode(path)
    image_files = {}

    for file in os.listdir(directory):
        filename = os.fsdecode(file) # iterates through all the files
        print("first " + filename)
        if filename.endswith(".properties"):
            with open(f"{path}/{filename}", "r") as property_file: # checks for .properties files
                for line in property_file.readlines():
                    if "nbt.ExtraAttributes.id" in line: 
                        id = line.replace("nbt.ExtraAttributes.id=", "").upper() + ".png" # checks for the skyblock id and combines it with the path
                        if re.search("[A-Z_]", id):
                            image_files[path + filename.replace(".properties", ".png")] = path + id # renames the files after dealing with underscores

    for filename in image_files.keys():
        print("second " + filename)
        try:
            os.rename(filename, image_files[filename]) # renames them
        except:
            continue

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print("third " + filename)
        try:
            if not filename.endswith(".png") and filename not in list(image_files.values()):
                os.remove(path + filename) # removes any irrelevant files
        except:
            continue
        
    shutil.rmtree(f"{path}assets")


def rename(path):
    directory = os.fsencode(path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        if extension1.isupper():
            os.rename(f"{path}/{filename}", f"{path}/{right_filename}")


def full_process(file, path):
    unzip(file)
    flatten(path)
    main(path)

# rename("./furf")
full_process("./4lFurfSky_6lReborn_8lFULL.zip", "./furf/")
