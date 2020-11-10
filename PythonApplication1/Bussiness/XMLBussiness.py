from Models import Sociedad
from Models import Cliente
from io import BytesIO
from xml.etree import ElementTree
import xml.dom.minidom

class XMLClass:

    def GenerateXML(sqlResult, entity, fecha):
        if entity == "sociedades":
            sociedadList = []
            sociedadList = XMLClass.MappingSociety(sqlResult)
            XMLClass.GenerateXMLSociedades(sociedadList);

        else:
            MappingDataBySociety(typeOfQuery, sqlResult , codeEntity, fecha)

        
    def MappingSociety(sqlResult):
        listSoc = []  

        for item in sqlResult:
            listSoc.append(Sociedad.Sociedad(item[0], item[1], item[2], item[3]))
        
        return listSoc


    def GenerateXMLSociedades(sociedadList):
        document = ElementTree.Element('sociedades')
        
        for sociedad in sociedadList:
            socNode = ElementTree.SubElement(document, 'soc')

            nodeCod = ElementTree.SubElement(socNode, 'cod')
            nodeCod.text = sociedad.Cod

            nodeRazons = ElementTree.SubElement(socNode, 'razons')
            nodeRazons.text = sociedad.Razons

            nodeNif = ElementTree.SubElement(socNode, 'nif')
            nodeNif.text = sociedad.Nif

            nodeCodmoneda = ElementTree.SubElement(socNode, 'codmoneda')
            nodeCodmoneda.text = sociedad.Codmoneda
            
        et = ElementTree.ElementTree(document)
        f = BytesIO()
        et.write(f, encoding='utf-8', xml_declaration=True) 
        #print(f.getvalue())  # your XML file, encoded as UTF-8

        parent = et.getroot()
        et2 = xml.dom.minidom.parseString(ElementTree.tostring(parent)).toprettyxml()
        
        with open("test.xml", "w") as files : 
            files.write(et2)



    def MappingDataBySociety(typeOfQuery, sqlResult , codeEntity, fecha):
        switch = {
            "clientes" : fClientes(sqlResult, entity, fecha)
        }
        return switch.get(typeOfQuery, default())


    def Default():
        pass


    def fClientes(sqlResult, entity, fecha):
        clientesList = mapingClientes(sqlResult)
        GenerateXMLClientes(clientesList, codeEntity, fecha);


    def MapingClientes(sqlResult):
        listCliente = []  
        for item in sqlResult:
            listCliente.append(
                Cliente.Cliente(
                    item[0],
                    item[1],
                    item[2],
                    item[3],
                    item[4],
                    item[5],
                    item[6],
                    item[7],
                    item[8],
                    item[9],
                    item[10],
                    item[11],
                    item[12],
                    item[13],
                    item[14],
                    item[15],
                    item[16],
                    item[17],
                    item[18],
                    item[19],
                    item[20],
                    item[21],
                    item[22],
                    item[23],
                    item[24],
                    item[25],
                    item[26],
                    item[27]
                )
            )
        return listCliente
