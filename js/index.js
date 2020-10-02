$(document).ready(function () {
  //   mobileSearch()
})

const mobileSearch = () => {
  $('.main-header__right a').click(function () {
    const div = $('<div><a href="#">X</a></div>')
    $(div).css({
      width: '100vw',
      height: '100vh',
      position: 'absolute',
      float: 'right',
      right: '0',
      top: '0',
      background: 'grey'
    })

    $('body').append(div).css({ overflow: 'hidden' })
  })
}
