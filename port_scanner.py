import socket
import common_ports

def get_open_ports(target, port_range, verbose = False):
    
    try:
      targetIP = socket.gethostbyname(target)
    except:
      return "Error: Invalid hostname";

    print(target)
    print(targetIP)

    verbose_return = "Open ports for "+target+" ("+targetIP+")\nPORT     SERVICE"
    if target == targetIP:
      verbose_return = "Open ports for "+target+"\nPORT     SERVICE"
  
    open_ports = []
  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    port = port_range[0]
    while(port >= port_range[0] and port <= port_range[1]):
      try:
        if(s.connect_ex((target, port))==0):
          open_ports.append(port)
          if(verbose):
            port_name = common_ports.ports_and_services.get(port)
            if(port_name != None):
              verbose_return = verbose_return + "\n" + str(port).ljust(4) +"     "+port_name
      except:
        return "Error: Invalid IP address";
      port=port+1
      
    if(verbose):
      return verbose_return
      
    return(open_ports)