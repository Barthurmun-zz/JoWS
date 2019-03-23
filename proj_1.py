#!/usr/bin/python

'This example runs stations in AP mode'

import sys

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.node import OVSKernelAP
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi


def topology():
    'Create a network.'
    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP)

    info("*** Creating nodes\n")
    
    # One way of creating topology -> Restrict one without the controller.
    
    #sta1 = net.addStation('sta1', mac='00:00:00:00:00:01',
    #                        ip='192.168.0.1/24', position='20,8,0')
    #sta2 = net.addStation('sta2', mac='00:00:00:00:00:02',
    #                        ip='192.168.0.2/24', position='20,7,8')
    #ap1 = net.addStation('ap1', mac='02:00:00:00:01:00',
    #                        ip='192.168.0.10/24', position='20,10,5')

    #ap1.setMasterMode(intf='ap1-wlan0', ssid='ap1-ssid', channel='36', mode='a')
    
    internet = net.addHost('internet', ip='10.0.0.1/24', position='30,30,30')
    
    # Other way -> Simply one
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:01',position='20,8,0') #YouTube
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:02',position='20,7,8') #YouTube
    
    ap1 = net.addAccessPoint('ap1', ssid='Jows-proj1', channel='36', mode='ac', position='25,10,15')
        
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:03', position='30,10,5') #BE DL traffic
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:04', position='30,15,10') #VoIP between sta4 and sta5
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:05',  position='30,17,8') #VoIP between sta4 and sta5
    
    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633)
    
    #net.setPropagationModel(model="logDistance", exp=4.5)

    info("***Ploting the graph***\n")
    net.plotGraph(max_x=60, max_y=60)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Adding Link\n")
    net.addLink(ap1, internet)
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)
    net.addLink(sta4, ap1)
    net.addLink(sta5, ap1)

    # If we would decide for connection oriented topology to the internet.
    #net.addLink(sta3, internet)
    #net.addLink(sta4, internet)
    #net.addLink(sta5, internet)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])
    
    net.pingFull()
    
    # To the first way of creating SOHO network.
    #ap1.setIP('10.0.0.2/24', intf='ap1-eth2')
    #ap1.setIP('192.168.0.101/24', intf='ap1-eth2')
    
    
    #internet.setIP('10.0.0.1/24', intf='internet-eth0')
    #internet.setIP('10.0.0.103/24', intf='internet-eth1')
    
    #ap1.sendCmd( "iperf -s -i 1 -u")
    #sta1.cmdPrint( "iperf -c 192.168.0.10 -u -b 40M" )     

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    isVirtual = True if '-v' in sys.argv else False
    topology()
