$(document).ready(function () {
  getProductBySorting()

  var sorting = $('#product-sorting').attr('data-selected')
  $('#' + sorting).attr('selected', true)
})

function getProductBySorting() {
  $('#product-sorting').on('change', function () {
    const type = this.value
    var url = window.location.href
    if (url.includes('sorting')) {
      url = url.replace(/(sorting=)[^\&]+/, '$1' + type)
    } else {
      if (url.slice(-1) === '/') {
        url = url + '?sorting=' + type
      } else {
        url = url + '&sorting=' + type
      }
    }
    window.location.href = url
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
