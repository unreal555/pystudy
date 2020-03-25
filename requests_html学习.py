#!/bin/py
#   -*-coding:utf-8-*-
js='''
	_inlineRun(function(){
		var page = $(".mod-page");
		var isTouch = !!("ontouchstart" in window);
		var isMouse = !!("onmousemove" in window);

		var chapterView = $("#ChapterView"), body = $("body");
		var pageContent = chapterView.find(".page-content"), saveFont = core.cookie("current-font"), currentFont = 1;

		var font = function(){
			//font size;
			var sizes = ["font-normal", "font-large", "font-xlarge", "font-xxlarge", "font-xxxlarge"],
				level = sizes.length;

			return {
				set: function(c){
					console.log(sizes[currentFont])
					pageContent.toggleClass( sizes[currentFont] + " " + sizes[c] );
					currentFont = c;
					core.cookie("current-font", c, { expires: 3600 });
					core.cookie("currentFontString", sizes[c], { expires: 3600 });
				},
				increase: function(){
					if( currentFont < level - 1 ) {
						this.set(currentFont + 1)
					}
				},
				descrease: function(){
					if( currentFont > 0 ) {
						this.set( currentFont - 1 );
					}
				},
				day: function(){
					isNight = false;
					body.removeClass("night");
					core.cookie.removeCookie("night-mode", {});
				},
				night: function(){
					isNight = true;
					body.addClass("night");
					core.cookie("night-mode", true, { expires: 3600 });
				}
			}
		}();

		if( typeof saveFont !== "undefined" ){
			font.set(saveFont * 1);
		}

		var isNight = !!core.cookie("night-mode");

		if( isNight ){
			font.night();
		}

		function action(){
			var type = $(this).data("role");

			if( type == "inc" ){
				font.increase();
			}else if( type == "des" ) {
				font.descrease();
			}else if( type == "mode" ){
				if( isNight ){
					font.day();
				}else{
					font.night();
				}
			}
		}

		core.Tabs( $(".chapter-recommend .tab-choose a"), $(".chapter-recommend ul") )

		if( isTouch ){
			chapterView
				.on("touchstart MSPointerDown", ".config span", function(){
					$(this).addClass("active");
				})
				.on("touchend MSPointerUp", ".config span", function(){
					$(this).removeClass("active");
				});

			chapterView.on("touchend MSPointerUp", ".config span", action)
		}else if( isMouse ){
			chapterView.on("click", ".config span", action)
		}
	});
'''
js1='''
function getid(a) {
	return document.getElementById(a)
};

function attachevent(a, b, c) {
	b = b.toLowerCase();
	a.attachEvent ? a.attachEvent('on' + b, c) : a.addEventListener(b, c, false)
};

function nextSibling(a) {
	var n = a.nextSibling;
	return n && n.nodeType != 1 ? arguments.callee(n) : n
};

function preSibling(a) {
	var n = a.previousSibling;
	return n && n.nodeType != 1 ? arguments.callee(n) : n
};

function trim(s) {
	return s.replace(/^\s*/, '').replace(/\s*$/, '')
};

function get(a) {
	return encodeURI(trim(typeof a == 'object' ? a.value : $(a).value))
};

function addCookie(a, b, c) {
	var d = new Date();
	d.setFullYear(d.getFullYear() + 1);
	c = c ? c.substring(0, c.lastIndexOf('/')) : '/';
	document.cookie = a + '=' + encodeURIComponent(b) + '; path=' + c + '; max-age=' + (31536000) + '; expires=' + d.toGMTString()
};

function getCookie(a) {
	var b = new RegExp('(^|;) ?' + a + '=([^;]+)(;|$)');
	var c = b.exec(document.cookie);
	return c == null ? false : decodeURIComponent(c[2])
};

function delCookie(a, b) {
	var c = new Date();
	c.setFullYear(c.getFullYear() - 1);
	b = b ? b.substring(0, b.lastIndexOf('/')) : '/';
	document.cookie = a + '= ; path=' + b + '; max-age=0; expires=' + c.toGMTString()
};
base64 = {
	map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
	decode: function(a) {
		var b = binary = '';
		for (var i = 0; i < a.length; i++) {
			if (a.substr(i, 1) == '=') {
				break
			};
			var c = this.map.indexOf(a.charAt(i)).toString(2);
			binary += {
				1: '00000',
				2: '0000',
				3: '000',
				4: '00',
				5: '0',
				6: ''
			}[c.length] + c
		};
		binary = binary.match(/[0-1]{8}/g);
		for (var i = 0; i < binary.length; i++) {
			b += String.fromCharCode(parseInt(binary[i], 2))
		};
		return b
	}
};
content = {
	index: 0,
	step: 5,
	star: 0,
	add: 0,
	code: 0,
	state: 'load',
	showState: 'no',
	childNode: [],
	load: function() {
//		console.log(document.getElementsByTagName('meta'));
		var e = base64.decode(document.getElementsByTagName('meta')[5].getAttribute('content')).split(/[A-Z]+%/);
		var j = 0;
//		alert("OK");
		function r(a) {
			var c = '';
			var d = document.createElement('span');
			for (var i = 0; i < 20; i++) {
				var n = Math.floor(Math.random() * 99001 + 1000);
				c += String.fromCharCode(n)
			};
			var b = ['。', '：', '？', '！', '—', '…', '；', '，', '”', ''];
			c += b[Math.floor(Math.random() * b.length)];
			d.style.color = '#fff';
			d.style.fontSize = '0';
			d.style.lineHeight = '0';
			d.style.position = 'absolute';
			d.style.top = 0;
			d.style.left = 0;
			d.appendChild(document.createTextNode(c));
			
			a.appendChild(d);
			return a
		};
		for (var i = 0; i < e.length; i++) {
			var k = this.UpWz(e[i], i);
			this.childNode[k] = r(this.box.childNodes[i])
		};
		this.show()
	},
	UpWz: function(m, i) {
		var k = Math.ceil((i + 1) % this.code);
		k = Math.ceil(m - k);
		return k
	},
	check: function() {
		return this.showState == 'yes' && content.button.style.display != 'none' && this.offsetTop + this.button.offsetTop - Math.max(document.body.scrollTop, document.documentElement.scrollTop) < document.documentElement.clientHeight ? true : false
	},
	init: function(a, b, code) {
		if (!b) {
			return false
		};
		this.time = new Date().getTime();
		this.box = a;
		this.button = b;
		this.code = code;
		this.offsetTop = 0;
		this.randomContent = [];
		this.hiddenItem = [];
		this.showItem = [];

		function random() {
			return String.fromCharCode(Math.floor(Math.random() * 25 + 97)) + Math.floor(Math.random() * (1000000000))
		};
		var c = document.styleSheets[3];
		//console.log(document.styleSheets);
		for (var i = 0; i < 100; i++) {
			this.showItem.push(random());
			this.hiddenItem.push(random())
		};
		if (c.insertRule) {
			c.insertRule('#content .' + this.hiddenItem.join(',#content .') + '{display:none;}', 0);
			c.insertRule('#content .' + this.showItem.join(',#content .') + '{display:block;}', 0)
		} else {
			for (var i = 0; i < this.hiddenItem.length; i++) {
				c.addRule('#content .' + this.hiddenItem[i], 'display:none');
				c.addRule('#content .' + this.showItem[i], 'display:block')
			}
		};
		for (var i = 0; i < this.box.childNodes.length; i++) {
			if (this.box.childNodes[i].tagName == 'H2') {
				this.star = i + 1
			};
			if (this.box.childNodes[i].tagName == 'DIV' && this.box.childNodes[i].className != 'chapter') {
				break
			}
		};
		/\/([0-9]+)\/([0-9]+)\/([0-9]+)\.html/.test(location.href);
		this.sid = RegExp.$1 + "_" + RegExp.$2+ "_" + RegExp.$3;
		this.load();
		window.onscroll = function() {
			if (content.check()) {
				content.showNext()
			}
		}
	},
	show: function() {
		this.showState = 'no';
		var a = 0;
		for (var i = this.index; i < this.childNode.length; i++) {
			if (this.childNode[i].nodeType != 1) {
				continue
			};
			a += this.childNode[i].innerHTML.length;
			this.index = i + 1;
			this.childNode[i].className = content.showItem[Math.floor(Math.random() * 100)];
			this.box.appendChild(this.childNode[i]);
			for (var j = 0; j < 5; j++) {
				var b = this.childNode[Math.floor(Math.random() * this.childNode.length)].cloneNode(true);
				b.className = content.hiddenItem[Math.floor(Math.random() * 100)];
				this.box.appendChild(b)
			};
			if (a > 500) {
				break
			}
		};
		var c = getCookie(this.sid);
		if (!c || c < this.index || c > this.childNode.length + 1) {
			addCookie(this.sid, this.index, location.pathname)
		};
		content.time = getCookie(this.sid) > this.index ? 0 : new Date().getTime();
		if (this.index >= this.childNode.length) {
			this.button.style.display = 'none'
		} else {
			this.showState = 'yes';
			if (this.check()) {
				this.showNext()
			}
		}
	},
	showNext: function() {
		if (this.showState == 'no') {
			return false
		};
		this.showState = 'no';
		setTimeout(function() {
			content.show()
		}, Math.max(0 - (new Date().getTime() - content.time), 0))
	}
};

$(document).ready(function(){			
	check();
});
//  声明定时器
var timer = null
//  检查dom是否执行完成
function check() {
    let dom = document.getElementById('content')
    if(dom) {
		/\/([0-9]+)\/([0-9]+)\/([0-9]+)\.html/.test(location.href);
		var wzid = RegExp.$1+"_"+RegExp.$2+"_"+RegExp.$3;
		var o =document.getElementById('content');
		var btn=document.getElementById('cload');
		var id=0;
		var iID=0;
		content.init(o,btn,codeurl);
		iID=setInterval(function(){
			content.showNext();
		},100);
        //  清除定时器
        if(!timer) {
            clearTimeout(timer)
        }
    } else {
        timer = setTimeout(check, 0)
    }
}
'''
from requests_html import HTMLSession
session=HTMLSession()
r=session.get('http://www.skwen.me/13/13577/185654.html')


dom=r.html.render(script=js1, reload=False)
print(dom)


