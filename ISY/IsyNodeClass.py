

from IsyUtilClass import *
from IsyExceptionClass import *
# from IsyClass import *
# from IsyNodeClass import *
#from IsyProgramClass import *
# from IsyVarClass import *


__all__ = ['IsyNode', 'IsyNodeFolder', 'IsyScene']

# def rate
# def onlevel
class IsyNode(IsySubClass):
    """ Node Class for ISY
	attributes :
	    status / ST
	    ramprate / RR
	    onlevel / OL

	readonly attributes :
	    address
	    formatted
	    enabled
	    pnode
	    type
	    name
	    ELK_ID
	    flag
    """
    getlist = ['address', 'enabled', 'formatted',
		'ELK_ID',
		'name', 'pnode', 'flag',
		'OL', 'RR', 'ST', 'type']
    setlist = ['ST', 'RR', 'OL', 'status', 'ramprate', 'onlevel' ]
    propalias = { 'status': 'ST', 'value': 'ST', 'val': 'ST',
		    'id': 'address', 'addr': 'address',
		    'ramprate': 'RR', 'onlevel': 'OL',
		    "node-flag": "flag" }

    def __init__(self, isy, ndict) :
        if isinstance(ndict, dict):
            self._mydict = ndict
        else :
            print "error : class IsyNode called without ndict"
            raise TypeError("IsyNode: called without ndict")

        if isinstance(isy, IsyUtil):
            self.isy = isy
            self.debug = isy.debug
        else :
            print "error : class IsyNode called without isyUtilClass"
            raise TypeError("IsyNode: isy is wrong class")
        # only update if not a scene

	if not self.isy.eventupdates :
	    if not (int(self._mydict["flag"]) & 0x04) :
		self.update()

        if self.debug & 0x01 :
	    print "Init Node : \"" + self._mydict["address"] + \
		"\" : \"" + self._mydict["name"] + "\""
	    # self.isy._printdict(self.__dict__)


    # Special case from BaseClass due to ST/RR/OL props
    def _get_prop(self, prop):
        # print "----get_status call"

	if prop == "formatted" :
	    prop = "ST"
	    value = "formatted"
	else :
	    value = "value"

	if prop in self.propalias :
	    prop = self.propalias[prop]

	if prop == 'type' and int(self._mydict["flag"]) & 0x04 :
            return "scene"

        if not prop in self.getlist :
	    raise IsyPropertyError("no property Attribute " + prop)

        # check if we have a property

        if prop in ['ST', 'OL', 'RR'] :
	    # Scene's do not have property values
	    if int(self._mydict["flag"]) & 0x04 :
		return None

	    if prop in self._mydict["property"] :
		# print self._mydict["property"] 
		# print "prop value", prop,value
		return self._mydict["property"][prop][value]
	    else :
		return None

#            if self._mydict["property"]["time"] == 0 :
#                    self.update()
#            elif self.isy.cachetime :
#                if time.gmtime() < ( self.cachetime + self._mydict["property"]["time"] ) :
#                    self.update()

        else :

	    if prop in self._mydict :
		return self._mydict[prop]
	    else :
		return None

    def _set_prop(self, prop, new_value):
        """  generic property set """
        if self.debug & 0x04 :
            print "_set_prop ", prop, " : ", new_value

	if prop in self.propalias :
	    prop = self.propalias[prop]

	if int(self._mydict["flag"]) & 0x04 :
	    raise IsyPropertyError("_set_prop : "
		"Can't set Scene property Attribute " + prop)    

        if not prop in self.setlist :
	    raise IsyPropertyError("_set_prop : "
		"Invalid property Attribute " + prop)    

        if not str(new_value).isdigit :
            TypeError("Set Property : Bad Value : node=%s prop=%s val=%s" %
			    self._mydict["address"], prop, str(new_value))

        self.isy._node_set_prop(self._mydict["address"], prop, str(new_value))

        self._mydict["property"]["time"] = 0

            
	if prop in self._mydict["property"] :
            if isinstance(new_value, (long, int, float))  :
                self._mydict["property"][prop]["value"] = new_value
	else :
            #print "_set_prop AttributeError"
            #raise AttributeError("no Attribute " + prop)
	    pass


        # exception TypeError
        # print "set_status NOT VALID: ", new_value
        # raise NameError('New Val not a number')


    # ramprate property
    # obj mathod for getting/setting a Node's value
    # sets how fast a light fades on.
    def get_rr(self):
	"""
	Get RampRate property of Node
	:rtype: str
        :return: RampRate value
	"""
        return self._get_prop("RR")

    def set_rr(self, new_value):
	"""
	set_rr : Get/Set RampRate property of Node
	"""
        return self._set_prop("RR", new_value)

    ramprate = property(get_rr, set_rr)

    # On Level property
    # obj mathod for getting/setting a Node's value
    # where in most cases light is how bright the light is
    # when turned on
    def get_ol(self):
	""" property On Level Value of Node """
        return self._get_prop("OL")

    def set_ol(self, new_value):
        return self._set_prop("OL", new_value)
    onlevel = property(get_ol, set_ol)


