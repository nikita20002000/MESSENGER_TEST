from flask import Flask, request

app = Flask(__name__)

message_list = []


@app.route('/')
def hello_world():
    return 'Messenger Flask is running ' \
           '<br> <a herf="/status">Check status</a>'


@app.route('/status')
def status():
    return {
        'message_count': len(message_list)
    }

@app.route("/api/Messanger", methods=['POST'])
def send_message():
    msg = request.json
    print(msg)
    message_list.append(msg)
    msg_text = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Total messages: {len(message_list)} ")
    return f"Send successfully. Total messages: {len(message_list)}"


@app.route("/api/Messanger/<int:id>")
def Get_message(id):
    print(id)
    if id >= 0 and id < len(message_list):
        print(message_list[id])
        return message_list[id], 200
    else:
        return "Not found", 400


if __name__ == '__main__':
    app.run()
