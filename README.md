

<!-- versión en ingles -->
<span id="EN">

EN

you are in english PUTO

</span>


<!-- versión en español -->
<span id="ES">

ES

estas en español PUTO

</span>



<!-- seleccionador automatico de lenguaje -->
<script type="text/javascript">

$puntuation=0;

for (var $tag in navigator.languages) {
	if (navigator.languages[$tag].substring(0,2) == "es") {
		$puntuation++;
	}
}

if ($puntuation>0) {
	document.getElementById("ES").style.display="block";
	document.getElementById("EN").style.display="none";
} else {
	document.getElementById("ES").style.display="none";
	document.getElementById("EN").style.display="block";
}

</script>
