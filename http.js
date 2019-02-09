function loadDoc() {
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("get_data").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "homepage_2.html", true);
  xhttp.send();
}