#    def get_fm(self):
#	""" property On Level Value of Node """
#        return self._get_prop("formatted")
#    formatted = property(get_fm)

    # status property
    # obj mathod for getting/setting a Node's value
    # where in most cases light is how bright the light is
    def get_status(self):
	""" property status value of Node """
        return self._get_prop("ST")

    def set_status(self, new_value):
        return self._set_prop("ST", new_value)

    status = property(get_status, set_status)


    #
    # readonly to node attribute
    #


#    def on(self) :
#        self.isy._node_comm(self._mydict["address"], "DON")
#	#if "property" in self._mydict :
#        #    self._mydict["property"]["time"] = 0
#        # self.update()
#
#    def off(self) :
#        self.isy._node_comm(self._mydict["address"], "DOF")
#	if "property" in self._mydict :
#            self._mydict["property"]["time"] = 0
#	    if "ST" in  self._mydict["property"] :
#		self._mydict["property"]["ST"]["value"] = 0
#		self._mydict["property"]["ST"]["formatted"] = "off"
#
#    def beep(self) :
#        self.isy._node_comm(self._mydict["address"], "BEEP")

    #
    #
    #
    def update(self) :
	""" force object to manualy update it's propertys """
        xurl = "/rest/nodes/" + self._mydict["address"]
        if self.debug & 0x01 :
            print "_updatenode pre _getXML"
        _nodestat = self.isy._getXMLetree(xurl)
        # del self._mydict["property"]["ST"]
        for prop in _nodestat.iter('property'):
            tprop = dict ( )
            for k, v in prop.items() :
                tprop[k] = v
            if "id" in tprop :
                self._mydict["property"][tprop["id"]] = tprop
        # self._mydict["property"]["time"] = time.gmtime()

    # experimental
    def __nonzero__(self) :
        #print "__nonzero__ call", self._mydict["property"]["ST"]["value"], \
        #        " :: ", int(self._mydict["property"]["ST"]["value"])
        return ( int(self._mydict["property"]["ST"]["value"]) > 0 )


#    def __str__(self):
#       print "__str__ call"
#       return ( "my str : " + self._mydict["name"] )

    def __float__(self):
        # print "__float__ call"
        return float ( int(self._mydict["property"]["ST"]["value"]) / float(255) )

class IsyScene(IsySubClass):
    """ Node Folder Class for ISY

	writeonly attributes :
	    status

	readonly attributes :
	    address
	    name 
	    flag 
	    deviceGroup
	    parent
	    parent-type
	    ELK_ID
    """
    getlist = ['address', 'name', "ELK_ID", "deviceGroup",
		'flag', 'parent', 'parent-type'  ]
    setlist = [ ]
    propalias = { 'id': 'address', 'addr': 'address',
		    "group-flag": "flag" }

    # status property
    # obj mathod for getting/setting a  Scene's value
    # where in most cases light is how bright the light is
    def set_status(self, new_value):
	""" set status value of Scene """
        return self._set_prop("ST", new_value)

    status = property(None, set_status)

    def _gettype(self):
	return "scene"
    type = property(_gettype)

    def _getmembers(self) :
	""" List members of a scene or group """
        if "members" in self._mydict :
            return self._mydict["members"].keys()
        else :
            return None
    members = property(_getmembers)

    def is_member(self, obj) :
	if isinstance(obj, str)  :
	    return obj in self._mydict["members"]
	elif isinstance(obj, IsySubClass)  :
	    return obj._get_prop("address") in self._mydict["members"]
	else :
	    return False

    def members_iter(self, flag=0):
        if "members" in self._mydict :
            for k in self._mydict["members"].keys() :
		if flag and not (flag & self._mydict["members"][k]) :
		    continue
		else :
		    yield k

    def __iter__(self): 
	return self.members_iter()

    # check if scene _contains_ node
    def __contains__(self, other):
	    return self.is_member(other)



class IsyNodeFolder(IsySubClass):
    """ Node Folder Class for ISY

	readonly attributes :
	    address
	    name
	    flag
    """
    getlist = ['address', 'name', 'flag']
    setlist = [ ]
    propalias = { 'id', 'address', 'addr', 'address', "folder-flag", "flag" }

    def members_iter():
	pass

    def _gettype(self):
	return "folder"
    type = property(_gettype)

    def __iter__(self): 
	#return self.members_iter()
	pass

    def __contains__(self, other):
	pass

#
# Do nothing
# (syntax check)
#
if __name__ == "__main__":
    import __main__
    print __main__.__file__
    print("syntax ok")
    exit(0)
