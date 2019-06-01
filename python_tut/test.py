from pysimplesoap.client import SoapClient
import pysimplesoap
import logging
logging.basicConfig()

client=SoapClient(wsdl="http://ws.cdyne.com/emailverify/Emailvernotestemail.asmx?wsdl",trace=True)
response = client.VerifyEmail(email="a-valid-gmail-address@gmail.com",LicenseKey="?")
print (response['VerifyEmailResult']['GoodEmail'])
print (response)