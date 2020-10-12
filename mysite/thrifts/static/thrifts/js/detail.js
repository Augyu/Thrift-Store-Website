$(document).ready(function () {
  $('.seller').on('mouseover', '.comment', function () {
    $(this).css({ background: '#E5E5E5' })
  })
  $('.seller').on('mouseout', '.comment', function () {
    $(this).css({ background: 'white' })
  })
  confirmCartModal()
  removeCartModal()
})

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
