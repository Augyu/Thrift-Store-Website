$(document).ready(function () {
  handleInput()
  createAccount()
})

const checkList = ['fName', 'lName', 'birth', 'email']

const createAccount = function () {
  const signUpBtn = $('#signUpBtn')
  signUpBtn.on('click', function (event) {
    event.preventDefault()
    const url = $(this).data('url')
    if (checkInfoValid()) {
      const fName = $('#fName').val()
      const lName = $('#lName').val()
      const email = $('#email').val()
      const birth = $('#birth').val()
      const data = {
        fName: fName,
        lName: lName,
        email: email,
        birth: birth
      }
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
    }
  })
}

const checkInfoValid = function () {
  let isValid = true

  const setErrorIfEmpty = function (element) {
    if ($('#' + element).val() === '') {
      $('#' + element + '-error').text('Please enter your' + element + ' .')
      isValid = false
    }
  }
  checkList.forEach(setErrorIfEmpty)
  return isValid
}

const handleInput = function () {
  // username
  const clearErrorMsg = function (element) {
    $('#' + element).on('input', function () {
      $('#' + element + '-error').empty()
    })
  }
  checkList.forEach(clearErrorMsg)
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
