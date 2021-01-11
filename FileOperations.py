import glob

import XMLParser


def read_and_store_input(input_path):
    # initialize dictionary
    data = {}
    # read file names from the input directory
    input_files = glob.glob(input_path+'*.xml')
    for file_path in input_files:
        data[file_path.split("\\")[len(file_path.split("\\")) - 1]] = XMLParser.GetMapOfXml(file_path)

    return data


#data = read_and_store_input("C:\\Users\\Enes Recep ÇINAR\\PycharmProjects\\metu-cogs-520-TED-talks-emotions\\annotated\\")
#for file in data:
#    print(file + " : " + str(data[file]))