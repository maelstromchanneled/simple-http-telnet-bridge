# simple-http-telnet-bridge
Simple python http server for bridging HTTP Get requests to telnet commands (with feedback)

# running script
Launch the server using command-line python:
```bash
python http_telnet_bridge.py &
```
To run in debug mode:
```bash
python http_telnet_bridge.py debug &
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
http://localhost:8000/?{telnet address}|[wait time in seconds|]{command}[|regex pattern[|match pattern]]
```
```{telnet address}``` and ```{command}``` are required, but ```[wait time]``` is optional.

The bridge will attempt to connect to the specified telnet address and send the command.  If no wait time is specified, the bridge will immediately close the session and return an empty body.  If a wait time is specified, the bridge will wait and then execute a non-blocking read from the session.  The read contents will be optionally processed (details below) and returned in the body.

The use of ```[wait time]``` requests server feedback.
In feedback mode, ```[regex pattern]``` can be used to extract a portion of the feedback
using the regular expression ```s/[regex pattern]/\1```.
To function properly, the pattern must contain exactly ONE parenthetical group.
If regular expression extraction is used, an additional matching operation can be called
using ```[match pattern]```.
In matching mode, the output of the regular expression extraction is compared directly
with the match pattern, return "1" is match, otherwise "0".
This is intended to support various HTTP query constructs 
that might expect a derived value or a match flag.

If the server is run in debug mode, each HTTP query will produce output
```
[HTTP TELNET BRIDGE] <192.168.0.106|0.2|MV?|.*MV(\d\d).*> ==> <MV455 MVMAX 98 > ==> <45>
```
This indicates the input command, the response, and the final output that is returned in the body.


# more detailed examples
```example-config.js``` uses the bridge to broker telnet commands (and responses) for several Homebridge HTTP-Switches and HTTP-Dimmers.  The image shows a screen capture of the result in Home App.

