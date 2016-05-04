import httplib
import json
from OpFlow import StaticFlowPusher
class StaticFlowPusher1(object):
    def __init__(self, server):
        self.server = server
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
pusher = StaticFlowPusher1('127.0.0.1')
push_del = StaticFlowPusher()
flow1 = {
    "switch": "00:00:00:00:00:00:00:01",
    "name": "flow-mod-1",
    "cookie": "0",
    "priority": "32767",
    "eth_type": "0x806",
    "in_port": "1",
    # "ipv4_src": "10.0.0.1",
    # "ipv4_dst": "10.0.0.2",
    "active": "true",
    "actions": "output=2"
    }

flow2 = {
    "switch": "00:00:00:00:00:00:00:01",
    "name": "flow-mod-2",
    "cookie": "0",
    "priority": "32767",
    "eth_type": "0x806",
    "in_port": "2",
    # "ipv4_src": "10.0.0.2",
    # "ipv4_dst": "10.0.0.1",
    "active": "true",
    "actions": "output=1"
    }
# push_del.removeflowbyDPID()
pusher.set(flow1)
pusher.set(flow2)