from zeep import Client #importando a biblioteca zeep (https://docs.python-zeep.org/en/master/)

client = Client('http://www.SoapClient.com/xml/SoapResponder.wsdl')
result = client.service.Method1('hello', 'world')
print(result)