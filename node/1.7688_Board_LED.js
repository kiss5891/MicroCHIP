var mraa = require('mraa');

var x = new mraa.Gpio(44);
x.dir(mraa.DIR_OUT);

while(true){
  setTimeout(function(){
      x.write(1);
  },200);
  setTimeout(function(){
      x.write(1);
  },200);
}
