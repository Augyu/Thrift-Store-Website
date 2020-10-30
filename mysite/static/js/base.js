$(document).ready(function () {
  $('.message-close').on('click', function () {
    return $('.message').animate({ width: 0, height: 30 }, function () {
      $('.message').remove()
    })
  })
})
