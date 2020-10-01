$(document).ready(function () {
  // preview the image
  $('#image').change((e) => previewImage(e))

  // detele preview image
  $('.create-form__right div div button')
    .last()
    .click((e) => {
      deleteImage(e)
    })

  $('.create-form__right button').click((e) => e.preventDefault())

  // button trigger input on click
  $('.upload').click(function () {
    $('#image').click()
  })
})

// the image box will change according to user's selected image
const previewImage = (e) => {
  if (e.target.files.length > 0) {
    const src = URL.createObjectURL(e.target.files[0])
    $('#preview-image').attr('src', src)
    $('#preview-image').load(() => {
      URL.revokeObjectURL(src)
    })
  }
}

const deleteImage = () => {
  $('#preview-image').attr('src', '')
}
