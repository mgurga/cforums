function loadhtml(element, url, onfinish) {
    httpreq = new XMLHttpRequest();
    httpreq.open('GET', url, true);
    httpreq.onload = function () {
        if (this.status >= 200 && this.status < 400) {
            element.innerHTML = this.response;

            scripttags = element.getElementsByTagName("script");
            for(var i = 0; i < scripttags.length; i++) {
                eval(scripttags[i].innerHTML);
            }

            onfinish();
        } else {
            console.log("error loading html");
        }
    }
    httpreq.send();
}

function getlocaltime(utctime) {
    utcdate = new Date(utctime);
    localtz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    localtime = utcdate.toLocaleString("en-US", {timeZone: localtz});
    return localtime;
}