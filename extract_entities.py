from calais import Calais
API_KEY = "djgq52vv8uufzykmnb9g7myv"
calais = Calais(API_KEY, submitter ="python-calais demo")
result = calais.analyze('''Microsoft is a big company. George Bush was the President of the United States
of America until 2009.  Barack Obama is the new President of the United States now.''')
result2 = calais.analyze('''Microsoft is a big company''')
result3 = calais.analyze('''Troubled drug development company SFBC International said on Monday it has changed its name to PharmaNet Development Group Inc. and will be traded on Nasdaq under the stock symbol "PDGI".''')
d={}
a=[]
for i in result3.entities:
    if i["_type"]=="Technology":
        a.append(i["name"])
        d["Technology"]=a;
        print d

