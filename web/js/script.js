function copy_function() {
  var copyText = document.getElementById("result");
  copyText.select();
  copyText.setSelectionRange(0, 99999); 
  document.execCommand("copy");
}


