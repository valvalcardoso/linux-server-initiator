import subprocess

class Analyst:

    def setLayout(self,layout):
        self.layout = layout

    def verifyActive(self):
        self.nginxStatus = f"{subprocess.run(['sudo', 'systemctl', 'status', 'nginx'], capture_output=True)}"
        self.mysqlStatus = f"{subprocess.run(['sudo', 'systemctl', 'status', 'mysql'], capture_output=True)}"
        activeNginx = self.nginxStatus.find('Active')
        activeMysql = self.mysqlStatus.find('Active')

        if 'inactive' in self.nginxStatus[activeNginx:activeNginx + 16]:
            self.nginxStatus = 'off'
        else:
            self.nginxStatus = 'on'
            self.layout.ids.nginxButton.background_normal = 'media/offnginx.png'

        if 'inactive' in self.mysqlStatus[activeMysql:activeMysql + 16]:
            self.mysqlStatus = 'off'

        else:
            self.mysqlStatus = 'on'
            self.layout.ids.mysqlButton.background_image = 'media/offmysql.png'

        return self.layout

    def setNginx(self):
        if self.nginxStatus == 'on':
            self.stopNginx()

        else:
            self.startNginx()

    def startNginx(self):
        print('nginx ligado')
        subprocess.run(['sudo','systemctl','start','nginx'],capture_output=True)
        self.layout.ids.nginxButton.background_normal = 'media/offnginx.png'
        self.nginxStatus = 'on'

    def stopNginx(self):
        print('nginx desligado')
        subprocess.run(['sudo','systemctl','stop','nginx'],capture_output=True)
        self.layout.ids.nginxButton.background_normal = 'media/nginx.png'
        self.nginxStatus = 'off'

    def setMySql(self):
        if self.mysqlStatus == 'on':
            self.stopMySql()

        else:
            self.startMySql()

    def startMySql(self):
        subprocess.run(['sudo', 'systemctl', 'start', 'mysql'], capture_output=True)
        self.layout.ids.mysqlButton.background_normal = 'media/offmysql.png'
        self.mysqlStatus = 'on'

    def stopMySql(self):
        subprocess.run(['sudo', 'systemctl', 'stop', 'mysql'], capture_output=True)
        self.layout.ids.mysqlButton.background_normal = 'media/mysql.png'
        self.mysqlStatus = 'off'