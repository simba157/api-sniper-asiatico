from flask import Flask, request, jsonify
import time, threading

app = Flask(__name__)
sinais = []             # memória simples em RAM
TOKEN = "CHAVE_SUPER_SECRETA"  # substitua por algo forte

@app.route("/sinais", methods=["GET", "POST"])
def sinais_endpoint():
    global sinais
    if request.method == "POST":
        if request.args.get("token") != TOKEN:
            return "Unauthorized", 401
        dados = request.get_json(force=True)
        sinais = dados   # sobrescreve lista
        return "OK", 200

    # GET → painel consome
    return jsonify(sinais)

# limpeza de sinais velhos a cada 10 minutos
def limpar():
    global sinais
    while True:
        time.sleep(600)
        sinais = []

threading.Thread(target=limpar, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
