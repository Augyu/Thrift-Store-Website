$(document).ready(function () {
  handleLeaveComment()
})

function handleLeaveComment() {
  $('.leave-comment-container button').click(function (event) {
    event.preventDefault()
    const comment = $('#leave_comment').val()
    const data = { comment: comment }
    var url = $(this).data('url')
    $.ajax({
      url: url,
      data: data,
      type: 'POST',
      dataType: 'json',
      headers: { 'X-CSRFToken': csrftoken }
    })
      .done(function (json) {
        if (json.success) {
          const data = json.data
          $('#leave_comment').val('')
          $('.comment-container').prepend(
            '<div class="comment"><div><a>' +
              data.buyer +
              '</a><span>' +
              data.date_posted +
              '</span></div><p>' +
              data.comment +
              '</p></div>'
          )
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
