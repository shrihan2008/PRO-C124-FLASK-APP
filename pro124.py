from msilib.schema import Error
from flask import Flask,jsonify,request

app=Flask(__name__)
contacts=[
    {
        'id':1,
        'name':u'John',
        'contact':u'8756403921',
        'done':False
    },

    {
        'id':2,
        'name':u'Murray',
        'contact':u'9980354785',
        'done':False
    },

     {
        'id':3,
        'name':u'Diesel',
        'contact':u'8756677215',
        'done':False
    },

    {
        'id':4,
        'name':u'Petrol',
        'contact':u'7893640145',
        'done':False
    }
]

@app.route("/add-data",methods=["POST"])

def addcontact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Give ur data"
        },400)
    work={
        "id":contacts[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',' '),
        'done':False
    }

    contacts.append(work)
    return jsonify({
        'status':"succes",
        "message":"thanks for adding ur contact"
    })

@app.route('/get-data',methods=["GET"])

def getcontact():
    return jsonify({
        'data':contacts
    })

if __name__=='__main__':
    app.run(debug=True)
  