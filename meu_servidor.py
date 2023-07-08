from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import keyboard
import sys


class MeuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        mensagem = "Olá! Este é o meu servidor HTTP simples."
        self.wfile.write(mensagem.encode('utf-8'))


def run():
    host = 'localhost'
    porta = 8000

    server = HTTPServer((host, porta), MeuHandler)
    print(f"Servidor rodando em http://{host}:{porta}")

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

    try:
        keyboard.wait('esc')
    except KeyboardInterrupt:
        pass

    server.shutdown()
    server.server_close()
    print("Servidor encerrado.")


if __name__ == '__main__':
    run()
