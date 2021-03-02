function loadhtml(element, url) {
    httpreq = new XMLHttpRequest();
    httpreq.open('GET', url, true);
    httpreq.onload = function () {
        if (this.status >= 200 && this.status < 400) {
            element.innerHTML = this.response;
            console.log(element);
        } else {
            console.log("error loading html");
        }
    }
    httpreq.send()
}