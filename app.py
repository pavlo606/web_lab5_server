from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
import json

INSECT_MODEL = ["id", "name", "species", "number_of_legs", "has_wings", "is_dangerous", "age"]

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>Insects</h1>"

@app.route("/insects", methods=["GET", "POST", "PUT", "DELETE"])
@cross_origin()
def insects():
    if request.method == "GET":
        limit = request.args.get("limit", type=int)
        page = request.args.get("page", type=int)
        insect_id = request.args.get("id", type=int)

        with open("insects.json", "r") as file:
            insects = json.load(file)

        if limit != None:
            print(limit, type(limit))
            if page != None:
                print(page, type(page))
                return insects[(page * limit):(page * limit) + limit]

            return insects[:limit]
        
        if insect_id != None:
            for insect in insects:
                if insect["id"] == insect_id:
                    return insect
            
            return {"message": "Record doesn't exists"}, 404

        return insects
    
    elif request.method == "POST":
        form_data = request.json

        obj = {}

        for key in INSECT_MODEL:
            obj.update({key: form_data.get(key)})

        with open("insects.json", "r") as file:
            insects = json.load(file)

        for insect in insects:
            if insect["id"] == obj["id"] or obj["id"] == None:
                abort(400)

        insects.append(obj)
        with open("insects.json", "w") as file:
            json.dump(insects, file)

        return insects
    
    elif request.method == "PUT":
        data = request.json

        obj = {}
        
        for key in INSECT_MODEL:
            obj.update({key: data.get(key)})

        with open("insects.json", "r") as file:
            insects = json.load(file)

        for insect in insects:
            if insect["id"] == obj["id"]:
                insect.update(obj)

                with open("insects.json", "w") as file:
                    json.dump(insects, file)

                return insects
            
        return {"message": "Record doesn't exists"}, 404
    
    elif request.method == "DELETE":
        insect_id = request.args.get("id")

        with open("insects.json", "r") as file:
            insects = json.load(file)

        for i, insect in enumerate(insects):
            if insect["id"] == insect_id:
                del insects[i]
                with open("insects.json", "w") as file:
                    json.dump(insects, file)

                return insects
            
        
        return {"message": "Record doesn't exists"}, 404
    