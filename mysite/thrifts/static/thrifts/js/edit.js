$(document).ready(function () {
  // preview the image
  $('#image').change((e) => {
    const msg = $('<p>Upload Success!</p>')
    isPreviewImageSuccess(e) && handleMsg(e.currentTarget, msg, true)
  })

  // delete preview image
  $('.edit-form__right div div button')
    .last()
    .click((e) => {
      const msg = $('<p>Delete Image!</p>')
      isDeleteImageSuccess(e) && handleMsg(e.currentTarget, msg, false)
    })

  $('.edit-form__right button').click((e) => e.preventDefault())

  // button trigger input on click
  $('.upload').click(() => $('#image').click())
})

// the image box will change according to user's selected image
const isPreviewImageSuccess = (e) => {
  if (e.target.files.length > 0) {
    const imgHolder = $('#preview-image')
    const src = URL.createObjectURL(e.target.files[0])
    $(imgHolder).attr('src', src).css({ visibility: 'visible' })
    $(imgHolder).on('load', () => URL.revokeObjectURL(src))
    return true
  }
  return false
}

const isDeleteImageSuccess = () => {
  try {
    $('#preview-image').attr('src', '#').css({ visibility: 'hidden' })
    return true
  } catch (e) {
    console.log(e)
    return false
  }
}

const handleMsg = (target, msg, isUpload) => {
  const color = isUpload ? '#508590' : '#CE0058'
  $(msg)
    .css({
      color: color,
      position: 'absolute',
      borderRadius: '2px',
      padding: '4px',
      display: 'none'
    })
    .appendTo($(target).parent())
    .fadeIn(1000)
    .fadeOut(2000)
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
