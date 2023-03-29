from urllib.request import urlopen
import json
doc_id=2
diagnosis='Pulmonary embolism'
total_pulse=0
count=0
for i in range(10):
    with urlopen("https://jsonmock.hackerrank.com/api/medical_records?page={0}".format(i)) as response:
        source=response.read()
    
    data=json.loads(source)
    for record in data['data']:
        print(record)
        if record['diagnosis']['name']==diagnosis and record['doctor']['id']==doc_id:
            total_pulse+=record['vitals']['pulse']
            count+=1
print(total_pulse//count)

    

    


