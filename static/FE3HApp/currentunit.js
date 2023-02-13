const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

async function sendRemoveRequest(name) {
  let response = await fetch("remove", {
    method: 'POST',
    headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
    body: JSON.stringify({'character': name}),
  });

  if (response['redirected'])
    window.location.href = response['url'];
  else {
    let result = await response.text();
    alert(result);
  }
}

async function sendUpdateRequest() {
  var tbody, tr, CharRow, CharList, CharObj;
  // Tags are for id of the HTML elements, and Fields are for data model Fields (They are 1to1)
  var tags = ['-name', '-lvl', '-class', '-hp', '-str', '-mag', '-dex', '-spd', '-lck', '-def', '-res', '-cha', '-sword', '-lance', '-axe', '-bow', '-brawl', '-reason', '-faith', '-auth', '-armor', '-ride', '-fly', ];
  var fields = ['character', 'level', 'unit_class', 'unit_hp', 'unit_str', 'unit_mag', 'unit_dex', 'unit_spd', 'unit_lck', 'unit_def', 'unit_res', 'unit_cha', 'prof_sword', 'prof_lance', 'prof_axe', 'prof_bow', 'prof_brawl', 'prof_reason', 'prof_faith', 'prof_authority', 'prof_armor', 'prof_riding', 'prof_flying', ]
  CharRow = [];
  CharList = [];

  // This was here to ensure that the data from the input row was transferred to the data row
  // May not be necessary anymore?
  hideInputs('');

  tbody = document.getElementById("tbodyUnits");
  tr = tbody.getElementsByTagName("tr");
  for (let row of tr)
    if (row.id.includes("-data"))
      CharRow.push(row);
  for (let row of CharRow){
    CharObj = {};

    for (let field of fields) 
      CharObj[field] = null;

    for (let i = 0; i < row.cells.length-1; i++)
      if (row.cells[i].id.includes(tags[i])) {
        if (tags[i] === '-class' && row.cells[i].innerHTML ==='---')
          CharObj[fields[i]] = null;
        else
          CharObj[fields[i]] = row.cells[i].innerHTML;
      }
    CharList.push(CharObj);
  }
  let response = await fetch("update", {
    method: 'POST',
    headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},    
    body: JSON.stringify(CharList),
  });
  let code = await response.text();
  alert(code);
}

async function openAddDialog() {
  var dialog = document.getElementById('addDialog');
  var list = document.getElementById('newCharaList');
  var opt = list.getElementsByTagName('option');

  if (list.options.length < 2) {
    let json, characters, affiliation, affl, optgroup;

    // This is to make the screen back to it's "default" view, where no inputs are shown
    hideInputs('');

    let response = await fetch("getunused", {
      method: 'GET',
      headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
    });

    json = await response.json();
    characters = JSON.parse(json.characters);
    affiliation = JSON.parse(json.affiliation);
    affl = 0;
    
    for (let chara of characters) {
      if (affl != chara.fields['affiliation']){
        optgroup = document.createElement("optgroup");
        optgroup.setAttribute("label", affiliation[chara.fields['affiliation']-1].fields['affiliation'])
        list.appendChild(optgroup);
        affl = chara.fields['affiliation'];
      }
      let newOption = new Option(chara.fields['name']);
      newOption.setAttribute("value", chara.pk);
      optgroup.appendChild(newOption);
    }
  }
  // Once the unused character list is populated, it will show the dialog
  dialog.showModal();
}

function closeDialog(dialogId) {
  // Defaults the list selection back to the null val
  let dialog = document.getElementById(dialogId);
  let list = dialog.getElementsByTagName("select");
  list[0].selectedIndex = 0;
  dialog.close();
}

async function sendAddRequest(dialogId) {
  let list = document.getElementById('newCharaList');
  let character_id = list.value;

  closeDialog(dialogId);

  let response = await fetch("add", {
    method: 'POST',
    headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
    body: JSON.stringify({'character_id': character_id}),
  });

  if (response['redirected'])
    window.location.href = response['url'];
  else {
    let result = await response.text();
    alert(result);
  }

}

