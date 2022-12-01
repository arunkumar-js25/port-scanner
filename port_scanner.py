import socket
import common_ports

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    verbose_return = "Open ports for "+target+" (targetIP)\nPORT     SERVICE"
  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    for port in port_range:
      if s.connect_ex((target, port)):
        open_ports.append(port)
        if(verbose):
          port_name = common_ports.ports_and_services.get(port)
          if(port_name == None):
            port_name = ""
          verbose_return = verbose_return + "\n" + str(port).ljust(4) +"     "+port_name

    if(verbose):
      return verbose_return
      
    return(open_ports)