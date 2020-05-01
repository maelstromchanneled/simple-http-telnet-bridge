{
  "bridge": {
    "name": "HomeBridge",
    "username": "CC:22:3D:E3:CE:30",
    "port": 51826,
    "pin": "123-45-678"
  },
  "description": "example for running marantz AVR",
  "platforms": [
  ],
  "accessories": [
    {
      "accessory": "HTTP-SWITCH", "name": "Mute", "switchType": "stateful", "pullInterval" : 3000,
      "onUrl":     "http://localhost:8000/?192.168.0.106|0.1|MUON",
      "offUrl":    "http://localhost:8000/?192.168.0.106|0.1|MUOFF",
      "statusUrl": "http://localhost:8000/?192.168.0.106|0.2|MU?",
      "statusPattern": "MUON"
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "FireTV", "switchType": "stateful", "pullInterval" : 3000,
      "onUrl":     "http://localhost:8000/?192.168.0.106|0.1|SISAT/CBL",
      "offUrl":    "http://localhost:8000/?192.168.0.106|0.1|SISAT/CBL",
      "statusUrl": "http://localhost:8000/?192.168.0.106|0.2|SI?",
      "statusPattern": "SISAT/CBL"
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "Wii", "switchType": "stateful", "pullInterval" : 3000,
      "onUrl":     "http://localhost:8000/?192.168.0.106|0.1|SIGAME",
      "offUrl":    "http://localhost:8000/?192.168.0.106|0.1|SISAT/CBL",
      "statusUrl": "http://localhost:8000/?192.168.0.106|0.2|SI?",
      "statusPattern": "SIGAME"
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "XBox", "switchType": "stateful", "pullInterval" : 3000,
      "onUrl":     "http://localhost:8000/?192.168.0.106|0.1|SIMPLAY",
      "offUrl":    "http://localhost:8000/?192.168.0.106|0.1|SISAT/CBL",
      "statusUrl": "http://localhost:8000/?192.168.0.106|0.2|SI?",
      "statusPattern": "SIMPLAY"
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "AppleTV", "switchType": "stateful", "pullInterval" : 3000,
      "onUrl":     "http://localhost:8000/?192.168.0.106|0.1|SIAUX2",
      "offUrl":    "http://localhost:8000/?192.168.0.106|0.1|SISAT/CBL",
      "statusUrl": "http://localhost:8000/?192.168.0.106|0.2|SI?",
      "statusPattern": "SIAUX2"
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "Vol+", "switchType": "stateless",
      "onUrl": "http://localhost:8000/?192.168.0.106|MVUP",
      "timeout": 100
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "Vol-", "switchType": "stateless",
      "onUrl": "http://localhost:8000/?192.168.0.106|MVDOWN",
      "timeout": 100
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "Quiet", "switchType": "stateless",
      "onUrl": "http://localhost:8000/?192.168.0.106|MV40",
      "timeout": 100
    }   
    ,
    {
      "accessory": "HTTP-SWITCH", "name": "Loud", "switchType": "stateless",
      "onUrl": "http://localhost:8000/?192.168.0.106|MV55",
      "timeout": 100
    }   
  ]
}