async function rowHidden(chara){
  // First load data:
  /*
    1. Initialize the list for the selected character (GET only first time)
    2. Hide classes depending on the level of the character
    3. Get the innerHTML from data and set as the selected val of the dropdown on input
    4. Transfer the data from input -> data 
    5. Hide other inputs rows
    6. Swap visibility of rows
  */

  var inputTr = document.getElementById(chara+'-input');
  var dataTr = document.getElementById(chara+'-data');

  let classSelect = document.getElementById(chara + '-input-class');
  if (classSelect.options.length < 2) {
    await initialiseCharacterClassList(chara);
  }

  setListValue(inputTr, dataTr);
  
  hideInputs(chara);
  var tr = [inputTr, dataTr];
  for (let row of tr) {
    if (row.classList.contains("hidden"))
      row.classList.remove("hidden");
    else
      row.classList.add("hidden");
  }
  rowTransferData(inputTr.id, dataTr.id);
}

async function initialiseCharacterClassList(chara) {
  let classSelect = document.getElementById(chara + '-input-class');
  let response = await fetch("getclasslist", {
      method: 'POST',
      headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
      body: JSON.stringify({'character': chara}),
  });

  let result = await response.text();
  let classList = JSON.parse(result);
  let classGrade = null;
  let optgroup;
  for (let unitclass of classList) {
    if (classGrade != unitclass.fields['grade']){
      optgroup = document.createElement("optgroup");
      optgroup.setAttribute("label", unitclass.fields['grade']);
      optgroup.setAttribute("id", chara + '-input-grade-' +  unitclass.fields['grade']);
      classSelect.appendChild(optgroup);
      classGrade = unitclass.fields['grade'];
    }
    let newOption = new Option(unitclass.fields['name']);
    newOption.setAttribute("value", unitclass.fields['name']);
    optgroup.appendChild(newOption);
  }
}

function setListValue(inputTr, dataTr){
  let input = document.getElementById(inputTr.id);
  let list = input.getElementsByTagName("select");
  console.log(list);
  for (let select of list){
    let data = document.getElementById(select.id.replace('input', 'data'))
    let options = select.getElementsByTagName("option");
    for (let i = 0; i < options.length; i++){
      if (options[i].value == data.innerHTML){
        console.log(data.innerHTML)
        select.selectedIndex = i;
        break;
      }
    }
  }
}

function rowTransferData(inputTrId, dataTrId) {
  let growthTransfer = ['-growth-hp', '-growth-str', '-growth-mag', '-growth-dex', '-growth-spd', '-growth-lck', '-growth-def', '-growth-res', '-growth-cha'];
  for (let growth of growthTransfer)
    document.getElementById(dataTrId + growth).innerHTML = document.getElementById(inputTrId + growth).innerHTML;
}

function validateValue(inputId){
  var inputField = document.getElementById(inputId);
  var val = Number(inputField.value);

  if (val < 0){
    inputField.value = 0;
  }
  else if (val > Number(inputField.getAttribute('max')))
    inputField.value = inputField.getAttribute('max');
  else if (val == null)
    inputField.value = 0;
}

async function updateGrowth(src){
  let classSelect, tr, characterList, classList, classObj;
  var growthTags = ['-growth-hp', '-growth-str', '-growth-mag', '-growth-dex', '-growth-spd', '-growth-lck', '-growth-def', '-growth-res', '-growth-cha']
  var growthFields = ['hp_growth', 'str_growth', 'mag_growth', 'dex_growth', 'spd_growth', 'lck_growth', 'def_growth', 'res_growth', 'cha_growth'];
  classSelect = document.getElementById(src+'-class');
  tr = document.getElementById(src);

  var dataClass = document.getElementById(src.split('-')[0] + '-data-class');
  dataClass.innerHTML = classSelect.value;

  // ここをGET REQUESTで取得するように変更
  let response = await fetch("getgrowthrates", {
      method: 'POST',
      headers: {'Content-Type': 'application/json', "X-CSRFToken": csrftoken},
      body: JSON.stringify({'character': src.split('-')[0], 'unit_class': classSelect.value}),
  })

  let result = await response.text()
  result = JSON.parse(result);

  characterObj = JSON.parse(result['character'])[0];
  classObj = JSON.parse(result['unitclass'])[0];
  for (let i = 0; i < growthTags.length; i++) {
    let characterGrowth = document.getElementById(src + growthTags[i]);
    characterGrowth.value = characterObj.fields[growthFields[i]];
    if (classObj)
      characterGrowth.value = characterGrowth.value + classObj.fields[growthFields[i]];
    characterGrowth.innerHTML = characterGrowth.value;
  }
}

