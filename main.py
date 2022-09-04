import os, re, itertools, shutil


def flatten(directory):
    all_files = []
    for root, _dirs, files in itertools.islice(os.walk(directory), 1, None):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    for filename in all_files:
        shutil.copy2(filename, directory)
        os.remove(filename)


def main(path):
    directory = os.fsencode(path)
    image_files = {}

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print("first " + filename)
        if filename.endswith(".properties"):
            with open(f"{path}/{filename}", "r") as property_file:
                for line in property_file.readlines():
                    if "nbt.ExtraAttributes.id" in line:
                        id = line.replace("nbt.ExtraAttributes.id=", "") + ".png"
                        if re.search("[A-Z_]", id):
                            image_files["./furf/" + filename.replace(".properties", ".png")] = "./furf/" + id

    for filename in image_files.keys():
        print("second " + filename)
        try:
            os.rename(filename, image_files[filename])
        except:
            continue

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print("third " + filename)
        try:
            if not filename.endswith(".png") and filename not in list(image_files.values()):
                os.remove("./furf/" + filename)
        except:
            continue


def rename(path):
    directory = os.fsencode(path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        if extension1.isupper():
            os.rename(f"{path}/{filename}", f"{path}/{right_filename}")


# rename("./furf")
