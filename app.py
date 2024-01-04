from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

import book_review

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


class UppercaseText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return jsonify({"text": text.upper()})


class AddRecord(Resource):
    def post(self):
        """
        This method responds to the POST request for adding a new record to the DB table.
        ---
        tags:
        - Records
        parameters:
            - in: body
              name: body
              required: true
              schema:
                id: BookReview
                required:
                  - Book
                  - Rating
                properties:
                  Book:
                    type: string
                    description: the name of the book
                  Rating:
                    type: integer
                    description: the rating of the book (1-10)
        responses:
            200:
                description: A successful POST request
            400:
                description: Bad request, missing 'Book' or 'Rating' in the request body
        """

        data = request.json
        print(data)

        if data is not None:
            success = True
        else:
            success = False

        if success:
            return {"message": "Record added successfully"}, 200
        else:
            return {"message": "Failed to add record"}, 500


api.add_resource(AddRecord, "/add-record")
api.add_resource(UppercaseText, "/uppercase")

if __name__ == "__main__":
    app.run(debug=True)
