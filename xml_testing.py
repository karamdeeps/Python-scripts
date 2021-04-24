from io import StringIO
from lxml import etree

def xml_test():
    xml_data = ''' <etc:ReqTagDetails xmlns:etc="http://kama.org/etc/schema/"><Head ver="1.0" ts="2020-06-10T11:18:22" orgId="STPZ" msgId="00000000000000000555" /><Txn id="00000000000000000555" note="" refId="" refUrl="" ts="2020-06-10T11:10:22" type="FETCH" orgTxnId=""><Vehicle TID="" vehicleRegNo="" tagId="" /></Txn></etc:ReqTagDetails>'''
    
    xml = StringIO(xml_data)
    valid_xml = etree.parse(xml)

    xml_schema = etree.parse('xml_schema.xsd')
    xml_validator = etree.XMLSchema(xml_schema)

    is_valid = xml_validator.validate(valid_xml)
    
    print("XML Data - ",valid_xml)
    print(" ")
    print("schema - ", xml_validator)
    print(" is_valid = ",is_valid)
    xml_validator.assertValid(valid_xml)

#    for i in tree.iter():
#        print(i.tag,' - ', i.attrib)


xml_test()
