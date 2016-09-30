var mraa = require('mraa');
var SerialPort = require('serialport').SerialPort;
var s;
var x = new mraa.Gpio(44);
x.dir(mraa.DIR_OUT);

var port = new SerialPort('/dev/ttyS0',{
        baudRate : 57600,
        parser: SerialPort.parsers.readline('\n')
});

port.on('open',function(){
        console.log('ok');
        port.on('data',function(data){
          var readVal = data.toString();
          var a = readVal.charAt(3);
          var b = readVal.charAt(5);
          console.log(a+b);
          if(a = '0' && b = '0'){
            x.write(0);
          }else{
            x.write(1);
          }
        });
});
