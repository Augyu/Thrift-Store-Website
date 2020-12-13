$(document).ready(function () {
  $('.seller').on('mouseover', '.comment', function () {
    $(this).css({ background: '#E5E5E5' })
  })
  $('.seller').on('mouseout', '.comment', function () {
    $(this).css({ background: 'white' })
  })
  handleAddComment()
  handleDeleteComment()
  handleEditComment()
  handleUpdateComment()
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
            $('#add_comment').val('')
            $('.comment-container').prepend(
              '<div class="form-group my-3 comment"><a href="' +
                data.buyer_url +
                '">' +
                data.buyer +
                '</a><span>' +
                data.date_posted +
                '</span><button class="btn btn-outline-secondary btn-sm edit-comment" data-id="' +
                data.id +
                '">Edit</button><button class="btn btn-outline-secondary btn-sm update-comment" data-id="' +
                data.id +
                '">Update</button><button class="btn btn-outline-danger btn-sm delete-comment" data-id="' +
                data.id +
                '">Delete</button><input type="text" class="form-control" name="username" value="' +
                data.comment +
                '" disabled></div>'
            )
            $('.empty-container').empty()
          }
        })
        .fail(function (xhr, status, errorThrown) {})
        .always(function (xhr, status) {})
    }
  })
}

function handleDeleteComment() {
  $('div').on('click', '.delete-comment', function (event) {
    event.preventDefault()
    event.stopPropagation()
    const parentDiv = $(this).parent()
    const comment_id = $(this).data('id')
    const url = $('.comment-container').data('delete-url')
    $.ajax({
      url: url,
      data: { id: comment_id },
      type: 'POST',
      dataType: 'json',
      headers: { 'X-CSRFToken': csrftoken }
    })
      .done(function (json) {
        if (json.success) {
          parentDiv.remove()
        }
      })
      .fail(function (xhr, status, errorThrown) {})
      .always(function (xhr, status) {})
  })
}

function handleUpdateComment() {
  $('div').on('click', '.update-comment', function (event) {
    event.preventDefault()
    event.stopPropagation()
    const comment_id = $(this).data('id')
    const url = $('.comment-container').data('edit-url')
    const input = $(this).parent().find('input')
    const comment = input.val()

    $.ajax({
      url: url,
      data: { id: comment_id, comment: comment },
      type: 'POST',
      dataType: 'json',
      headers: { 'X-CSRFToken': csrftoken }
    })
      .done(function (json) {
        if (json.success) {
          input.attr('disabled', true)
          input.prev().css('display', 'inline-block')
          input.prev().prev().css('display', 'none')
          input.prev().prev().prev().css('display', 'inline-block')
        }
      })
      .fail(function (xhr, status, errorThrown) {})
      .always(function (xhr, status) {})
  })
}

function handleEditComment() {
  $('div').on('click', '.edit-comment', function (event) {
    event.preventDefault()
    event.stopPropagation()
    const input = $(this).parent().find('input')
    const comment_id = $(this).data('id')
    input.removeAttr('disabled')
    $(this).css('display', 'none')
    $(this).next().next().css('display', 'none')
    $(this).next().css('display', 'inline-block')
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
