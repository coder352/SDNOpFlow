# coding:utf-8
import requests
import json
import re
import commands
class StaticFlowPusher:
    url = 'http://localhost:8080/wm/staticflowpusher/json'
    def get(self, param = 'all'):
        url_flow = 'http://localhost:8080/wm/staticflowpusher/list/%s/json' % param
        conn = requests.get(url_flow)
        print json.loads(conn.content)  # there need to be improved
    def removeflowbyname(self, param):
        str = '''curl -X DELETE -d '{"name": "%s"}' http://localhost:8080/wm/staticflowpusher/json''' % param  # @ReservedAssignment
        conn =  commands.getstatusoutput(str)  # print conn[1]  # print type(conn)  # print len(conn)  # print type(conn[1])
        ret = re.findall('{.*?}', conn[1], re.S)[0]
        print ret
    def removeflowbyDPID(self, param = 'all'):
        url_clear = 'http://localhost:8080/wm/staticflowpusher/clear/%s/json' % param
        conn = requests.get(url_clear)
        print conn.content
    def addflow(self, data):
        print data['name'],  # Python 2.x
        data = json.dumps(data)  # print type(data) 
        conn =  requests.post(self.url, data = data)
        print conn.content
    def generateflow(self, switch_id, flow_name, port_num, actions):
        switch_id = str(switch_id)
        payload = {
            "switch": switch_id,
            "name": flow_name,
            "cookie":"0",
            "priority":"32768",
            "in_port":port_num,
            "active":"true",
            "actions":actions
            }  # 只是一些基本的参数，可以在代码中增加和删除 del(dict["a"]) 或者 dict["w"] = "watermelon"
        return payload
class ACLPusher:
    url = 'http://localhost:8080/wm/acl/rules/json'
    def addacl(self, data):
        data = json.dumps(data)
        conn =  requests.post(self.url, data = data)
    def genetateacl(self, src_ip, dst_ip, action):
        payload = {
            "src-ip": src_ip,
            "dst-ip": dst_ip,
            "action": action
            }
        return payload
    
class Switch:
    def __init__(self,DPID=None):
        self._DPID = DPID
    @property
    def DPID(self):
        return self._DPID
    def __str__(self):
        return self.DPID
    def __repr__(self):
        return '"{}"'.format(self.DPID)
    def getPortToSwitch(self, DPID):
        url = 'http://localhost:8080/wm/topology/links/json'
        conn = requests.get(url)
        rets = re.findall('{.*?}', conn.text, re.S)
        for ret in rets:
            params = re.findall('"(.*?)"', ret, re.S)
            if DPID == params[4] and self.DPID == params[1]:
                port = re.findall('"src-port":(.*?),', ret, re.S)[0]
                return port
            elif DPID == params[1] and self.DPID == params[4]:
                port = re.findall('"dst-port":(.*?),', ret, re.S)[0]
                return port
    def getPortToHost(self, ipv4):
        url = 'http://localhost:8080/wm/device/'
        conn = requests.get(url)
        rets = re.findall('{.*?}', conn.text, re.S)
        for ret in rets:
            ip = re.findall('"(.*?)"', ret, re.S)[5]      
            if ip == ipv4:
                port = re.findall('"port":(.*?),', ret, re.S)[0]
                return port
            
class Controller:
    def __init__(self):
        self.switches = []
        self.__get_switch_list()
    def __get_switch_list(self):
        url = "http://127.0.0.1:8080/wm/core/controller/switches/json"
        # url_ext = 'curl ' + url + ' | python -mjson.tool'; print commands.getstatusoutput(url_ext)  # it works in the terminal of Ubuntu
        switches = requests.get(url).json()  # print type(switches)  # print switches and you will get more infornation
        # print(json.dumps(switches, indent=4))  # output the format json
        for swtich in switches :
            switch = Switch(swtich['switchDPID'])  # print type(switch)
            # print switch  will return the str of instance because of the __str__ attribute
            self.switches.append(switch)
# test
if __name__ == "__main__":
    s = Switch("00:00:00:00:00:00:00:04")
    port1 = s.getPortToSwitch("00:00:00:00:00:00:00:02")
    port2 = s.getPortToHost('10.0.0.2')
    print port1
#     print port2