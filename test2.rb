def b(browser)
script = <<JS
$(".MdBtn01Edit01").click();
$('.mdRGT11Ttl').text("<改名稱 練手速> -屏東分校");
JS
	while browser.div(id: 'groupInfoLayer').present? do
		#a = browser.div(id: "_chat_message_area").html
	    sleep 0.1
		#if browser.div(id: "_chat_message_area").html != a
		if browser.a(class: "mdRGT11Ttl").present? && browser.a(class: "mdRGT11Ttl").text != "<改名稱 練手速> -屏東分校"
			browser.execute_script(script)
			browser.send_keys :enter
		end
	end
end