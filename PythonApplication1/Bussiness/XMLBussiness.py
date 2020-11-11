from Models import Sociedad
from Models import Cliente
from io import BytesIO
from lxml import etree
from lxml import builder

class XMLClass:

    def GenerateXML(sqlResult, entity, date):
        print("Generating XML")

        if entity == "sociedades":
            sociedadList = []
            sociedadList = XMLClass.MappingSociety(sqlResult)
            XMLClass.GenerateXMLSociedades(sociedadList);

        else:
            MappingDataBySociety(typeOfQuery, sqlResult , codeEntity, date)

        
    def MappingSociety(sqlResult):
        listSoc = []  

        for item in sqlResult:
            listSoc.append(Sociedad.Sociedad(item[0], item[1], item[2], item[3]))
        
        return listSoc


    def GenerateXMLSociedades(sociedadList):

        noNamespaceSchemaLocation = 'http://www.w3.org/2001/XMLSchema-instance'
        xsi = 'http://www.w3.org/2001/XMLSchema-instance'
        E = builder.ElementMaker( nsmap= { None: noNamespaceSchemaLocation, 'xsi': xsi })

        document = etree.Element('sociedades')
        document.attrib['{{{pre}}}noNamespaceSchemaLocation'.format(pre=xsi)] = 'sociedades'

        for sociedad in sociedadList:
            socNode = etree.SubElement(document, 'soc')

            nodeCod = etree.SubElement(socNode, 'cod')
            nodeCod.text = sociedad.Cod

            nodeRazons = etree.SubElement(socNode, 'razons')
            nodeRazons.text = sociedad.Razons

            nodeNif = etree.SubElement(socNode, 'nif')
            nodeNif.text = sociedad.Nif

            nodeCodmoneda = etree.SubElement(socNode, 'codmoneda')
            nodeCodmoneda.text = sociedad.Codmoneda
            
        et = etree.ElementTree(document)
        
        with open("sociedades.xml", "wb") as files : 
            et.write(files,  encoding="UTF-8", xml_declaration=True, pretty_print=True)


    def MappingDataBySociety(typeOfQuery, sqlResult , codeEntity, date):
        switch = {
            "clientes" : fClientes(sqlResult, entity, date)
        }
        return switch.get(typeOfQuery, default())


    def Default():
        pass


    def fClientes(sqlResult, entity, date):
        clientesList = mapingClientes(sqlResult)
        GenerateXMLClientes(clientesList, codeEntity, date);


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
