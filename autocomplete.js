function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
}

/*An array containing all the identifiers in the document:*/
var names = ["AB005548","AB007174","AB034984","AB035089","AB043547","AB045122","AB061824","AB065574","AB065915","AB065916","AF025880","AF025882","AF025884","AF025886","AF045447","AF046026","AF081866","AF081867","AF081869","AF081871","AF081873","AF081875","AF081877","AF081879","AF081880","AF081882","AF081884","AF081885","AF085628","AF085630","AF085632","AF120981","AF120989","AF120993","AF127519","AF127520","AF129817","AF134214","AF134215","AF143897","AF157102","AF157379","AF216854","AF232229","AF282904","AF293358","AF293359","AF306520","AF328890","AF347021","AF363483","AF404831","AF404832","AF485252","AF485253","AF485254","AH009108","AJ001716","AJ007421","AJ250235","AJ272310","AJ278717","AJ316564","AB234097","AY138487","AY138488","AY138489","AY138490","AY138491","AY138492","AY138493","AY138494","AY138495","AY177663","AY574212","D00517","D00596","D50604","D64176","D88548","DQ979790","EF017813","FR869631","HQ729920","HQ729921","HQ834246","HQ834247","HQ834248","U02523","U11424","U19562","U19568","U19576","U34844","U55184","U63613","U75701","U78733","U84540","U84547","U84551","U86246","U86247","U86248","U86249","U86250","U90660","U93565","X17286","X63760","Z27420","SCCA1","SCCA2","SMAD4","ME2","RPL17","IMPA2","DPC4","HUT11","MBD1","MBD2","TXNL","NPC1","IMPACT","VPS4B","DSC1","DSC3","JK","SALL3","MPPE1","SS18/SSX1fusion","SS18/SSX2fusion","DSG1","FECH","PI13","UT-B1","taf4b","SSX2/SS18fusion","DSG4","ACTBP9","NDUFV2","BCL2/JH6fusion","DSC2","SLC14A1JK","SLC14A1","FAU1P","pseudoTPMT","SSCA1","AQP4","SEF2-1B","Smad2","DTN","OR18-17","OR18-42","OR18-43","OR18-44","OR18-79","GALNR","MBP","NCAD","18q21","18q21.3","18q21.1-q21.2","18p11.2","18q21.1","18q12","18q21.2-q22","18p11.32","18q12-q21","18q11","18q11.2-q12.1","18q21-q22","18q12.1","18p11","18q23","t(X;18)(p11.21;q11.21)","18q11.21","Xp11.21","q12.1","q23","18q12.1","18q12-q21.1","t(18;X)(q11.21;p11.23)","Xp11.23","t(18;X)(q11.21;p11.21)","18p11.3","t(14;18)(q32;q21)","q21","q32","18q11-q12","18q22","18p11.21-pter","18q21;7cRtelomericfromWI6206","q21.3", "squamous cell carcinoma antigen 2", "ribosomal protein L17", "squamous cell carcinoma antigen 1", "SMAD4", "ME2", "U58b small nucleolar RNA", "U58a small nucleolar RNA", "Putative U58 small nucleolar RNA", "seven transmembrane helix receptor", "inosine monophosphatase 2", "deleted in pancreatic carcinoma", "blood group Kidd urea transporter", "methyl-CpG binding protein 1", "testis-specific methyl-CpG binding protein 2", "methyl-CpG binding protein 2", "thymidylate synthase", "JK blood group urea transporter HUT11", "thioredoxin-like protein", "myo-inositol monophosphatase 2", "Niemann-Pick C1 protein", "headpin", "imprinted and ancient", "vacuolar protein sorting factor 4B", "desmocollin 1a", "desmocollin 1b", "desmocollin 3a", "desmocollin 3b", "C18orf2", "urea transporter JK glycoprotein", "C2H2 zinc finger protein", "metallo phosphoesterase", "SS18/SSX1 fusion protein", "SS18/SSX2 fusion protein", "transthyretin amyloidosis variant A120S", "transthyretin amyloidosis variant D38V", "transthyretin amyloidosis variant F33V", "Niemann-Pick C1 disease protein", "desmoglein type 1", "spalt-like zinc finger protein", "ferrochelatase", "desmocollin type 3", "hurpin", "urea transporter-B1", "SSX2/SS18 fusion protein", "desmoglein 4 preproprotein", "IMPACT", "beta-cytoplasmic actin", "24-kDa subunit of Complex I", "24-kDa subunit of complex I", "desmocollin 2 precursor", "SLC14A1", "solute carrier family 14", "truncated solute carrier family 14", "squamous cell carcinoma antigen", "mercurial-insensitive water-channel", "Golf alpha", "aquaporin-4 M23 isoform", "aquaporin-4 M1 isoform", "aquaporin-4", "SEF2-1B", "Smad2", "dystrobrevin isoform DTN-3", "dystrobrevin isoform DTN-2", "dystrobrevin isoform DTN-1", "galanin receptor", "putative p150", "myelin basic protein", "N-Cadherin"];

/*initiate the autocomplete function on the "myInput" element, and pass along the names array as possible autocomplete values:*/
autocomplete(document.getElementById("myInput"), names);
