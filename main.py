from configparser import ConfigParser

    
class Server:
    def __init__(self, server):
        self.id_server = server["id_server"]
        self.credentials = server["credentials"]
        self.path = server["port"]
        self.frequency = server["alias"]
    def __str__(self):
        return f"server: {self.id_server} - {self.credentials} - {self.path} - {self.frequency}"
    
class AutoBackup:
    def __init__(self, autoBackup):
        self.id_autoBackup = autoBackup["id_backup"]
        self.id_server = autoBackup["id_server"]
        self.path = autoBackup["path"]
        self.frequency = autoBackup["frequency"]
        self.timestamp = autoBackup["timestamp"]
    def __str__(self):
        return f"auto-backup: {self.id_autoBackup} - {self.id_server} - {self.path} - {self.frequency}"



if __name__ == "__main__":
    config = ConfigParser()

    config.read("conf.ini")
    config_server = config["server"]
    config_autBackup = config["auto_backup"]

    server1 = Server(config_server)
    print(server1) 
    autoBackup1 = AutoBackup(config_autBackup)
    print(autoBackup1)