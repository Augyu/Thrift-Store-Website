$(document).ready(function () {
  handleSearchResult()
})

// if users search electronics then the list will show up
// otherwise, show no result page
const handleSearchResult = () => {
  const queryString = new URLSearchParams(window.location.search)
  const search = queryString.get('search')
  changeSearchValue(search)
  if (search === 'electronics' || search === 'Electronics') {
    $('.no-result-container').hide()
  } else {
    $('.left-container').hide()
    $('.middle-container').hide()
    $('.right-container').hide()
  }
}

// change the value of the search bar with the search value
const changeSearchValue = (searchVal) => {
  $('#search-middle').attr('value', searchVal)
}
