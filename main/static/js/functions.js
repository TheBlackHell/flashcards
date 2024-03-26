function checkMultichoiceAnswer(selected, answer, clicked_id) {
  if (selected == answer) {
    document.getElementById(clicked_id).style.backgroundColor = 'rgb(92, 46, 167)';
    document.getElementById(clicked_id).disabled = 'disabled';
    const buttonIds = ['b-0', 'b-1', 'b-2', 'b-3'];
    delete buttonIds[answer];
    
    buttonIds.forEach(id => {
      document.getElementById(id).style.backgroundColor = 'rgb(167, 46, 46)';
      document.getElementById(id).disabled = 'disabled';
      document.getElementById(id).style.filter = 'opacity(0.4)';
    });
    document.getElementById('continue-button').disabled = '';
  }
  else {
    document.getElementById(clicked_id).style.backgroundColor = 'rgb(167, 46, 46)';
    document.getElementById(clicked_id).style.filter = 'opacity(0.4)';
    document.getElementById(clicked_id).disabled = 'disabled';
  }
}

function checkTrueFalseAnswer(selected, answer, clicked_id, correct_value) {
  let other_id = '';
  if (clicked_id == 'button-a') {
    other_id = 'button-b'
  }
  else {
    other_id = 'button-a'
  }
  if (answer == selected) {
    document.getElementById(other_id).style.filter = 'opacity(0.4)';
    document.getElementById(other_id).style.backgroundColor = 'rgb(167, 46, 46)';
    document.getElementById(clicked_id).style.backgroundColor = 'rgb(92, 46, 167)';
  } 
  else {
    document.getElementById(clicked_id).style.filter = 'opacity(0.4)';
    document.getElementById(clicked_id).style.backgroundColor = 'rgb(167, 46, 46)';
    document.getElementById(other_id).style.backgroundColor = 'rgb(92, 46, 167)';
  }
  if (answer == false) {
    document.getElementById('value-b').append(' '+ correct_value)
    document.getElementById('value-b-strong').style.textDecoration = 'line-through';
  }
  document.getElementById(clicked_id).disabled = 'disabled';
  document.getElementById(other_id).disabled = 'disabled';
  document.getElementById('continue-button').disabled = '';
}