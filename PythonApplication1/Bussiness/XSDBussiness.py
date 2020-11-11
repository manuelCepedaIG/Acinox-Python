from lxml import etree

class XSDClass:
	def ValidateXML(name, date):

		print("Validating XML")

		xml_root = etree.parse('sociedades.xml')
		xsd_root = etree.parse('XSD/sociedades.xsd')
		schema = etree.XMLSchema(xsd_root)
		schemaValid = schema.validate(xml_root)
		if not schemaValid:
			log = schema.error_log
			error = log.last_error
			#schema.assertValid(xml_root)
			#schemaassert_(xml_root)
			#print(error.domain_name)
			#print(error.type_name)
			#print(error)
			print('Error found in file:', error.filename)
			print('Error found in column:', error.column)
			#print(error.domain)
			#print(error.domain_name)
			#print(error.level)
			#print(error.level_name)
			print('Error found in line:', error.line)
			print(error.message)
			print('Error found in path:', error.path)
			#print(error.type)
			#print(error.type_name)
