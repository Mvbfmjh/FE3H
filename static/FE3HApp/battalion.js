function filterByName() {
  document.getElementById("affl").value = "";
  document.getElementById("isFlying").value = "";

  var filter, table, tr, td, i, txtValue;
  filter = document.getElementById("battalionName").value;
  table = document.getElementById("BattalionTable");
  tr = table.getElementsByTagName("tr");

  for (i=0; i<tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.includes(filter)) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function filterBattalion(){
  var filterAffiliation, filterIsFlying, table, container, checkBoxesSelected, tr, i;
  table = document.getElementById("BattalionTable");
  tr = table.getElementsByTagName("tr");
  container = document.getElementById("CheckBoxFields");
  checkBoxesSelected = container.querySelectorAll('input[type="checkbox"]:checked');

  filterAffiliation = [];
  filterIsFlying = [];
  for (i = 0; i < checkBoxesSelected.length; i++){
    filterAffiliation.push(checkBoxesSelected[i].name);
  }
  filterIsFlying.push(document.getElementById("isFlying").value)
  console.log(filterAffiliation);
  console.log(filterIsFlying);

  let resultFly, resultAffl;
  resultAffl = checkAffiliation(filterAffiliation, tr, 1);
  resultFly = checkFlying(filterIsFlying, tr, 2);
  for (i = 0; i < tr.length; i++){
    if (resultAffl[i] && resultFly[i])
      tr[i].style.display = "";
    else
      tr[i].style.display = "none"
  }
}

function checkFlying(filter, tr, col){
  let i, txtValue;
  var resultList = [true];
  console.log("checkFlying()");
  console.log(filter);
  if (!(filter[0] === "")){
    for (i = 0; i < tr.length; i++){
      let td = tr[i].getElementsByTagName("td")[col];
      if (td) {
        txtValue = td.textContent||td.innerText;
        console.log("txtValue: " + txtValue + " filter[0]: " + filter[0])
        if (txtValue === filter[0]){
          resultList.push(true);
        } else {
          resultList.push(false);
        }
      }
    }
  } else {
    for (i = 0; i < tr.length; i++) {
      let td;
      td = tr[i].getElementsByTagName("td")[col];
      if (td) {
        resultList.push(true);
      }
    }
  }
  console.log(resultList)
  return resultList
}

function checkAffiliation(filterList, tr, col){
  let i, k, txtValue;
  var resultList = [true];
  console.log("checkAffiliation()");
  console.log(filterList);

  for (i = 0; i < tr.length; i++){
    if (filterList.length > 0) {
      for (k = 0; k < filterList.length; k++) {
        let td = tr[i].getElementsByTagName("td")[col];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (k == 0){
            if(txtValue === filterList[k])
              resultList.push(true);
            else
              resultList.push(false);
          } else {
            resultList[i] = resultList[i] || txtValue === filterList[k];
          }
        }
      }
    } else {
      resultList.push(true);
    }
  }
  console.log(resultList)
  return resultList
}

function clearCheckbox(){
  let container = document.getElementById("CheckBoxFields");
  let checkBoxesSelected = container.querySelectorAll('input[type="checkbox"]:checked');
  for (i = 0; i < checkBoxesSelected.length; i++){
    checkBoxesSelected[i].checked = false;
  }
  filterBattalion();
}