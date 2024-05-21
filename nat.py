from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.node import OVSController

class customTopo(Topo):
	def build(self):
		s1 = self.addSwitch('s1')
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		self.addLink(s1, h1)
		self.addLink(s1, h2)
		self.addLink(s1, h3)
		
net = Mininet(topo=customTopo(), controller=OVSController, autoSetMacs=True)
net.addNAT().configDefault()
net.start()
CLI(net)
net.stop()
		
