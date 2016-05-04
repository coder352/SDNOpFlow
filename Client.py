from OpFlow import StaticFlowPusher

if __name__ == "__main__":   
    pusher = StaticFlowPusher()
#     ctl = Controller()
    ###########################
    # 1. add/delete flow quickly
    ###########################
#     for switch in range(len(ctl.switches)):
#         for port in range(1, 4):
#             flow = pusher.generateflow(ctl.switches[switch],
#                                        's{0}p{1}f1'.format(switch, port), 
#                                        port,
#                                        'output=flood')
#             pusher.addflow(flow)
#             pusher.removeflowbyname(flow['name'])
#         pusher.removeflowbyDPID(ctl.switches[switch])
#     pusher.removeflowbyDPID()
    
    ####################
    # 2. get switchs flow
    ####################
#     for switch in range(len(ctl.switches)):
#         pusher.get(ctl.switches[switch])  # get the single switch flows
#     pusher.get()  # get all switchs flows

    #####################################################################################
    # 3. define some single flow or flows that have no law or you have some flow with json
    # example
    #####################################################################################
     # H1 to D1
    
    flow = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow-mod-1",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.1",
        "ipv4_dst": "10.0.0.3",
        "active": "true",
        "actions": "output=3"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow-mod-2",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.1",
        "ipv4_dst": "10.0.0.3",
        "active": "true",
        "actions": "output=2"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow-mod-3",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.1",
        "ipv4_dst": "10.0.0.3",
        "active": "true",
        "actions": "output=1"
        }
    pusher.addflow(flow)
    # H1 to D2
    flow = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow-mod-4",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.1",
        "ipv4_dst": "10.0.0.4",
        "active": "true",
        "actions": "output=4"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow-mod-5",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.1",
        "ipv4_dst": "10.0.0.4",
        "active": "true",
        "actions": "output=2"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow-mod-6",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.1",
        "ipv4_dst": "10.0.0.4",
        "active": "true",
        "actions": "output=2"
        }
    pusher.addflow(flow)
    # H2 to D1
    flow = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow-mod-7",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.2",
        "ipv4_dst": "10.0.0.3",
        "active": "true",
        "actions": "output=4"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow-mod-8",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.2",
        "ipv4_dst": "10.0.0.3",
        "active": "true",
        "actions": "output=2"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow-mod-9",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.2",
        "ipv4_dst": "10.0.0.3",
        "active": "true",
        "actions": "output=1"
        }
    pusher.addflow(flow)
    # H2 to D2
    flow = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow-mod-10",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.2",
        "ipv4_dst": "10.0.0.4",
        "active": "true",
        "actions": "output=3"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow-mod-11",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.2",
        "ipv4_dst": "10.0.0.4",
        "active": "true",
        "actions": "output=2"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow-mod-12",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.2",
        "ipv4_dst": "10.0.0.4",
        "active": "true",
        "actions": "output=2"
        }
    pusher.addflow(flow)
    
    
    # back route
    flow = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow-mod-13",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.4",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow-mod-14",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.4",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow-mod-15",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.4",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow-mod-16",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.4",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)




    flow = {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow-mod-17",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.3",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow-mod-18",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.3",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow-mod-19",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.3",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)
    flow = {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow-mod-20",
        "cookie": "0",
        "priority": "32767",
        "eth_type": "0x0800",
        "ipv4_src": "10.0.0.3",
        "active": "true",
        "actions": "output=flood"
        }
    pusher.addflow(flow)