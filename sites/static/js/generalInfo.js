
function showCompany(dName, dLink, dPhone, dAddress, dComments, dCommentators) {
    var cName    = document.getElementById('cName');
    var cSite    = document.getElementById('cSite');
    var cPhone   = document.getElementById('cPhone');
    var cAddress = document.getElementById('cAddress');
    //var cRating  = document.getElementById('cRating');

console.log('-', dComments)
console.log('+', dCommentators)

    cName.innerHTML = dName;
    cSite.innerHTML = dLink;
    cSite.href = dLink;
    cPhone.innerHTML = dPhone;
    cAddress.innerHTML = dAddress;

    showItem('companyInfo');

    for(var item of dComments) {
        addComment(item.fields.comment);
        addComment(item.fields.rate);
        addComment(item.fields.candlesite);
        addComment(item.fields.commentator);
    }

}

function showItem(dItem) {
    var item2Close = document.getElementById(dItem);
    item2Close.style.display = 'block';
}

function hideItem(dItem) {
    var item2Close = document.getElementById(dItem);
    item2Close.style.display = 'none';
}

function captureRecSite(dNewItem) {
    var recSites = document.getElementById('id_recSites');
    var newItem  = document.getElementById(dNewItem).value;
    var newLi = document.createElement('li');
    var liText = document.createTextNode(newItem);
    newLi.appendChild(liText);
    recSites.appendChild(newLi);
}

function addComment( dComment ) {
    var docInfo = document.getElementById('companyInfo');
    var newP = document.createElement('p');
    var pText = document.createTextNode(dComment);
    newP.appendChild(pText);
    newP.className = 'commClass';
    docInfo.appendChild(newP);
}