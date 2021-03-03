function loadhtml(element, url, onfinish) {
    httpreq = new XMLHttpRequest();
    httpreq.open('GET', url, true);
    httpreq.onload = function () {
        if (this.status >= 200 && this.status < 400) {
            element.innerHTML = this.response;
            onfinish();
        } else {
            console.log("error loading html");
        }
    }
    httpreq.send();
}