def a(browser)
script = <<JS
$(".MdBtn01Edit01").click();
$('.mdRGT11Ttl').text("
JS
	while browser.div(id: 'groupInfoLayer').present? do
		#a = browser.div(id: "_chat_message_area").html
	    sleep 0.1
		#if browser.div(id: "_chat_message_area").html != a
		tmpnm = browser.a(class: "mdRGT11Ttl").text
		kid = browser.time(css = ".MdRGT10Notice mdRGT10Desc mdRGT07Other")
		if browser.a(class: "mdRGT11Ttl").present? && (gpname = tmpnm.gsub([/(?:胡|古|月)(.?| +)(?:鈞|金勻)/], kid)) != tmpnm
			gpname = "<改名稱 練手速> -屏東分校\"\)\;"
			browser.execute_script(script+gpname)
			browser.send_keys :enter
		end
	end
end
胡金勻