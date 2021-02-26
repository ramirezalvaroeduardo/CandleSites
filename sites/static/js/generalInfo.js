
function showCompany(dSiteId, dName, dLink, dPhone, dAddress, dSites, dComments, dCommentators) {
    var cName    = document.getElementById('cName');
    var cSite    = document.getElementById('cSite');
    var cPhone   = document.getElementById('cPhone');
    var cAddress = document.getElementById('cAddress');
    //var cRating  = document.getElementById('cRating');
    var cComments = []

    cName.innerHTML = dName;
    cSite.innerHTML = dLink;
    cSite.href = dLink;
    cPhone.innerHTML = dPhone;
    cAddress.innerHTML = dAddress;

    var docInfo = document.getElementById('companyInfo');
    var commId  = document.getElementById('commDiv');
    commId.remove();
    var newDiv = document.createElement('div');
    newDiv.id = 'commDiv';
    newDiv.style = 'padding-top: 1rem;';
    docInfo.appendChild(newDiv);

    // Adding Comment to Company Info Item
    for(var item of dComments) {
        if(item.fields.candlesite == dSiteId) {
            var dCommtr;
            // Showing Commentator Name
            for(var item2 of dCommentators) {
                if(item2.pk == item.fields.commentator) dCommtr = item2.fields.username;
            }        
            addComment(item.fields.comment, item.fields.rate, dCommtr);
        }
    }

    showItem('companyInfo');
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

function addComment( dComment, dRate, dCommtr ) {
    var docInfo = document.getElementById('commDiv');
    var newDiv = document.createElement('div');
    var newP;
    var newR;
    var pText;

    newP = document.createElement('p');
    pText = document.createTextNode(dCommtr);
    newP.appendChild(pText);
    newP.className = 'commClassCommentator';
    newDiv.appendChild(newP);

    newR = document.createElement('p');
    pText = document.createTextNode(dRate);
    newR.appendChild(pText);
    newR.className = 'commClassRate';
    newP.appendChild(newR);

    newP = document.createElement('p');
    pText = document.createTextNode(dComment);
    newP.appendChild(pText);
    newP.className = 'commClass';
    newDiv.appendChild(newP);

    newDiv.className = 'commDivClass';
    docInfo.appendChild(newDiv);
}