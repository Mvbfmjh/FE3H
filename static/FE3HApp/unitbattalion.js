const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

var subjLvlList = ['E', 'E+', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A+', 'S', 'S+'];
var battalions, units;
units = [];

async function getBattalionList(){
  let response = await fetch("get", {
    method: 'GET',
    headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
  });

  let result = await response.json();
  /*
  console.log(result);
  console.log(JSON.parse(result.battalion_json));
  console.log(JSON.parse(result.affiliation_json));
  */
  return result;
}

async function getCharacter(rowId){
  let response = await fetch("getchara", {
    method: 'POST',
    headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
    body: JSON.stringify({'character': rowId}),
  });
  let result = await response.json();
  return JSON.parse(result)[0];
}

async function addBattalionList(){
  let affiliations, optgroup, affl;
  var tbody = document.getElementById("tbodyUnits");
  var tr = tbody.getElementsByTagName("tr");
  let result = await getBattalionList();
  affiliations = JSON.parse(result.affiliation_json);
  battalions = JSON.parse(result.battalion_json);

  affl = 0;
  for (let row of tr){
    let selectList = document.getElementById(row.id+'-btl');
    for (let battalion of battalions){
      let subjLvl = document.getElementById(row.id+'-subj');
      if (affl != battalion.fields['affiliation']){
        optgroup = document.createElement("optgroup");
        optgroup.setAttribute("label", affiliations[battalion.fields['affiliation']-1].fields['affiliation']);
        selectList.appendChild(optgroup);
        affl = battalion.fields['affiliation'];
      }

      if (subjLvlList.indexOf(subjLvl.innerHTML) >= subjLvlList.indexOf(battalion.fields['auth_requirement'])){
        let option = new Option(battalion.fields['name']);
        option.setAttribute("value", battalion.pk);
        optgroup.appendChild(option);
      }
    }
    let unit = await getCharacter(row.id);
    units.push({'name': row.id, 'unit': unit});
    let battalionSelect = document.getElementById(row.id+'-btl');
    setStats(row.id, battalions[battalionSelect.value-1]);
  }
}

async function setStats(rowId, selectedBattalion){
  let idTags = ['-btl-end', '-phy', '-mag', '-hit', '-crit', '-avd', '-prot', '-res', '-cha', '-btl-gambit'];
  let unit;
  for (let item of units){
    if (item.name === rowId){
      unit = item.unit;
      break;
    }
  }

  let data_end = document.getElementById(rowId+'-btl-end');
  let data_phy = document.getElementById(rowId+'-phy');
  let data_mag = document.getElementById(rowId+'-mag');
  let data_hit = document.getElementById(rowId+'-hit');
  let data_crit = document.getElementById(rowId+'-crit');
  let data_avd = document.getElementById(rowId+'-avd');
  let data_prot = document.getElementById(rowId+'-prot');
  let data_res = document.getElementById(rowId+'-res');
  let data_cha = document.getElementById(rowId+'-cha');
  let data_gambit = document.getElementById(rowId+'-btl-gambit');

  if (selectedBattalion) {
    data_end.innerHTML = selectedBattalion.fields['endurance'];
    data_phy.innerHTML = unit.fields['unit_str'] + selectedBattalion.fields['physical'];
    data_mag.innerHTML = unit.fields['unit_mag'] + selectedBattalion.fields['magical'];
    data_hit.innerHTML = unit.fields['unit_dex'] + selectedBattalion.fields['hit_rate']; //(unit.fields['unit_dex'] + unit.fields['unit_lck'])/2 + selectedBattalion.fields['hit_rate'];
    data_crit.innerHTML = (unit.fields['unit_dex'] + unit.fields['unit_lck'])/2 + selectedBattalion.fields['critical'];
    data_avd.innerHTML = (unit.fields['unit_spd']) + selectedBattalion.fields['avoidance']; //攻速の計算が必要
    data_prot.innerHTML = (unit.fields['unit_def']) + selectedBattalion.fields['protection']; 
    data_res.innerHTML = (unit.fields['unit_res']) + selectedBattalion.fields['resistance']; 
    data_cha.innerHTML = (unit.fields['unit_cha']) + selectedBattalion.fields['charm']; 
    data_gambit.innerHTML = selectedBattalion.fields['gambit'];

  } else if (unit.fields['battalion']) {
    data_end.innerHTML = battalions[unit.fields['battalion']].fields['endurance'];
    data_phy.innerHTML = unit.fields['unit_str'] + battalions[unit.fields['battalion']].fields['physical'];
    data_mag.innerHTML = unit.fields['unit_mag'] + battalions[unit.fields['battalion']].fields['magical'];
    data_hit.innerHTML = unit.fields['unit_dex'] + battalions[unit.fields['battalion']].fields['hit_rate']; //(unit.fields['unit_dex'] + unit.fields['unit_lck'])/2 + battalions[unit.fields['battalion']].fields['hit_rate'];
    data_crit.innerHTML = (unit.fields['unit_dex'] + unit.fields['unit_lck'])/2 + battalions[unit.fields['battalion']].fields['critical'];
    data_avd.innerHTML = (unit.fields['unit_spd']) + battalions[unit.fields['battalion']].fields['avoidance']; //攻速の計算が必要
    data_prot.innerHTML = (unit.fields['unit_def']) + battalions[unit.fields['battalion']].fields['protection']; 
    data_res.innerHTML = (unit.fields['unit_res']) + battalions[unit.fields['battalion']].fields['resistance']; 
    data_cha.innerHTML = (unit.fields['unit_cha']) + battalions[unit.fields['battalion']].fields['charm']; 
    data_gambit.innerHTML = battalions[unit.fields['battalion']].fields['gambit'];

  } else {
    data_end.innerHTML = '---';
    data_phy.innerHTML = unit.fields['unit_str']
    data_mag.innerHTML = unit.fields['unit_mag']
    data_hit.innerHTML = unit.fields['unit_dex']//(unit.fields['unit_dex'] + unit.fields['unit_lck'])/2 + battalions[unit.fields['battalion']].fields['hit_rate'];
    data_crit.innerHTML = (unit.fields['unit_dex'] + unit.fields['unit_lck'])/2;
    data_avd.innerHTML = (unit.fields['unit_spd']); //攻速の計算が必要
    data_prot.innerHTML = (unit.fields['unit_def']); 
    data_res.innerHTML = (unit.fields['unit_res']); 
    data_cha.innerHTML = (unit.fields['unit_cha']); 
    data_gambit.innerHTML = '---';
  }

}

async function setBattalion(rowId){
  let battalionSelect = document.getElementById(rowId+'-btl');
  let response = await fetch("set", {
    method: 'POST',
    headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
    body: JSON.stringify({'character': rowId, 'battalion': battalionSelect.value}),
  });
  setStats(rowId, battalions[battalionSelect.value-1]);
}

//getBattalionList();
addBattalionList();
