$(document).ready(function () {
  $('#image').change((e) => previewImage(e))
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
