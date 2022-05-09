# **A.D.A.M.S**
## **Automated Decentralization And Managment System**
```diff
- A.D.A.M.S. is still a work in progress. Running the installer module is not yet recommended.
```

***

- [About](#about)
- [Install](#how-to-run)
  - [Ubuntu 20.04 LTS](#ubuntu-2004-lts)
- [Features](#features)
  - [Skynet Webportal](#skynet-webportal)
  - [Handshake Daemon](#handshake-daemon)
  - [NGIX Webserver](#nginx-webserver)
  - [PowerDNS](#powerdns)
- [User Manual](#user-manual)
- [TODO](./TODO.md)

***

```
                _                                    
   __ _      __| |     __ _      _ _ _      ____     
  / _` |    / _` |    / _` |    | ` ` |    / __/     
 | (_| |   | (_| |   | (_| |    | | | |    \__ \     
  \__,_| ⍟ \__,_|▄⍟▄\__,_|█⍟▄|_|_|_| ⍟ /___/ ⍟  
                 ███           ███                   
               ███               ███                 
              ██                   ██                
                       ▄▄█▄▄                         
             ▄       ███───███       ▄               
            ███     ███──█──███     ███              
             ▀       ██──▄──██       ▀               
                       ▀▀█▀▀                         
              ██                   ██                
               ███               ███                 
  Automated Decentralization And Management System   
                  ▀▀▀█████████▀▀▀                   
```

# **About**
A.D.A.M.S. is a easy to deploy single-user [Skynet Webportal](https://portal-docs.skynetlabs.com) and Managment System.

With an intuitive user interface, A.D.A.M.S empowers users of all skill levels to take full control over their online data. Complete with a built-in [Handshake full node](https://github.com/handshake-org/hsd) and [PowerDNS server](https://github.com/PowerDNS/pdns), A.D.A.M.S. automates the deployment of a self reliant Skynet Portal. With the ability to act as its own Handshake DNS resolver, A.D.A.M.S the need for users to trust their data with any third-party.

# **Install**

> Note: A.D.A.M.S is currently only compatible with Ubuntu systems. Windows and MacOS compatibility will be a [future development](./TODO.md).

### Ubuntu 20.04 LTS
```
./build.sh && ./adams
```

# **Features**

## Skynet Webportal
A Skynet Portal is the doorway in which a you can access [Skynet](https://skynetlabs.com/about), and like any real doorway you do not own, it can be closed. This is why it is imparitive that users have the tools necessary to quickly and easily deploy a Skynet Portal of their own.

## Handshake Daemon

The [Handshake protocol (HNS)](https://handshake.org/) is a decentralized naming and certificate authority. A fundamental part of the decentralized internet, Handshake provides users with the ability to fully own their domain name. Effectively breaking the monopolistic strangle hold ICANN has enjoyed for so long. No longer are website and application developers at the whims of a third-party central authority.

By running a Handshake full node A.D.A.M.S is also able to break the need for a user to rely on third-party owned, and operated, DNS servers. Ensuring that the point of access to their personal Skynet Portal is always under their control.

## NGINX Webserver
The [NGINX Webserver](https://www.nginx.com/resources/wiki/) is a high preformance open-source webserver which is used by A.D.A.M.S. to provide users with a easy to use and remotely accessible user interface. Ensuring that no matter where they are, a user can manage and maintain their personal Skynet Portal.

## PowerDNS
[PowerDNS](https://www.powerdns.com/) is a light-weight open-source DNS server. Used in conjunction with the Handshake full node, PowerDNS provides users to resolve their own Handshake domain names.

# **User Manual**
***Coming Soon***