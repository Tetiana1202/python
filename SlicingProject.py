property_transfer_xml = """<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento'; 
//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento'; 
//urn:multiCall/sessionId['?']</con:targetPath>""" 
 
start_pos = property_transfer_xml.find("<con:targetType>") 
end_pos = property_transfer_xml.find("</con:targetType>") 
 
result = property_transfer_xml[start_pos:end_pos].split(">")[1].strip() 
 
print("The value of con:targetType attribute is:", result)