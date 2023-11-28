import sys
sys.path.append("D:\\Programming\\2_course\\web\\lab5_server\\web_lab5_server\\venv\\Lib\\site-packages")
from flask import Flask, request, abort, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import json
import itertools

UPLOAD_FOLDER = 'images'
ITEM_MODEL = ["id", "title", "text", "image", "price", "category", "quantity", "rating"]

app = Flask(__name__)
CORS(app)

mysql = MySQL()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# MySQL configs
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'pavlo'
app.config['MYSQL_PASSWORD'] = 'it31013107606'
app.config['MYSQL_DB'] = 'arduino_shop'
mysql.init_app(app)

def is_true(value):
    return value.lower() == "true"

def parse_item_list(raw_list) -> list[dict]:
    raw_list = list(raw_list)
    final_list = []
    for item in raw_list:
        temp_dict = {}
        for key, value in zip(ITEM_MODEL, item):
            try:
                temp_dict[key] = json.loads(str(value))
            except json.decoder.JSONDecodeError:
                temp_dict[key] = value

        final_list.append(temp_dict)
    
    return final_list

@app.route("/")
def home():
    return "<h1>Arduino</h1>"

sortingFunctions = {
    "price": lambda a: a["price"],
    "name": lambda a: a["title"],
    "rating": lambda a: a["rating"]
}

@app.route("/items", methods=["GET"])
@cross_origin()
def get_items():
    sort = request.args.get("sort", type=str)
    filter_option = request.args.get("filter", type=str)
    reverse_sort = request.args.get("reverse_sort", type=is_true)
    search = request.args.get("search", type=str)
    limit = request.args.get("limit", type=int)
    item_id = request.args.get("id", type=int)

    cursor = mysql.connection.cursor()
    if item_id:
        cursor.execute(f''' SELECT * FROM goods WHERE id = {item_id}''')
    else:
        cursor.execute(''' SELECT * FROM goods ''')
    items = parse_item_list(cursor.fetchall())
    mysql.connection.commit()
    cursor.close()

    if sort:
        items = list(sorted(items, key=sortingFunctions[sort]))

    if filter_option and not filter_option == "all":
        items = list(filter(lambda a: a["category"] == filter_option, items))
    
    if search:
        for i in items.copy():
            # if not (search.lower() in i["title"].lower() or search.lower() in i["text"].lower()):
            if search.lower() not in i["title"].lower():
                items.remove(i)

    if reverse_sort:
        items.reverse()

    if limit:
        items = items[0:limit]

    return items

@app.route("/items/<item_id>", methods=["PUT"])
@cross_origin()
def put_item(item_id):
    form_data = dict(request.form)
    try:
        image = request.files["myfile"]
        filename = secure_filename(image.filename)
        image.save(f"images/{filename}")
    except:
        pass
    
    request_data = [f"{key}='{value}'" for key, value in form_data.items()]
    
    cursor = mysql.connection.cursor()
    cursor.execute(f''' 
    UPDATE goods
    SET {",".join(request_data)}
    WHERE id = {item_id};
    ''')
    mysql.connection.commit()
    cursor.close()

    return "Succesfull"

@app.route("/items/category", methods=["GET"])
@cross_origin()
def get_categories():
    cursor = mysql.connection.cursor()
    cursor.execute(f''' 
    SELECT DISTINCT category FROM arduino_shop.goods;
    ''')
    items = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()

    return list(itertools.chain(*items))

@app.route("/items/image/<name>", methods=["GET"])
@cross_origin()
def get_image(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route("/items/create", methods=['POST'])
@cross_origin()
def create_item_post():
    form_data = dict(request.form)
    image = request.files["myfile"]
    filename = secure_filename(image.filename)
    image.save(f"images/{filename}")

    insert_data = ''
    for key in form_data.keys():
        value = form_data[key]
        insert_data += f"'{value}',\n"
    insert_data += f"'{filename}'"

    # with open("sql_scripts.sql", "a") as file:
    #     file.write("\n(\n")
    #     file.writelines(insert_data.split('\r'))
    #     file.write("\n)")

    cursor = mysql.connection.cursor()
    cursor.execute(f''' 
    INSERT INTO goods 
    (`title`, `product_description`, `category`, `price`, `quantity`, `rating`, `image`)
    VALUES ( {insert_data} )
    ''')
    mysql.connection.commit()
    cursor.close()

    return render_template("input_form.html")

@app.route("/items/create", methods=['GET'])
@cross_origin()
def create_item_get():
    return render_template("input_form.html")