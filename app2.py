from flask import Flask, request, jsonify
import sqlite3
# import json

app = Flask(__name__)

@app.route('/books', methods=['GET','POST'])
def books():
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    
    if request.method == 'GET':
        try:
            cursor1 = conn.execute("SELECT * FROM book")
            books = [
                dict(id=row[0],author=row[1],language=row[2],title=row[3])
                for row in cursor1.fetchall()
                ]
            if books is not None:
                return jsonify(books)
            
        except:
            return "def books not working"
        
    if request.method == 'POST':
        try:
            new_author = request.form["author"]
            new_language = request.form["language"]
            new_title = request.form["title"]

            sql = """INSERT INTO book (author, language, title) 
            VALUES (?, ?, ?)"""


            try:
                # cursor.execute("INSERT INTO book (author, language, title) VALUES (?, ?, ?)", (new_author, new_language, new_title))
                cursor.execute(sql, (new_author, new_language, new_title))
                conn.commit()
                return f"Book with the id:{cursor.lastrowid} created successfully", 201
            except:
                return "cur or conn not working"
        except:
            return "def books not working 2"
        
@app.route('/books/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    conn = sqlite3.connect("books.sqlite")
    cursor = conn.cursor()
    book = None
    if request.method == 'GET':
        cursor2 = cursor.execute("SELECT * FROM book WHERE id=?",(id,))
        book = [
                dict(id=row[0],author=row[1],language=row[2],title=row[3])
                for row in cursor2.fetchall()
                ]
        if book is not None:
            return jsonify(book)
        else:
            return "somting wrong in GET methode"
        
    if request.method == 'PUT':
        sql = """UPDATE book SET
            author=?,
            language=?,
            title=?
            WHERE id=?"""
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = [
            {
            "id": id,
            "author": author,
            "language": language,
            "title": title
            }
        ]

        cursor.execute(sql, (author, language, title,id))
        return jsonify(updated_book)
    if request.method == 'DELETE':
        sql = """DELETE FROM book WHERE id=?"""
        cursor.execute(sql, (id,))
        conn.commit()
        return "The book was deleted"
    # if request.method == 'POST':b
    #     request.form
    #     cursor.execute()
    #     rows = cursor.fetchall()
    #     for r in rows:
    #         book = r
    #     if book is not None:
    #         return jsonify(book)
    #     else:
    #         return "somting wrong in  methode"

# @app.route('/books/post', methods=['POST'])
# def books2():

#     if request.method == 'POST':

#         new_author = request.get_json("author")
#         new_lan = request.get_json("language")
#         new_title = request.get_json("title")
#         iD = book_list[-1]["id"]+1

#         new_object = {
#             "id": iD,
#             "author": new_author,
#             "language": new_lan,
#             "title": new_title
#         }
#         book_list.append(new_object)
#         return jsonify(book_list)
#         # except:
#         #     print("the post method dosen't working")


if __name__ == '__main__':
    app.run()