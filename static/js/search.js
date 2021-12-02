const searchEI = document.querySelector('.search');
const searchInputEI = searchEI.querySelector('input');

searchEI.addEventListener('click', function(){
    searchInputEI.focus();
});

searchInputEI.addEventListener('focus', function() {
    searchInputEI.classList.add('focused');
    searchInputEI.setAttribute('placeholder', '검색어를 입력하세요.');
});

searchInputEI.addEventListener('blur', function() {
    searchInputEI.classList.remove('focused');
    searchInputEI.removeAttribute('placeholder', '');
});