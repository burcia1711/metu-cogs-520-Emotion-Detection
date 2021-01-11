import xml.etree.ElementTree as ET


def GetMapOfXml(input_path):
    root = ET.parse(input_path).getroot()
    parts = ["dikkat", "olgu", "gözlem", "yorum", "kapanış"]
    properties = {}
    for prop in parts:
        tempStr = ""
        for type_tag in root.findall('konuşma/' + prop):
            if(prop not in properties):
                properties[prop] = []
            tempStr += " " + str(type_tag.text)
        properties[prop] = tempStr.split()
            #print(prop + " : " +str(type_tag.text))

    return properties


#result = GetMapOfXml("C:\\Users\\Enes Recep ÇINAR\\PycharmProjects\\metu-cogs-520-TED-talks-emotions\\annotated\\12.xml")
#print(result)