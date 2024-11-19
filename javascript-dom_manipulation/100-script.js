document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('add_item').addEventListener('click', function () {
        const ul =  document.querySelector('.my_list');
        const list = document.createElement('li');
        list.appendChild(document.createTextNode('Item'));
        ul.appendChild(list);
    })
    
    document.getElementById('remove_item').addEventListener('click', function () {
        const ul =  document.querySelector('.my_list');
        const list = ul.lastElementChild;
        ul.removeChild(list);
    })

    document.getElementById('clear_list').addEventListener('click', function () {
        const ul =  document.querySelector('.my_list');
        ul.innerHTML = '';
    })
});