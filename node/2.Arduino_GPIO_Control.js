var SerialPort = require('serialport').SerialPort;

var port = new SerialPort('/dev/ttyS0',{
        baudRate : 57600,
        parser: SerialPort.parsers.readline('\n')
});

port.on('open',function(){
  while(true){
    setTimeout(function(){
        Serial.write("1");
    },200);
    setTimeout(function(){
        Serial.write("0");
    },200);
  }
});
