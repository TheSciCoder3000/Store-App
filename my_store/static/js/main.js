
const addi = {
  'scrollX': true
}
$('#prod_table').DataTable(addi);
$('#user-table').DataTable(addi);
$('#admin-table').DataTable(addi);

var use_ajax = true;
function deactivate_me(btn_id){
  if(!$(btn_id).hasClass("submitted")){
    $(btn_id).addClass("submitted");
    $.ajax({
      type: "GET",
      url: '/deactivate_btn/',
      dataType: 'json',
      success: function (data){
        if (data.msg == 'success'){
          $(btn_id).removeClass("submitted");
        }
      }

    });
  }
}   //Deactivate the button to avoid double ordering

function updateQuantity(){
  var order_message = document.getElementById('message-text');
  var order_form = document.getElementById('message-form');
  var quantityItems = document.querySelectorAll(".item-quantity");
  var quantityCounter = document.querySelectorAll(".item-quantity-counter > input[type='number']");
  var btn_id = document.getElementById("update-btn");
  var update_btns = document.getElementById("update-buttons");
  var i = 0;

  for (i = 0; i < quantityItems.length; i++) {
      quantityItems[i].classList.add("hidden");
      quantityCounter[i].style.display = "block";
  }
  order_message.classList.add("hidden");
  order_form.classList.remove("hidden");
  btn_id.classList.add("hidden");
  update_btns.classList.remove("hidden");
}

function cancelUpdate(){
  var quantityItems = document.querySelectorAll(".item-quantity");
  var quantityCounter = document.querySelectorAll(".item-quantity-counter > input[type='number']");
  var update_btns = document.getElementById("update-buttons");
  var update_btn = document.getElementById("update-btn");
  var order_message = document.getElementById('message-text');
  var order_form = document.getElementById('message-form');

  for (i = 0; i < quantityItems.length; i++) {
      quantityItems[i].classList.remove("hidden");
      quantityCounter[i].style.display = "none";
  }
  order_message.classList.remove("hidden");
  order_form.classList.add("hidden");
  update_btns.classList.add("hidden");
  update_btn.classList.remove("hidden");
}

function hide_me(this_item, id){
  var item_checkbox = document.querySelector("#"+ this_item +"-checkbox");
  var item_settings = document.querySelector("#"+ this_item +"-order");
  var IS_select = item_settings.childNodes[1];
  var IS_counter = item_settings.childNodes[3];

  if (item_checkbox.checked){
    IS_select.value = id.toString();
    IS_counter.style.display = "block";
    IS_counter.value = "1.00";
  }else {
    IS_select.value = "";
    IS_counter.style.display = "none";
    IS_counter.value = "";
  }
}   //Hide the number input of each item

function check_price(this_item, item_thresh, item_discount){
  var item_price = document.querySelector("#"+this_item+"-price").innerHTML;
  var item_count = document.querySelector("#form-"+this_item+"-counter").value;

  if (item_thresh == null){
  } else if (item_count > item_thresh){
    document.getElementById(this_item+"-price").innerHTML = parseInt(item_price)*(1-item_discount);
  }
}
