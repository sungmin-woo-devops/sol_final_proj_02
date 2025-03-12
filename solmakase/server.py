from flask import Flask, request, jsonify
from flask_sock import Sock
from flask_cors import CORS
import subprocess
import threading

app = Flask(__name__)
CORS(app)

sock = Sock(app)

# WebSocket 연결을 유지하는 리스트
clients = []

@sock.route('/ws')
def stream_logs(ws):
    clients.append(ws)
    print("✅ WebSocket 연결됨")
    try:
        while True:
            message = ws.receive()
            if message is None:
                break
    except Exception as e:
        print(f"❌ WebSocket Error: {e}")
    finally:
        clients.remove(ws)
        print("❌ WebSocket 연결 종료됨")

@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.json
    if not data or "command" not in data:
        return jsonify({"error": "No command provided"}), 400

    command = data["command"]
    thread = threading.Thread(target=run_command, args=(command,))
    thread.start()
    
    print(f"🚀 실행 중: {command}")
    return jsonify({"command": command})  # JSON 응답 반환

def run_command(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in iter(process.stdout.readline, ''):
        for client in clients:
            try:
                client.send(line.strip())
            except Exception as e:
                print(f"❌ WebSocket Error: {e}")
                clients.remove(client)

    process.stdout.close()
    process.wait()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
