$(document).ready(function () {
  setDeleteModalId()
  deleteSelling()
})

function setDeleteModalId() {
  $('.selling').on('click', '.selling-delete', function () {
    var url = $(this).parent().parent().parent().data('delete-url')
    $('#confirmDeleteModal').data('url', url)
  })
}

function deleteSelling() {
  $('#confirmDeleteModal').on('click', '.selling-delete__confirm', function () {
    var url = $('#confirmDeleteModal').data('url')
    $.ajax({
      url: url,
      data: '',
      type: 'POST',
      dataType: 'json',
      headers: { 'X-CSRFToken': csrftoken }
    })
      .done(function (json) {
        if (json.success) {
          location.reload()
        }
      })
      .fail(function (xhr, status, errorThrown) {})
      .always(function (xhr, status) {})
  })
}

function getCookie(name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}
const csrftoken = getCookie('csrftoken')
