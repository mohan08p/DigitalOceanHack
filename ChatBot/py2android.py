import socketserver
import threading
from code.bot_trainer import BotTrainer
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    t=BotTrainer()
    def handle(self):
        print "connected"
        data2 = str(self.request.recv(1024))
        #chatbot = ChatBot('Job bot')
        #chatbot.set_trainer(ChatterBotCorpusTrainer)

        #chatbot.train("chatterbot.corpus.english")
        #response=chatbot.get_response(data2)
        
        response = ThreadedTCPRequestHandler.t.respond(data2)
        print("Server: {}".format(data2));
        response = bytes(str(response))
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST=""
    PORT =  5000

    tcpserver = ThreadedTCPServer((HOST, PORT-1), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=tcpserver.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("TCP serving at port", PORT-1)

    while True:
        pass
    tcpserver.shutdown()
