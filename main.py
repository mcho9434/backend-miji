from flask import Flask, jsonify
import os
from notion_client import Client

PAGE_ID = "6fe8589f772b4fee8a0b094ebf19cc5d"
NOTION_TOKEN = "secret_9tJzDXlU8gHV5UnjKQclS5zeBELZ2RjNWzH2run5viB"

app = Flask(__name__)

# chrome://net-internals/#sockets

@app.route('/')
def index():
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/tester')
def fixer():
    def fetchDB(notion):
        payload=[]
        try:
            dbData = notion.databases.query(
                **{
                    "database_id": PAGE_ID,
                    "sorts": [
                        {
                            "property": "Date",
                            "direction": "descending",
                        },
                    ],
                }
            )
            # print(dbData)
            for i in dbData["results"]:
                props = i["properties"]
                print("Title: ", props["Title"]["title"][0]["plain_text"])
                print("Date: ", props["Date"]["date"]["start"])
                print("URL: ", i["url"])
                uuid = i["url"][-32:]
                print(len(uuid), " | ", uuid)
                pgData = notion.blocks.children.list(
                    **{
                        "block_id": uuid,
                        "page_size": 50,

                    }
                )
                payload.append(props["Title"]["title"][0]["plain_text"])
                print(pgData)
                print("--------")
        except Exception as e:
            print(e)
        return payload
    notion = Client(auth=NOTION_TOKEN)

    rawDB = fetchDB(notion)

    return jsonify({"Choo Choo": "test rioute for tester nest", "servicepass":rawDB})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
