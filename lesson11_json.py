import json

# Data to be written

dictionary ={
    "name": "Ylia",
    "rollno": 56,
    "FPGA": 8.7,
    "telephone": "+791812345678"
}

#
json_object = json.dumps(dictionary)

#Writing to sample.json

with open("sample.json", "w") as outfile:
    outfile.write(json_object)

with open("sample.json", "r") as openfile:
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))