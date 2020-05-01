# simple-http-telnet-bridge
Simple python http server for bridging HTTP Get requests to telnet commands (with feedback)

# running script
```bash
python http_telnet_bridge.py &
```

# example compatibility extension to Homebridge using HTTP switch
The following example implements an HTTP-SWITCH for Homebridge.  The switch URLs connect to the http-telnet-bridge and send commands according to the Marantz FY18 AV SR NR PROTOCOL V02-02072018.  The sent commands are mute on (MUON), mute off (MUOFF), and a request for the mute status (MU?). 
```js
    {
      "accessory":     "HTTP-SWITCH",
      "name":          "Mute",
      "switchType":    "stateful",
      "pullInterval" : 3000,
      "onUrl":         "http://localhost:8000/?192.168.0.106|0.1|MUON",
      "offUrl":        "http://localhost:8000/?192.168.0.106|0.1|MUOFF",
      "statusUrl":     "http://localhost:8000/?192.168.0.106|0.2|MU?",
      "statusPattern": "MUON"
    }
```
(For more details, see [homebridge-http-switch](https://github.com/Supereg/homebridge-http-switch) and, e.g., [Marantz manuals](https://www.us.marantz.com/en-us/support/manuals)>AV Receivers>NR1609)

# command syntax
```html
http://localhost:8000/?{telnet address}|[wait time in seconds|]{command}
```
```{telnet address}``` and ```{command}``` are required, but ```[wait time]``` is optional

The bridge will attempt to connect to the specified telnet address and send the command.  If no wait time is specified, the bridge will immediately close the session and return an empty body.  If a wait time is specified, the bridge will wait and then execute a non-blocking read from the session.  The read contents will be returned in the body.

# more detailed example
```example-config.js``` uses the bridge to broker telnet commands (and responses) for several Homebridge HTTP-Switches.  The image shows a screen capture of the result in Home App.

