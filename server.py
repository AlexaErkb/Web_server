import settings
from threading import Thread
from pathlib import Path
from os.path import exists, sep
import datetime
import socket
import logging

types = {'html':'text/html', 'jpeg':'image/jpeg', 'png':'image/png', 'css':'text/css', 'js':'text/javascript'}

def handler(request, addr):
    try:
        file = request.split('\n')[0].split()[1][1:]
    except:
        file = 'index.html'
    if not file:
        file = 'index.html'
    path = Path(file)
    if exists(path):
        type = file.split(".")[-1]
        if type in types:
            stat = '200'
            log_info(stat, addr, path)
            with open(path, "rb") as file:
                src = file.read()
            resp = get_response(stat, 'OK', src, type)
            return resp
        else:
            stat = '403'
            text = "<h1>Error 403</h1>".encode()
            type = 'html'
            log_info(stat, addr, path)
            resp = get_response(stat, 'Forbidden', text, type)
            return resp

    elif not exists(path) or file == '':  # нет файла
        stat = '404'
        text = "<h1>Error 404</h1>".encode()
        type = 'html'
        log_info(stat, addr, path)
        resp = get_response(stat, 'Not found', text, type)
        return resp

def connection(conn, addr):
    with conn:
        data = conn.recv(64000)
        if data == b"":
            conn.close()
        request = data.decode()
        print(request)
        resp = handler(request, addr)
        conn.send(resp)

def get_response(stat, status, src, type):
    return f"""HTTP/1.1 {stat} {status}
Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
Server: {settings.server}
Content-Type: {types[type]}
Content-Length: {len(src)}
Connection: keep-alive

""".encode() + src

def log_info(stat, addr, src):
        logging.info(f"""IP-address: {addr} File path: {src} Code: {stat} """)

def main():
    log()
    sock = socket.socket()
    try:
        sock.bind(('', settings.port))
        print('Using port: 80')
    except OSError:
        sock.bind(('', settings.other_port))
        print('Using port: 8080')
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        print("Connected", addr)
        Thread(target=connection, args=[conn, addr[0]]).start()

def log():
    logging.basicConfig(
        level=logging.DEBUG,
        format="Date: %(asctime)s | %(message)s",
        handlers=[
            logging.FileHandler("logs.log"),
            logging.StreamHandler(),
        ],
    )

if __name__ == '__main__':
    main()