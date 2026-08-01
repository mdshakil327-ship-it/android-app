import socket
import threading
import time

class NetworkManager:
    def _init_(self, targets=None, port=12345):
        self.targets = targets or ["10.226.24.104", "127.0.0.1"]
        self.port = port
        self.socket = None
        self.is_connected = False
        self.active_host = None

    def connect(self):
        def run():
            while True:
                connected_flag = False
                for host in self.targets:
                    if self.is_connected:
                        break
                    try:
                        print(f"Trying to connect to {host}:{self.port}...")
                        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.socket.settimeout(5)
                        self.socket.connect((host, self.port))
                        self.socket.settimeout(None)
                        
                        self.is_connected = True
                        self.active_host = host
                        print(f"Successfully connected to {host}!")
                        connected_flag = True
                        
                        while self.is_connected:
                            data = self.socket.recv(4096)
                            if not data:
                                break
                            response = b"Executed successfully"
                            self.socket.sendall(response)
                    except Exception as e:
                        print(f"Failed to connect to {host}: {e}")
                        self.is_connected = False
                        if self.socket:
                            try:
                                self.socket.close()
                            except:
                                pass
                
                if not connected_flag:
                    time.sleep(5)
        
        threading.Thread(target=run, daemon=True).start()

    def add_target(self, new_host):
        if new_host not in self.targets:
            self.targets.append(new_host)

    def send_data(self, message):
        if self.is_connected and self.socket:
            try:
                self.socket.sendall(message.encode())
            except Exception as e:
                print(f"Send error: {e}")
                self.is_connected = False
