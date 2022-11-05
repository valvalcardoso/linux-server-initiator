#biblioteca que executa os comandos do cmd.
import subprocess

class Analyst:

    def setLayout(self,layout):
        self.layout = layout
        
    #Método que verifica se os serviços estão ativos.
    def verifyActive(self):
        #O retorno dessas 2 varíaveis será um informativo dos serviços.
        self.nginxStatus = f"{subprocess.run(['sudo', 'systemctl', 'status', 'nginx'], capture_output=True)}"
        self.mysqlStatus = f"{subprocess.run(['sudo', 'systemctl', 'status', 'mysql'], capture_output=True)}"
        
        #Procura o índice da palavra 'active' no informativo.
        activeNginx = self.nginxStatus.find('Active')
        activeMysql = self.mysqlStatus.find('Active')
        
        #Se existir uma string 'inactive após o índice da palavra 'Active'...
        if 'inactive' in self.nginxStatus[activeNginx:activeNginx + 16]:
            self.nginxStatus = 'off'
        else:
            self.nginxStatus = 'on'
            #muda o background dos botões.
            self.layout.ids.nginxButton.background_normal = 'media/offnginx.png'

        if 'inactive' in self.mysqlStatus[activeMysql:activeMysql + 16]:
            self.mysqlStatus = 'off'

        else:
            self.mysqlStatus = 'on'
            #muda o background dos botões.
            self.layout.ids.mysqlButton.background_image = 'media/offmysql.png'

        return self.layout

    def setNginx(self):
        if self.nginxStatus == 'on':
            self.stopNginx()

        else:
            self.startNginx()
            
    #Inicia o servidor nginx e troca a imagem do botão.
    def startNginx(self):
        print('nginx ligado')
        subprocess.run(['sudo','systemctl','start','nginx'],capture_output=True)
        self.layout.ids.nginxButton.background_normal = 'media/offnginx.png'
        self.nginxStatus = 'on'
        
    #Para o servidor nginx e troca a imagem do botão.
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
            
    #Inicia o serviço mysql e troca a imagem do botão.
    def startMySql(self):
        subprocess.run(['sudo', 'systemctl', 'start', 'mysql'], capture_output=True)
        self.layout.ids.mysqlButton.background_normal = 'media/offmysql.png'
        self.mysqlStatus = 'on'
        
    #Para o serviço mysql e troca a imagem do botão.
    def stopMySql(self):
        subprocess.run(['sudo', 'systemctl', 'stop', 'mysql'], capture_output=True)
        self.layout.ids.mysqlButton.background_normal = 'media/mysql.png'
        self.mysqlStatus = 'off'
