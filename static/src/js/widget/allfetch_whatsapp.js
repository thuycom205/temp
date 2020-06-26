function getShop() {
		if (null != window.Shopify) return window.Shopify.shop;
		var e = window.location.href;
		return (e.indexOf("://") > -1 ? e.split("/")[2] : e.split("/")[0]).split(":")[0]
	} ;

	function mobilecheck() {
		var e, t = !1;
		return e = navigator.userAgent || navigator.vendor || window.opera, (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(e) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(e.substr(0, 4))) && (t = !0), t
	};
	function is_order_checkout_page() {
		return !(!window.location.pathname.match("(.*)/orders/(.*)") && !window.location.pathname.match("(.*)/checkouts/(.*)"))
	}

	function is_product_page() {
		return !!window.location.pathname.match("(.*)/products/(.*)")
	}

	function _is_product_collection_page() {
		return !(!window.location.pathname.match("(.*)/collections/(.*)") && !window.location.pathname.match("(.*)/collections") || window.location.pathname.match("(.*)/products/(.*)") || window.location.pathname.match("(.*)/products"))
	}

	function  createChatWidget() {
		var html = '<div id="wa-chat-btn-root" class="wa-chat-btn-fixed wa-splmn-chat-btn-offset wa-custom-chat-btn btn_custom_class: wa-chat-btn-base-cta wa-chat-btn-container-size-big wa-chat-btn-theme-cta-new-inverted" style="background: rgb(34, 206, 90);"><div class="wa-chat-btn-icon-cta-big wa-custom-icon wa-icon-mask" style="background: #ffffff"></div><div class="wa-chat-button-cta-text" style="color: #ffffff">Chat with us</div></div>';
        var txt2 = $("<div></div>").html(html);
        jQuery("body").append(txt2);

	}
	createChatWidget();
	function  createChatPanel() {
		var html = '<div id="wa-chat-bubble" class="wa-chat-bubble-floating-popup animated wa-greeting-widget-z-index wa-chat-bubble-pos-right bounceUp"><div class="wa-chat-bubble-header-common wa-chat-bubble-header-301" style="background-image: linear-gradient(110.56deg, rgb(32, 128, 44) 0%, rgb(48, 191, 66) 100%);"><div class="wa-chat-bubble-close-btn"><img style="display: table-row" src="https://cdn.shopify.com/s/files/1/0070/3666/5911/files/Vector.png?574"></div><div class="wa-chat-bubble-header-title" style="color: rgb(255, 255, 255);">Hi there 👋</div><div class="wa-chat-bubble-header-desc" style="color: rgb(255, 255, 255);">We are here to help. Chat with us on WhatsApp for any queries.</div></div><div class="wa-chat-bubble-chat"><div class="wa-chat-multiple-cs"><div class="list-cs"><div><img class="wa-chat-bubble-whatsapp-avatar" src="https://cdn.shopify.com/s/files/1/0070/3666/5911/files/tiny-logo.png?840"><div class="wa-chat-bubble-avatar"><img style="height: 55px; width: 55px; border-radius: 50%; background: #20802C;" class="avatar-theme-301" src="https://cdn.shopify.com/s/files/1/0070/3666/5911/files/male-avatar-1.svg?v=1583717709"></div></div><div class="wa-chat-bubble-cs-profile"><div class="wa-chat-bubble-profile-name">Andy</div><p>Agent role</p></div></div><div class="list-cs"><div><img class="wa-chat-bubble-whatsapp-avatar" src="https://cdn.shopify.com/s/files/1/0070/3666/5911/files/tiny-logo.png?840"><div class="wa-chat-bubble-avatar"><img style="height: 55px; width: 55px; border-radius: 50%; background: #20802C;" class="avatar-theme-301" src="https://cdn.shopify.com/s/files/1/0070/3666/5911/files/male-avatar-1.svg?v=1583717709"></div></div><div class="wa-chat-bubble-cs-profile"><div class="wa-chat-bubble-profile-name">meogaming Admin</div><p>Customer Support</p></div></div></div></div><div class="wa-chat-widget-footer"><span style="vertical-align: middle;">Powered by <span class="wa-chat-widget-footer-superlemon">AllFetch</span></span></div></div>';
		var txt2 = $("<div></div>").html(html);
        jQuery("body").append(txt2);
	}
     createChatPanel();
	function  createOptinWidget() {
		var html = '<div id="whatsapp-optin-input-box" style="position: fixed;width: 100%;height: auto;background: #fdfdfd;z-index: 2147483647;bottom: 0px;box-shadow: 1px 1px 9px 4px #4444444d;max-width: 550px;margin: 0 auto; left: 0px;"><p style="width: 100%;padding: 5px;margin: 0px;font-weight: bold;  margin-left: 12px;    font-family: calibri;">🚚 Get Order Updates &amp; Offers on Whatsapp!</p><span style="position: absolute;top: 6px;right: 7px;background: #FF5257;margin: 0px;color: #ffffffed;line-height: 5px;border-radius: 18px;width: 23px;height: 23px;padding: 6px 0px 0px 6px;font-size: 20px;cursor: pointer;    font-family: sans-serif;" id="whatsapp-optin-close">x</span><div style="display: flex;box-shadow: 1px 2px 10px 2px #cccccc9e;margin: 5px 15px 15px;"><input type="text" id="whatsapp-optin-input" placeholder="Whatsapp Number with Country Code." style="background: none; border: 0px;padding: 10px;margin: 0px;width: 100%; height: 50px; "><input id="whatsapp-optin-submit" type="button" value="✓" style="cursor: pointer; background: #1EB89F;color: white;font-weight: bold;font-size: 20px;border: none;min-width: 50px;margin: 0px; width: 50px;"></div></div>';
        		var txt2 = $("<div></div>").html(html);

        jQuery("body").append(txt2);
	}
	 createOptinWidget();

	function clickAgentChat() {
		var number = arguments[0];
		var url = arguments[1];
		console.log(number);
		console.log(url);

	}
	clickAgentChat('84972873899', 'meugaming.com');
	
	function  toggleWidget() {

	}
	
	function clickOptIn() {

	}