from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [
    {
        "id": 1,
        "author": "new man",
        "language": "bangla",
        "title": "joy bangla"
    }
]


@app.route('/books/get', methods=['GET'])
def books():
    if request.method == 'GET':
        if len(book_list) > 0:
            return jsonify(book_list)
        else:
            'Nothing Found', 404


@app.route('/books/post', methods=['POST'])
def books2():

    if request.method == 'POST':

        new_author = request.get_json("author")
        new_lan = request.get_json("language")
        new_title = request.get_json("title")
        iD = book_list[-1]["id"]+1

        new_object = {
            "id": iD,
            "author": new_author,
            "language": new_lan,
            "title": new_title
        }
        book_list.append(new_object)
        return jsonify(book_list)
        # except:
        #     print("the post method dosen't working")


if __name__ == '__main__':
    app.run()
