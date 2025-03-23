from flask import Flask, request, jsonify

app = Flask(__name__)

providersList = {
        0 : "Amazon",
        1 : "OpenAI",
        2 : "Microsoft",
        3 : "Google",
        4 : "Meta"
    }

@app.route("/")
def Greeting():
    return "Hello World!"

@app.route("/get-providers/<provider_id>")
def Get_Provider(provider_id):
    response = {
        "data":{},
        "message":"Successfully retrieved the provider."
    }

    if(int(provider_id) < 0):
        response["message"] = "Provider id cannot be a negative value."
        return jsonify(response),400
    elif(int(provider_id) > 4):
        response["message"] = "No provider found with the given id."

    response["data"] = {
        "provider" : providersList.get(int(provider_id), "NA"),
        "id" : provider_id
    }
    return jsonify(response),200

@app.route("/add-provider", methods=["POST"])
def Add_Provider():
    data = request.get_json()
    new_id = max(providersList.keys()) + 1
    new_provider = data["provider"]

    response = {
        "id" : new_id,
        "provider" : new_provider
    }
    return (jsonify(response)),200


if(__name__ == "__main__"):
    app.run(debug=True)