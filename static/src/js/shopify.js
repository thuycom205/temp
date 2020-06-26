  var txt1 = '<p class="line-item-property__field">\n' +
      '  <label for="from">From</label>\n' +
      '  <input required class="required" id="from" type="date" name="properties[From]">\n' +
      '</p>';

  var txt2 ='<p class="line-item-property__field">\n' +
      '  <label for="to">To</label>\n' +
      '  <input required class="required" id="to"  type="date" name="properties[To]">\n' +
      '</p>';
  // Create element with HTML
// var select1 = '<p class="line-item-property__field">\n' +
//     '  <label>Delivery type</label><br>\n' +
//     '  <select required class="required" id="delivery-type" name="properties[Delivery type]">\n' +
//     '    <option value="Local Pickup">Local Pickup</option>\n' +
//     '    <option value="Shipping">Shipping</option>\n' +
//     '  </select>\n' +
//     '</p>';

jQuery('.product-form__controls-group').first().before(txt1,txt2);

