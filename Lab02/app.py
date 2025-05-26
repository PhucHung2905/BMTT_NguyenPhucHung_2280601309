from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Route cho trang chủ
@app.route("/")
def home():
    return render_template("index.html")

# Route cho giao diện Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

# Route xử lý mã hóa
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"""
    <p><strong>Text:</strong> {text}</p>
    <p><strong>Key:</strong> {key}</p>
    <p><strong>Encrypted Text:</strong> {encrypted_text}</p>
    """

# Route xử lý giải mã
@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"""
    <p><strong>Text:</strong> {text}</p>
    <p><strong>Key:</strong> {key}</p>
    <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
    """


# Route cho giao diện Vigenere Cipher
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

# Route xử lý mã hóa Vigenere
@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.encrypt(text, key)
    return f"""
    <p><strong>Text:</strong> {text}</p>
    <p><strong>Key:</strong> {key}</p>
    <p><strong>Encrypted Text:</strong> {encrypted_text}</p>
    """

# Route xử lý giải mã Vigenere
@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.decrypt(text, key)
    return f"""
    <p><strong>Text:</strong> {text}</p>
    <p><strong>Key:</strong> {key}</p>
    <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
    """

# Hàm main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)