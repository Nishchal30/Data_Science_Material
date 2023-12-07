import pymongo

#create a connection with Mongo DB from below codd

client = pymongo.MongoClient("mongodb+srv://Nishchal30:Nishchal30@cluster0.9omin78.mongodb.net/")
db = client.test
print(db)


dict = {
    "name" : "abc",
    "surname" : "xyz",
    "email" : "abc@gmail.com"
} # this is called a document in Mongo DB

List_of_records = [
    {
        'company' : "ineuron",
        'name' : "abc",
    },
    {
        'company' : "ineuron",
        'name' : "xyz",
    },
    {
        'company' : "ineuron",
        'name' : "pqr",
    },

]

data = {"packetType":"D",
        "data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":638,"batteryVoltageStable":"ahd","batteryVoltageOff":"12.42",
                                 "batteryCrankParamTN":"-0.08","batteryCrankParamVN":"rgvf","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"fdhf","batteryCrankParamTT":"-0.00008",
                                 "batteryCrankParamV0":"jbwdk","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36",
                                 "batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99",
                                 "vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00",
                                 "coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":637,
                                 "imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[3567],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]
                },
        "header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":344,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification",
                "pomVer":"1.0","headerVer":"V6","timestamp":637,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416",
                "deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"
                }
}



db1 = client['mongotest'] # Here we have created a database called Mongotest
collection = db1['test'] # The tables inside the database called as collections, and we have created one collection as test

# collection.insert_one(dict)
# collection.insert_many(List_of_records)
# collection.insert_one(data)

collection1 = db1['new_collection']  # Created 2nd collection inside the same database
# collection1.insert_one(data)

records = collection.find() # we can find all the records from that collection using .find() and we can iterrate on it
for i in records:
    print(i)