from flask import Flask, jsonify
import psycopg
import os

app = Flask(__name__)

# chrome://net-internals/#sockets

@app.route('/')
def index():
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    # Use DATABASE_URL
    with psycopg.connect("postgresql://postgres:ZrOeOthYCMBaRXOKbQvmgnOVSVosAGnf@roundhouse.proxy.rlwy.net:21371/railway") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute("""
                CREATE TABLE test23 (
                    id serial PRIMARY KEY,
                    num integer,
                    data text)
                """)
            

            # Make the changes to the database persistent
            conn.commit()
    return response

@app.route('/selector')
def select():
   
    # Use DATABASE_URL
    with psycopg.connect("postgresql://postgres:ZrOeOthYCMBaRXOKbQvmgnOVSVosAGnf@roundhouse.proxy.rlwy.net:21371/railway") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            postgreSQL_select_Query = "select * from test"

            cur.execute(postgreSQL_select_Query)
            print("Selecting rows from mobile table using cursor.fetchall")
            mobile_records = cur.fetchall()

            print("Print each row and it's columns values")
            for row in mobile_records:
                print("Id = ", row[0], )
                print("Model = ", row[1])
                print("Price  = ", row[2], "\n")
                
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/tester')
def fixer():
    return jsonify({"Choo Choo": "test rioute for tester nest","servicepass":"test"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