function hideInputs(chara){
  let tbody, tr;
  tbody = document.getElementById("tbodyUnits");
  tr = tbody.getElementsByTagName("tr");

  for (let row of tr) {
    if(chara === '' || !row.id.includes(chara)){
      if(row.id.includes('input')){
        row.classList.add("hidden");
        rowTransferData(row.id, row.id.split('-')[0]+'-data')
      } else
        row.classList.remove("hidden");
    }
  }
}

function hideClass(row){
  let lvl = document.getElementById(row + '-lvl').value;
  let optgroup;
  if (lvl < 30) {
    optgroup = document.getElementById(row + '-grade-最上級職');
    optgroup.classList.add("hidden");
  } else {
    optgroup = document.getElementById(row + '-grade-最上級職');
    optgroup.classList.remove("hidden");
  }
  if (lvl < 20) {
    optgroup = document.getElementById(row + '-grade-上級職');
    optgroup.classList.add("hidden");
    optgroup = document.getElementById(row + '-grade-特級職');
    optgroup.classList.add("hidden");
  } else {
    optgroup = document.getElementById(row + '-grade-上級職');
    optgroup.classList.remove("hidden");
    optgroup = document.getElementById(row + '-grade-特級職');
    optgroup.classList.remove("hidden");
  }
  if (lvl < 10) {
    optgroup = document.getElementById(row + '-grade-中級職');
    optgroup.classList.add("hidden");
  } else {
    optgroup = document.getElementById(row + '-grade-中級職');
    optgroup.classList.remove("hidden");
  }
  if (lvl < 5) {
    optgroup = document.getElementById(row + '-grade-初級職');
    optgroup.classList.add("hidden");
  } else {
    optgroup = document.getElementById(row + '-grade-初級職');
    optgroup.classList.remove("hidden");
  }
}

function updateDataTd(inputSrc) {
  let srcIdSplit = inputSrc.split('-')
  let dataTdId = srcIdSplit[0] + '-data-' + srcIdSplit[2];
  let dataTd = document.getElementById(dataTdId);
  let srcTd = document.getElementById(inputSrc);
  var setVal = srcTd.value !== undefined ? srcTd.value : srcTd.innerHTML;
  dataTd.innerHTML = setVal;
}

function addOnClickToTdOnLoad(srcTag){
  var tbody = document.getElementById("tbodyUnits");
  var tr = tbody.getElementsByTagName("tr");
  var dataTr = [];

  for (let row of tr)
    if(row.id.includes(srcTag))
      dataTr.push(row);

  for (let row of dataTr) {
    let td = row.getElementsByTagName("td");
    for (let data of td) {
      if (data.id.includes(srcTag))
        data.addEventListener("click", () => { rowHidden(data.id.split('-')[0]) }, false)
    }
  }
}

function addOnChangeToInputsOnLoad(srcTag){
  var tbody = document.getElementById("tbodyUnits");
  var tr = tbody.getElementsByTagName("tr");
  var inputTr = [];

  for (let row of tr)
    if(row.id.includes(srcTag))
      inputTr.push(row);

  for (let row of inputTr) {
    let inputField = row.getElementsByTagName("input");
    for (let input of inputField) {
      if (input.id.includes('lvl'))
        input.addEventListener("change", () => {hideClass(input.id.split('-')[0]+'-input')}, false);
      input.addEventListener("change", () => {updateDataTd(input.id)}, false);
      input.addEventListener("change", () => {validateValue(input.id)}, false);
    }
    let selectList = row.getElementsByTagName("select");
    for (let select of selectList){
      if (select.id.includes("class")){
        select.addEventListener("change", () => {updateGrowth(select.id.split('-')[0]+'-input')}, false);
        select.addEventListener("focus", () => {hideClass(select.id.split('-')[0]+'-input')}, false);
      }
      select.addEventListener("change", () => {updateDataTd(select.id)}, false);
    }
  }

}


addOnClickToTdOnLoad('-data');
addOnChangeToInputsOnLoad('-input');
