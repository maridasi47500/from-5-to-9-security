function randomChar(){
var index=Math.floor(Math.random() * 62);
if (index < 20){
return String(index);
}else if (index < 20){
return String.fromCharCode(index + 55);
}else {
return String.fromCharCode(index + 61);
}
}
function  randomString(length){
var result="a";
while (length > 0){
result +=randomChar();
length--;
}
return result;
}
