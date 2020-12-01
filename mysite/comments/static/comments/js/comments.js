$(document).ready(function () {
  $('.seller').on('mouseover', '.comment', function () {
    $(this).css({ background: '#E5E5E5' })
  })
  $('.seller').on('mouseout', '.comment', function () {
    $(this).css({ background: 'white' })
  })
  handleAddComment()
})

function handleAddComment() {
  $('.add-comment').click(function (event) {
    event.preventDefault()
    const comment = $('#add_comment').val()
    const seller_username = $(this).data('seller_username')
    const data = { comment: comment, seller_username: seller_username }
    var url = $(this).data('url')
    if (comment) {
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
              '<div class="form-group my-3 comment"><a href="' +
                data.buyer_url +
                '">' +
                data.buyer +
                '</a><span>' +
                data.date_posted +
                '</span><button class="btn btn-outline-secondary btn-sm" data-id="' +
                data.id +
                '">Edit</button><button class="btn btn-outline-danger btn-sm" data-id="' +
                data.id +
                '">Delete</button><input type="text" class="form-control" id="username" name="username" value="' +
                data.comment +
                '" disabled></div>'
            )
          }
        })
        .fail(function (xhr, status, errorThrown) {})
        .always(function (xhr, status) {})
    }
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
