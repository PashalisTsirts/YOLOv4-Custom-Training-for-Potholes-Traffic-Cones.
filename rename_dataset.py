from pathlib import Path

def rename_photos():
    first_name = "TrfC"
    images = Path("C:/Users/pashalis/Desktop/Images")
    custom_dataset = Path("C:/Users/pashalis/Desktop/CustomDataset")
    counter = 1
    for file in images.iterdir():
        if file.is_file():
            if counter > 99:
                new_file = first_name + "00" + str(counter) + file.suffix
                file.rename(custom_dataset / new_file)
                counter += 1
            elif counter > 9:
                new_file = first_name + "000" + str(counter) + file.suffix
                file.rename(custom_dataset / new_file)
                counter += 1
            else:
                new_file = first_name + "0000" + str(counter) + file.suffix
                file.rename(custom_dataset / new_file)
                counter += 1



if __name__ == "__main__":
    rename_photos()