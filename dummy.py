from mininet.net import Mininet
from mininet.node import OVSController, Host
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0', controller=OVSController, ip='127.0.0.2', port=6633)
    c1 = net.addController(name='c1', controller=OVSController, ip='127.0.0.2', port=6633)

    info('*** Add Switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)

    info('*** Add Hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)

    info('*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s2)
    net.addLink(h3, s3)
    net.addLink(h4, s3)
    net.addLink(h4, s4)
    net.addLink(h5, s4)

    info('*** Starting network\n')
    net.build()

    info('*** Starting controllers\n')
    c0.start()
    c1.start()

    info('*** Starting switches\n')
    s1.start([c0, c1])
    s2.start([c0])
    s3.start([c0])
    s4.start([c0])

    info('*** Post configure switches and hosts\n')
    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()

