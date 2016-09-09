import miniupnpc

class UPnPClient(object):
    def __init__(self):
        self._upnp = miniupnpc.UPnP()
        self._upnp.discoverdelay = 200;
        self._upnp.discover()
        self._upnp.selectigd()

    def map(self, port):
        self._upnp.getspecificportmapping(port, 'TCP')
        return self._upnp.addportmapping(port, 'TCP', self._upnp.lanaddr, port, 'UPnP IGD Tester port %u' % port, '')

    def unmap(self, port):
        return self._upnp.deleteportmapping(port, 'TCP')

    def get_external_ip(self):
        return self._upnp.externalipaddress()
