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

  // set category value selected
  const category = $('.product-category').data('selected')
  $('#' + category).attr('selected', true)
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
