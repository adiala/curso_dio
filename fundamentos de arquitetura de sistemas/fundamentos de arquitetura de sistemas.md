# Fundamentos de arquitetura de sistemas

## Vantagens e desenvolvimento de web services

### O que são web services

- são soluções para  aplicações de comunicarem independente de linguagem
- são API's que se comunicam por meio de redes sobre o protocolo HTTP
- xml e json são as linguagens de marcação mais utilizadas

#### Vantagens

- linguagem comum
- Integração
- reutilização de implementação
- segurança
- custos

#### Principais tecnologias

- soap

- rest

- json

- xml

  ------

### Estrutura SOAP

#### O que é o SOAP

- Soap - Simple Object Access Protocol
- É um protocolo baseado em XML para acessar serviços web principalmente por HTTP
- SOAP é um meio de transporte genérico que independe de linguagem para se comunicar.

#### Vantagens

- Permite integração independente de linguagem
- É independente de plataforma e software
- Meio de transporte genérico, pode ser usado por outros protocolos além no HTTP

#### Estrutura

<img src="https://www.guru99.com/images/3-2016/032316_0711_SOAPSimpleO1.png" alt="SOAP Web Services Tutorial: Simple Object Access Protocol EXAMPLE" style="zoom: 67%;" />

#### SOAP message

![SOAP Web Services Tutorial: Simple Object Access Protocol EXAMPLE](https://www.guru99.com/images/3-2016/032316_0711_SOAPSimpleO2.png)

#### XML

- XML - Extensible Markup Language
- A XML serve para facilitar a separação de conteúdo
- Não tem limitação de criação de tags
- linguagem comum para integrações entre aplicações

#### WSDL - Web Services Description Languages

- Usado para descrever web services, funciona como um contrato do serviço
- O "contrato" do web service é descrito por meio de um arquivo XML contendo especificações de acesso, operações, métodos e etc.

#### XSD - XML schema definition

- É um schema no formato XML usado para definir a estrutura de dados que será validada no XML
- O XSD funciona como uma documentação de como deve ser montado o SOAP message (XML) que será enviado através de web service

#### Exemplo SOAP

```xml
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<definitions xmlns:tns="http://www.SoapClient.com/xml/SoapResponder.wsdl" xmlns:xsd1="http://www.SoapClient.com/xml/SoapResponder.xsd" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns="http://schemas.xmlsoap.org/wsdl/" name="SoapResponder" targetNamespace="http://www.SoapClient.com/xml/SoapResponder.wsdl">
<types>
<schema xmlns="http://www.w3.org/1999/XMLSchema" targetNamespace="http://www.SoapClient.com/xml/SoapResponder.xsd"> </schema>
</types>
<message name="Method1">
<part name="bstrParam1" type="xsd:string"/>
<part name="bstrParam2" type="xsd:string"/>
</message>
<message name="Method1Response">
<part name="bstrReturn" type="xsd:string"/>
</message>
<portType name="SoapResponderPortType">
<operation name="Method1" parameterOrder="bstrparam1 bstrparam2 return">
<input message="tns:Method1"/>
<output message="tns:Method1Response"/>
</operation>
</portType>
<binding name="SoapResponderBinding" type="tns:SoapResponderPortType">
<soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
<operation name="Method1">
<soap:operation soapAction="http://www.SoapClient.com/SoapObject"/>
<input>
<soap:body use="encoded" namespace="http://www.SoapClient.com/xml/SoapResponder.xsd" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
</input>
<output>
<soap:body use="encoded" namespace="http://www.SoapClient.com/xml/SoapResponder.xsd" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
</output>
</operation>
</binding>
<service name="SoapResponder">
<documentation>A SOAP service that echoes input parameters in the response</documentation>
<port name="SoapResponderPortType" binding="tns:SoapResponderBinding">
<soap:address location="http://www.soapclient.com/xml/soapresponder.wsdl"/>
</port>
</service>
</definitions>
```

#### Exemplo do SOAP implementado em Python

```python
from zeep import Client #importando a biblioteca zeep (https://docs.python-zeep.org/en/master/)

client = Client('http://www.SoapClient.com/xml/SoapResponder.wsdl')
result = client.service.Method1('hello', 'world')
print(result)
```

[]: https://docs.python-zeep.org/en/master/	"Biblioteca Zeep"

------

### REST, API e JSON

#### Rest - Representational State Transfer

- É um estilo de arquitetura de software que define a imprementação de um serviço web. Não é um protocolo como o SOAP.
- Pode trabalhar com diversos formatos como XML e JSON

##### Vantagens

- Arquitetura de fácil compreensão
- Permite integrações entre aplicações e também entre cliente e servidor em páginas web e aplicações
- Utiliza métodos HTTP para definir a operação que está sendo efetuada

##### Estrutura

<img src="https://www.astera.com/wp-content/uploads/2020/01/rest.png" alt="REST API: Definition, Working, Benefits, and Design Principles | Astera" style="zoom: 67%;" />

#### API - Application Programming Interface

São conjuntos de rotinas documentados e disponibilizados por uma aplicação para que outras aplicações possam consumir suas funcionalidades

#### Principais métodos HTTP

- **GET** - Solicita a representação de um recurso
- **POST** - Solicita a criação de um recurso
- **DELETE** - Solicita a exclusão de um recurso
- **PUT** - Solicita a atualização de um recurso

#### JSON - JavaScript Object Notation

- Formatação leve utilizada para troca de mensagens entre sistemas
- Usa uma estrutura de chave e valor e também de listas ordenadas

