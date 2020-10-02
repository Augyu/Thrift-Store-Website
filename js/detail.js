$(document).ready(function () {
  $('.seller').on('mouseover', '.comment', function () {
    $(this).css({ background: '#E5E5E5' })
  })
  $('.seller').on('mouseout', '.comment', function () {
    $(this).css({ background: 'white' })
  })
})
