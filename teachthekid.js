btn = $(".MdBtn01Edit01");
txtfld = $('.mdRGT11Ttl');


/*
txtfld.bind("teachthekid",function(e){
alert("Enter");
});
txtfld.keyup(function(e){
if(e.keyCode == 13)
{
  $(this).trigger("teachthekid");
}
});
*/
 
var observeDOM = (function(){
    var MutationObserver = window.MutationObserver || window.WebKitMutationObserver,
        eventListenerSupported = window.addEventListener;

    return function(obj, callback){
        if( MutationObserver ){
            // define a new observer
            var obs = new MutationObserver(function(mutations, observer){
                if( mutations[0].addedNodes.length || mutations[0].removedNodes.length )
                    callback();
            });
            // have the observer observe foo for changes in children
            obs.observe( obj, { childList:true, subtree:true });
        }
        else if( eventListenerSupported ){
            obj.addEventListener('DOMNodeInserted', callback, false);
            obj.addEventListener('DOMNodeRemoved', callback, false);
        }
    };
})();

// Observe a specific DOM element:
observeDOM( document.getElementById('_chat_message_area') ,function(){ 
	if $('#_chat_message_area:last_child').text == 'syllu'{
		$(".MdBtn01Edit01").click();
    	$('.mdRGT11Ttl').text('Test succs');
	}    

});


browser=Watir::Browser.start("https://chrome.google.com/webstore/detail/line/menkifleemblimdogmoihpfopnplikde?utm_source=chrome-ntp-icon", browser=:chrome)
browser.div(class: "dd-Va g-c-wb g-eg-ua-Uc-c-za g-c-Oc-td-jb-oa g-c").click

script = <<-JAVASCRIPT
var observeDOM = (function(){
    var MutationObserver = window.MutationObserver || window.WebKitMutationObserver,
        eventListenerSupported = window.addEventListener;

    return function(obj, callback){
        if( MutationObserver ){
            // define a new observer
            var obs = new MutationObserver(function(mutations, observer){
                if( mutations[0].addedNodes.length || mutations[0].removedNodes.length )
                    callback();
            });
            // have the observer observe foo for changes in children
            obs.observe( obj, { childList:true, subtree:true });
        }
        else if( eventListenerSupported ){
            obj.addEventListener('DOMNodeInserted', callback, false);
            obj.addEventListener('DOMNodeRemoved', callback, false);
        }
    };
})();

// Observe a specific DOM element:
observeDOM( document.getElementById('_chat_message_area') ,function(){ 
//	if $('#_chat_message_area:last_child').text == 'syllu'{
		$(".MdBtn01Edit01").click();
    	$('.mdRGT11Ttl').text('Test succs');
    	return "dom changed";
//	}    
});
JAVASCRIPT

browser.execute_script(script)


