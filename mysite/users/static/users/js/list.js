$(document).ready(function () {
  $('.change-role-btn').on('click', function (event) {
    event.preventDefault()
    const role = $(this).siblings().val()
    const id = $(this).data('id')
    const data = {
      id: id,
      role: role
    }
    const url = $(this).data('url')
    $.ajax({
      url: url,
      data: data,
      type: 'POST',
      dataType: 'json',
      headers: { 'X-CSRFToken': csrftoken }
    })
      .done(function (json) {
        if (json.success) {
          window.location.href = json.data.url
        }
      })
      .fail(function (xhr, status, errorThrown) {})
      .always(function (xhr, status) {})
  })
})

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
