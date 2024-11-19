

document.querySelector('#add_item').addEventListener('click', function () {
    const ul =  document.querySelector('.my_list');
    const list = document.createElement('li');
    list.appendChild(document.createTextNode('Item'));
    ul.appendChild(list);
}
);