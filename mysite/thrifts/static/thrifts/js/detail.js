$(document).ready(function () {
  // $('.seller').on('mouseover', '.comment', function () {
  //   $(this).css({ background: '#E5E5E5' })
  // })
  // $('.seller').on('mouseout', '.comment', function () {
  //   $(this).css({ background: 'white' })
  // })
  // confirmCartModal()
  removeCartModal()
  addItemToCart()
})

function addItemToCart() {
  $('#add-cart').click(function (event) {
    event.preventDefault()
    const url = $(this).data('url')
    const data = { product_id: $(this).data('product-id') }
    $.ajax({
      url: url,
      data: data,
      type: 'POST',
      dataType: 'json',
      headers: { 'X-CSRFToken': csrftoken },
      context: this
    })
      .done(function (json) {
        console.log(json)
        if (json.success) {
          const modal = $(
            '<div class="modal-container"><div class="modal-content">' +
              json.success +
              '</div></div>'
          )
          modal.appendTo($(this).parent())
          $('body').css({ overflow: 'hidden' })
        }
      })
      .fail(function (xhr, status, errorThrown) {})
      .always(function (xhr, status) {})
  })
}

function confirmCartModal() {
  $('#add-cart').click(function () {
    const modal = $(
      '<div class="modal-container"><div class="modal-content">You have succesfully added to cart!</div></div>'
    )
    modal.appendTo($(this).parent())
    $('body').css({ overflow: 'hidden' })
  })
}

function removeCartModal() {
  $('.product__description').on('click', '.modal-container', function () {
    $(this).remove()
    $('body').css({ overflow: 'revert' })
  })
}
