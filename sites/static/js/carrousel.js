
var bkgImageItem = document.getElementById("mainDiv");
var firstImag = 1;
const totImgs = 39;
const pathPrefix = 'url("../../static/img/';
const pathSufixx = '.jpg")';

function chgBkgImage() {
    if( firstImag > totImgs ) { firstImag = 1; }
    console.log(bkgImageItem);
    console.log(pathPrefix + firstImag++ + pathSufixx);
    bkgImageItem.style.backgroundImage = pathPrefix + firstImag++ + pathSufixx;
    
}

// Execute Carrousel loop
setInterval( chgBkgImage, 5000 );