def b(browser)
script = <<JS
if ($('#_chat_message_area :last-child').eq(-2).attr("class") == "MdRGT10Notice mdRGT10Desc mdRGT07Other") {
	$(".MdBtn01Edit01").click();
	$('.mdRGT11Ttl').text("<快來改名稱> -屏東分校");
}
JS
	loop do
		a = browser.div(id: "_chat_message_area").html
	    sleep 0.1
		if browser.div(id: "_chat_message_area").html != a
			browser.execute_script(script)
			browser.send_keys :enter
		end
	end
end