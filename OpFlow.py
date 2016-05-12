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
        self.dictsHost = {} # srcHost(str): dstHost(set) 存放流表中所对应的源Host和目的host
        self.__getFlowHost()
        self.dictsPort = {} # PostId(int) : deviceId(str) 存放交换机端口所对应的设备，可以是Host或者Switch
    @property
    def DPID(self):
        return self._DPID
    def __str__(self):
        return self.DPID
    def __repr__(self):
        return '"{}"'.format(self.DPID)
    def __getFlowHost(self): # 找出交换机上的流表项中的源IP和目的IP，有点偏，为了做16年提高题第二小题
        url = 'http://localhost:8080/wm/core/switch/' + self.DPID + '/flow/json'
        self.flows = requests.get(url).json()
        self.flows = self.flows["flows"]
        for flow in self.flows:
            match = flow["match"]
            if "ipv4_src" not in match.iterkeys():
                continue



            if match['ipv4_src'] in self.dictsHost.iterkeys():
                s = self.dictsHost[match['ipv4_src']]
            else:
                s = set()
            s.add(match['ipv4_dst'])
            self.dictsHost[match["ipv4_src"]] = s


            # self.dictsHost[match["ipv4_src"]] = match["ipv4_dst"]
            # print self.dicts[match["ipv4_src"]]
    # 下面两个函数写的比较早，因为后来写了 getPortToDevice，建立了端口到设备的映射表， 下面两个函数要重写了
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
        self.dicts = {} # 建立双索引
        self.__get_switch_list()
        self.__getSwitchPorfToDevice()
    def __get_switch_list(self):
        url = "http://127.0.0.1:8080/wm/core/controller/switches/json"
        # url_ext = 'curl ' + url + ' | python -mjson.tool'; print commands.getstatusoutput(url_ext)  # it works in the terminal of Ubuntu
        switches = requests.get(url).json()  # print type(switches)  # print switches and you will get more infornation
        # print(json.dumps(switches, indent=4))  # output the format json
        for switch in switches :
            switchDPID = switch['switchDPID']
            switch = Switch(switch['switchDPID'])  # print type(switch)
            # print switch  will return the str of instance because of the __str__ attribute
            self.switches.append(switch)
            self.dicts[switchDPID] = switch
    def __getSwitchPorfToDevice(self):
        # 将端口对应的Switch记录下来
        url = 'http://localhost:8080/wm/topology/links/json'
        ress = requests.get(url).json()
        for res in ress:
            self.dicts[res['src-switch']].dictsPort[res['src-port']] = res['dst-switch']
            self.dicts[res['dst-switch']].dictsPort[res['dst-port']] = res['src-switch']
        # 将端口对应的Host记录下来
        url = 'http://localhost:8080/wm/device/'
        ress = requests.get(url).json()
        for res in ress:
            attachmentPoint = res['attachmentPoint']
            params = attachmentPoint[0]
            self.dicts[params['switchDPID']].dictsPort[params['port']] = res['ipv4'][0]
    def getSwitchFlowPath(self, srcHost, dstHost):
        S, res = set(), []
        res.append(srcHost)

        def toHost(switch, dstHost):
            if switch.DPID in S: return
            S.add(switch.DPID)
            res.append(switch.DPID)
            for nxtDeviceID in switch.dictsPort.itervalues():
                if len(nxtDeviceID.split('.')) == 4:
                    if nxtDeviceID == dstHost:
                        res.append(dstHost)
                        return
                elif srcHost in self.dicts[nxtDeviceID].dictsHost.iterkeys() and dstHost in self.dicts[nxtDeviceID].dictsHost[srcHost]:
                    toHost(self.dicts[nxtDeviceID], dstHost)

        for switch in self.switches:
            if srcHost in switch.dictsPort.itervalues():
                toHost(switch, dstHost)
                break

        for i in res:
            print i
        print

# test
if __name__ == "__main__":
    s = Switch("00:00:00:00:00:00:00:04")
    port1 = s.getPortToSwitch("00:00:00:00:00:00:00:02")
    port2 = s.getPortToHost('10.0.0.2')
    # print port1
    ctl = Controller()
    ctl.getSwitchFlowPath("10.0.0.1", "10.0.0.4")


#     print port2
