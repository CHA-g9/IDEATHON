function a_b(){
  var input_where = document.getElementById("myInput1").value;
  var input_much = document.getElementById("myInput2").value;
  var input_when = document.getElementById("myInput3").value;
  var a = input_where + " ";
  var b = input_much + "원";
  var q = document.getElementById(input_when.slice(5, ));
  var ele_tot_mon = document.getElementById("total_money");
  var total_money = parseInt(input_much);
  

  div = document.createElement('div');
  div.textContent = a + b;
  q.appendChild(div);
  q.className = "event";

  div2 = document.createElement('div');
  div2.textContent = b;
  ele_tot_mon.appendChild(div2);
  ele_ton_mon.className = "event";
}
