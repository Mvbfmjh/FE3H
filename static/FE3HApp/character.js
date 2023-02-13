
function filterTable(){
  //let genList = [{% for gen in gender %}'{{gen}}',{% endfor %}]
  //let afflList = [{% for affl in affiliation_list %}'{{affl}}',{% endfor %}];
  //console.log(genList);
  //console.log(afflList);

  var genderFilter, afflFilter, table, tr;
  genderFilter = document.getElementById('gender').value;
  afflFilter = document.getElementById('affiliation').value;
  table = document.getElementById("CharacterTable");
  tr = table.getElementsByTagName("tr");
  // When both filters have a selection
  if(!(genderFilter === "" || afflFilter === "")) {
    for (i = 2; i < tr.length; i++) {
      let tdGender, tdAffl;
      tdGender = tr[i].getElementsByTagName("td")[1];
      tdAffl = tr[i].getElementsByTagName("td")[2];
      if (tdGender && tdAffl) {
        let txtGen, txtAffl;
        txtGen = tdGender.textContent || tdGender.innerText;
        txtAffl = tdAffl.textContent || tdAffl.innerText;
        if (txtGen.indexOf(genderFilter) > -1 && txtAffl.indexOf(afflFilter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  } else if (!(genderFilter === "")) {
    for (i = 2; i < tr.length; i++) {
      let tdGender;
      tdGender = tr[i].getElementsByTagName("td")[1];
      if (tdGender) {
        let txtGen;
        txtGen = tdGender.textContent || tdGender.innerText;
        if (txtGen.indexOf(genderFilter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  } else if (!(afflFilter === "")) {
    for (i = 2; i < tr.length; i++) {
      let tdAffl;
      tdAffl = tr[i].getElementsByTagName("td")[2];
      if (tdAffl) {
        let txtAffl;
        txtAffl = tdAffl.textContent || tdAffl.innerText;
        if (txtAffl.indexOf(afflFilter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  } else {
    for (i = 2; i < tr.length; i++) {
      tr[i].style.display = "";
    }
  }
}