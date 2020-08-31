import time
import re
from selenium import webdriver
import my_html_tools

html=r'''<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1" />
<title>CTR20201763详细信息</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1" />

<meta name="viewport" />

<meta http-equiv="content-type" content="text/html; charset=UTF-8" />

<style></style>
<!--[if lt IE 9]><script r='m'>document.createElement("section")</script><![endif]--><script></script>
<meta name="SiteName" content="国家药审" />
<meta name="SiteDomain" content="http://chinadrugtrials.org.cn" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<meta name="Keywords" content="查询详细信息" />
<meta name="ColumnKeywords" content="查询详细信息" />
<meta name="ColumnName" content="null" />
<meta name="ColumnType" content="null" />
<meta name="ColumnDescription" content="null" />
<meta name="ArticleTitle" content="CTR20201763详细信息" />
<meta name="Description" content="CTR20201763详细信息查询详细信息" />
<link href="/resource/css/bootstrap.min.css" rel="stylesheet" />
<link href="/resource/css/font-awesome.min.css" rel="stylesheet" />
<link href="/resource/css/bootstrap-select.min.css" rel="stylesheet" />
<link href="/skin/skin_01/style.css" rel="stylesheet" />
<link href="/resource/js/layer/skin/layer.css" rel="stylesheet" />
<link href="/resource/js/layer/skin/layer.ext.css" rel="stylesheet" />
<link href="/skin/origin.css" rel="stylesheet" />
<!--[if !IE]><!-->
<script type="text/javascript" src="/resource/js/jquery-2.1.4.min.js"></script>
<!-- <![endif]-->
<!--[if IE]>
<script src="/resource/js/jquery-1.11.3.min.js"></script>
<![endif]-->
<script src="/resource/js/clientmediatype.js"></script><style>@keyframes nodeInserted{from{outline-color:#fff}to{outline-color:#000}}@-moz-keyframes nodeInserted{from{outline-color:#fff}to{outline-color:#000}}@-webkit-keyframes nodeInserted{from{outline-color:#fff}to{outline-color:#000}}@-ms-keyframes nodeInserted{from{outline-color:#fff}to{outline-color:#000}}@-o-keyframes nodeInserted{from{outline-color:#fff}to{outline-color:#000}}.ace-save-state{animation-duration:10ms;-o-animation-duration:10ms;-ms-animation-duration:10ms;-moz-animation-duration:10ms;-webkit-animation-duration:10ms;animation-delay:0s;-o-animation-delay:0s;-ms-animation-delay:0s;-moz-animation-delay:0s;-webkit-animation-delay:0s;animation-name:nodeInserted;-o-animation-name:nodeInserted;-ms-animation-name:nodeInserted;-moz-animation-name:nodeInserted;-webkit-animation-name:nodeInserted}</style>
<link rel="stylesheet" href="http://www.chinadrugtrials.org.cn/resource/js/layer/skin/layer.css" id="layui_layer_skinlayercss" style="" /><link rel="stylesheet" href="http://www.chinadrugtrials.org.cn/resource/js/layer/skin/layer.ext.css" id="layui_layer_skinlayerextcss" style="" /></head>
<body class="" ads="" style="background-color: rgb(244, 244, 244); min-height: 264px;">
    <header class="" style="">
	<div class="row " style="background-color: #3f69c4; box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);">
			<div class="container" style="">
				<div class="column col-sm-3 col-md-3" style=""><div class="skin_01 eapblock " id="block1" style=""><style>
/*内容样式片段*/
.wrap_428 .widget-body{
	
}
</style>

<div class="wrap_428">
	<div class="widget-wrap">
	    <div style="height: 80px;padding-top: 18px;">
    <img src="/website/img/logoFront.png" alt="" />
</div>
	</div>
</div></div></div>
				<div class="column col-sm-9 col-md-9" style="position: relative; padding-right: 140px;"><div class="skin_01 eapblock " id="block2" style=""><script type="text/javascript" src="/resource/js/leftnav/jquery.mmenu.all.min.js"></script>


<div class="widget-menuwrap">
    

    

    <div id="hader-title" class="header-bg hidden-sm hidden-md hidden-lg">
        <a href="#widget-menu"></a>
        药物临床试验登记与信息公示平台
    </div>

    <nav id="widget-menu">
        <ul class="widget-nav clearfix">
            <li>
                <a target="_self" href="/index.html">
                首页
                </a>
            </li>
            <li>
                <a target="_self" href="/clinicaltrials.prosearch.dhtml">
                试验公示和查询
                </a>
            </li>
            <li>
                <a target="_self" href="/clinicaltrials.index.dhtml">
                试验登记
                </a>
            </li>
            <li>
                <a target="_self" href="/genericdrugs.index.dhtml">
                备案平台
                </a>
            </li>
            <li>
                <a target="_self" href="/clinicaltrials.tongji.dhtml">
                信息统计
                </a>
            </li>
            <li>
                <a target="_self" href="/helpLink.html">
                帮助与链接
                </a>
            </li>
            <li>
                <a target="_self" href="/snipet/434.html">
                关于平台
                </a>
            </li>

        </ul>
    </nav>
</div>



<script type="text/javascript">
    var str;
    $(function() {
        str = $(".widget-menuwrap").html();
        window.onload=function() {
            initLayout();
            $(window).resize(function(){
                initLayout();
            });
        };
    });
    function initLayout() {
        map_width=document.documentElement.clientWidth;
        if(map_width&lt;768){
            $('nav#widget-menu').mmenu({
                extensions	: [ 'effect-slide-menu', 'pageshadow','theme-white' ],
                counters	: false,
                slidingSubmenus: true,

                navbar 		: {
                    title		: '网站导航'
                },
                navbars		: [
                    {

                        position	: 'top',
                        content		: [
                            'prev',
                            'title',
                            'close'
                        ]
                    }
                ]
            });

        }else{
            $("#hader-title").remove();
            $("nav#widget-menu").remove();
            $(".widget-menuwrap").append(str);
        }
    }

</script>
</div><div class="skin_01 eapblock " id="block3" style="position: absolute; top: 15px; right: 65px; z-index:999;"><style>
/*内容样式片段*/
.wrap_435 .widget-body{
	
}
</style>

<div class="wrap_435">
	<div class="widget-wrap">
	    <style>
.inputBox {
  width: 50px;
  height: 50px;
  position: relative; z-index: 999;
}
.inputBox .search {
  position: absolute;
  margin: auto; 
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 50px; text-align: center; color: #fff; line-height: 50px; font-size: 16px;
  background: #517bd6;
  border-radius: 50%;
  transition: all 1s;
  z-index: 4;
  box-shadow: 0 0 25px 0 rgba(0, 0, 0, 0.1);
}
.inputBox .search:hover {
  cursor: pointer;
}
.inputBox .search::before {
  content: url(/website/img/searchIcon.png);
}
.inputBox input {
  position: absolute;
  margin: auto;
  top: 0;
  right: 0;
  bottom: 0;
  /* left: 0; */
  width: 40px;
  height: 40px;
  outline: none;
  border: none;
  background: #fff;
  color: #777;
  border-radius: 30px;
  box-shadow: 0 0 25px 0 #517bd6, 0 0px 15px 0 rgba(0, 0, 0, 0.5);
  transition: all 1s;
  opacity: 0;
  z-index: 5;
  font-weight: bolder;
}
.inputBox input:hover {
  cursor: pointer;
}
.inputBox input:focus {
  width: 300px;
  padding: 0 80px 0 20px;
  opacity: 1;
  cursor: text;
}
.inputBox input:focus ~ .search {
  right: 0px;
  background: #f60;
  z-index: 6;
}
.inputBox input:focus ~ .search::before {
  content: "搜索"; 
}
.inputBox input::placeholder {
  color: #777;
  opacity: 0.8;
}
</style>
<div class="inputBox">
    <input type="text" name="keywords" id="keywords" autocomplete="off" placeholder="查询药物试验 如输入糖尿病" />
    <div class="search" id="goSearch"></div>
</div>
<script>
  $(function(){
    $("#goSearch").click(function(){
      window.location.href = encodeURI("/clinicaltrials.searchlist.dhtml?keywords="+$("#keywords").val());
    })
  })
</script>
	</div>
</div></div><div class="skin_01 eapblock " id="block4" style="position: absolute; top: 15px; right: 0px; z-index:999;"><style>
/*内容样式片段*/
.wrap_465 .widget-body{
	
}
</style>

<div class="wrap_465">
	<div class="widget-wrap">
	    <script>
    function getCookie(name) {
        var cookies = document.cookie.split(";");
        for(var i=0;i&lt;cookies.length;i++) {
            var cookie = cookies[i];
            var cookieStr = cookie.split("=");
            if(cookieStr &amp;&amp; cookieStr[0].trim()==name) {
                return  decodeURI(cookieStr[1]);
            }
        }
    }
    $(function () {
        if(getCookie("eap_username")!=undefined&amp;&amp;getCookie("eap_username")!=""){
           $.ajax({
		type: "get",
		url: "/clinicaltrials.getuserinfo.phtml",
		success: function(data){
			var jdata=jQuery.parseJSON(data);
			$("#topuser_name").html(jdata.user_name);
			$("#topname").html(jdata.name);
			$(".userinfo").css("display","block");
			$("#inBtn").css("display","none");
		}, error: function (xhr, textStatus, errorThrown) {
			if(xhr.status==401){
				$(".userinfo").css("display","none");
				$("#inBtn").css("display","block");
			}else{
				$("#topuser_name").html("获取失败");
				$("#topname").html("获取失败");
				$(".userinfo").css("display","block");
				$("#inBtn").css("display","none");
			}
		}
	   });
           
        }else{
            console.log(2);
            $(".userinfo").css("display","none");
            $("#inBtn").css("display","block");
        }
        $("#inBtn").click(function(){
            window.location.href="/common.login.dhtml"
        })
        $("#dologout").click(function(){
               $.post("/common.login.logout.dhtml",
               "",
               function(data, textStatus){
                   $(".userinfo").css("display","none");
                   $("#inBtn").css("display","block");
                   localStorage.clear();
                   window.location.reload();
               });
        });
    })
</script>
<style>
    .inOutBtn{
        width: 50px; height: 50px; border-radius: 25px; background-color: #517bd6;
        text-align: center; cursor: pointer; 
        box-shadow: 0 0 25px 0 rgba(0, 0, 0, 0.1);
	line-height:50px;
	color:#fff
    }
    .inOutBtn img{
        display: block;
    }
    .userinfo{
        display: none;
    }
    .userinfo .dropdown-menu {
    min-width: 170px; margin-right: -60px; top: 95%;
    color: #fff;
    border-radius: 0;
    border: 0;
    text-align: center;
    padding: 0;
    background-color: #1991ec;
  }

  .userinfo .dropdown-menu li {
    line-height: 18px !important; padding: 12px;
    border-bottom: 1px #3aa6f8 solid;
  }

  .userinfo .dropdown-menu li:nth-of-type(odd) {
    background-color: #0e86e1;
  }

  .userinfo .dropdown-menu li a {
    color: #fff;
    padding: 0 !important;
  }

  .userinfo .dropdown-menu li a:hover {
    color: #fff;
    background-color: transparent;
  }
  .userinfo:hover .dropdown-menu {display: block;}
</style>
 <div class="inOutBtn" id="inBtn" style="display: block;">
    
    登录
</div>

<div class="dropdown pull-right userinfo" style="display: none;">
    <a id="dLabel" role="button" aria-expanded="false" aria-haspopup="true" data-toggle="dropdown" data-target="#">
      <div class="inOutBtn"><img src="/website/img/login.png" alt="" /></div>
    </a>
    <ul class="dropdown-menu" aria-labelledby="dLabel">
      <li>当前账号：<span id="topuser_name"></span></li>
      <li id="topname"></li>
      <li style="background-color: #e9a23e; border-bottom:0;"><a id="dologout" href="javascript:void(0)"><i class="fa fa-sign-out"></i> 退 出 </a></li>
    </ul>
</div> 
	</div>
</div></div></div>
			</div>
		</div></header> 
    <main style="padding-top:15px;" class="">
	<div class="row clearfix">
			<div class="container">
				<div class="col-md-12 column"></div>
			</div>
		</div><div class="row " style="">
            <div class="container" style="background-color: #fff; ">
                <div class="column col-md-12" style="">
                    <div class="_main_content  skin_01" style=""><div class="_main_content null skin_01" style=""><link rel="alternate" type="application/rss+xml" href="/clinicaltrials.searchdetail.rss.dhtml?ckm_id=09cbc4282bcd4057be8ff9ccdf9a52e0" title="RSS" />
<link href="/resource/component/clinicaltrials/css/lcsy.css" rel="stylesheet" media="screen" />
<link href="/resource/component/clinicaltrials/css/print.css" rel="stylesheet" media="print" />
<script>
$(function(){
    if($(document).scrollTop()&gt;=85){
      $(".goTop").show();
    }else{
      $(".goTop").hide();
    }
    $(window).scroll(function(){
      if($(document).scrollTop()&gt;=85){
        $(".goTop").show();
      }else{
        $(".goTop").hide();
      }
    });
    $(".goTop").click(function () {
      $("html, body").animate({
        "scroll-top":0
      },"slow");
	});
});
//临床试验列表展开或关闭
function open_close(id){
var div = "#div_open_close_" + id;
var input = "#" + id;
var open_or_close = $(input).attr("class");
//如果要检索的字符串值没有出现，则该方法返回 -1
if(open_or_close.indexOf("down_icon") == -1){
//没找到则是关闭状态,需要进行开启
$(div).css("display","block");
$(input).attr("class","down_icon2");
}else{
//找到则是展开状态,需要进行关闭
$(div).css("display","none");
$(input).attr("class","up_icon2");
}
}
//打印
function doPrint(){
window.print();
}
function printit(){ 
if (confirm('确定打印吗？')){
var headhtml = "&lt;html&gt;" +
"			&lt;head&gt;" +
"				&lt;title&gt;&lt;/title&gt;" +
"	    		&lt;style&gt;" +
"		    		 .tabled , .tabled th , .tabled td{ border:1px solid;border-collapse: collapse; }" +
"		    	&lt;/style&gt;" +
"			&lt;/head&gt;" +
"		&lt;body&gt;";
var foothtml = "&lt;/body&gt;";
var newhtml = document.all.item('打印主题id').innerHTML;
var oldhtml = document.body.innerHTML;
document.body.innerHTML = headhtml + newhtml + foothtml;
// 调用window.print方法打印新窗口
$("#newsContent").show();
window.print();
// 将原来窗口body的html值回填展示
document.body.innerHTML = oldhtml;
return false;
}
if(getExplorer() == "IE"){
pagesetup_null();
}
}
function logdetail(id){
	$("#log_id").val(id)
	$("#logform")[0].submit();
}

//上/下/第一/最后一个试验
function gotopage(currentpage){
	document.getElementById("currentpage").value = currentpage;
	document.getElementById("searchform").submit();
}
</script>

<div class="onlyPrintVisible">
	药物临床试验登记与信息公示平台
</div>
<div class="btnNav marginBtm0">
    <div class="container btnNavCon clearfix">
        <div class="currentPlace">
            <a href="/index.html">首页</a> &gt; <a href="/clinicaltrials.prosearch.dhtml">试验公示和查询</a> &gt; <a href="/clinicaltrials.searchlist.dhtml">公示列表</a> &gt;详细信息
        </div>
    </div>
</div>


<form action="/clinicaltrials.updatehistorypublic.dhtml" method="post" target="_blank" id="logform" style="display: inline;">
<input type="hidden" name="id" id="log_id" value="" />
</form>								

<div class="padding15 printHidden">

	<div class="pull-right">
		<form action="/clinicaltrials.searchlistdetail.dhtml?_export=doc" method="post" style="display: inline;">
			<input type="hidden" name="id" value="3ebce5b6a4d84f2f9570906cdac4f7ff" />
			<button type="submit" class="btn btn-sm btn-info download"><span class="fa fa-download"></span> 下载</button>
			</form>
			<button type="button" class="btn btn-sm btn-info" onclick="window.location='/clinicaltrials.searchdetail.rss.dhtml?id=3ebce5b6a4d84f2f9570906cdac4f7ff'"><span class="fa fa-feed"></span> 订阅RSS</button>
			<button type="button" class="btn btn-sm btn-info" onclick="doPrint()"><span class="fa fa-print"></span> 打印</button>
	</div>

	查询条件：  
	<span style="color: #f00;">
		无
	</span>
	
</div>

<div id="toolbar_top" class="paddingSide15">

<style>
.f00{
	color:#F00
}
.radius_100{
	border-radius: 100px;
}

</style>
<div class="row" style="border-top: 1px #dedede solid; text-align: center; padding: 40px 0; line-height: 32px; font-size: 16px;">



		   
		目前是第 
		<span class="f00">1</span> 个试验/共 
		<span class="f00">11341</span> 个试验
		   

			<a href="javascript:void(0)" class="btn btn-default radius_100" onclick="gotopage(2);">
				下一个试验
				 
				<span class="fa fa-angle-right"></span>
			</a>

	

</div>

	<form id="searchform" name="searchform" action="/clinicaltrials.searchlistdetail.dhtml" method="post">
		
	  	<input type="hidden" id="currentpage" name="currentpage" value="1" />
		
		<input type="hidden" id="sort" name="sort" value="desc" />
		
		<input type="hidden" id="sort2" name="sort2" value="desc" />
		<input type="hidden" id="rule" name="rule" value="CTR" />
	</form>
</div>


<div class="paddingSide15">
	<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
		
		<div class="panel panel-default">
			<div class="panel-heading" role="tab" id="headingOne">
				<h4 class="panel-title">
					<a role="button" data-toggle="collapse" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
						基本信息
					</a>
				</h4>
			</div>
			<div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
				<div class="panel-body">
					<table class="searchDetailTable">
						<tbody><tr>
							<th width="15%">登记号</th>
							<td width="35%">CTR20201763</td>
							<th width="15%">试验状态</th>
							<td width="35%">进行中</td>
						</tr>
						<tr>
							<th>申请人联系人</th>
							<td>张静</td>
							<th>首次公示信息日期</th>
							<td>
							2020-08-31
							</td>
						</tr>
						<tr>
							<th>申请人名称</th>
							<td colspan="3">
								湖南华纳大药厂股份有限公司
							</td>
						</tr>
					</tbody></table>
						
				</div>
			</div>
		</div>
		
		<div class="panel panel-default">
			<div class="panel-heading" role="tab" id="headingTwo">
				<h4 class="panel-title">
					<a class="collapsed" role="button" data-toggle="collapse" href="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
						公示的试验信息
					</a>
				</h4>
			</div>
			<div id="collapseTwo" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingTwo">
				<div class="panel-body">
						<div class="searchDetailPartTit" style="margin-top: 0;">一、题目和背景信息</div>
						<table class="searchDetailTable">
							<tbody><tr>
								<th>登记号</th>
								<td colspan="3">CTR20201763</td>
							</tr>
							<tr>
								<th>相关登记号</th>
								<td colspan="3"></td>
							</tr>
							<tr>
								<th>药物名称</th>
								<td colspan="3">
									吗替麦考酚酯胶囊
									 曾用名:
								</td>
							</tr>
							<tr>
								<th>药物类型</th>
								<td colspan="3">
								化学药物
								</td>
							</tr>
							<tr>
								<th>
									备案号
								</th>
								<td colspan="3">
									B202000189-01
								</td>
							</tr>
							<tr>
								<th>适应症</th>
								<td colspan="3">可用于预防同种肾移植病人的排斥反应，及治疗难治性排斥反异，可与环孢素和肾上腺皮质激素同时应用。</td>
							</tr>
							<tr>
								<th>试验专业题目</th>
								<td colspan="3">吗替麦考酚酯胶囊在健康人群单中心、随机、开放、双周期、自身交叉、单剂量空腹试验和单中心、随机、开放、三周期、半重复交叉、单剂量餐后试验</td>
							</tr>
							<tr>
								<th>试验通俗题目</th>
								<td colspan="3">吗替麦考酚酯胶囊人体生物等效性试验</td>
							</tr>
							<tr>
								<th width="15%">试验方案编号</th>
								<td width="35%">JY-BE-MMF-2019-01</td>
								<th width="15%">
									方案最新版本号
								</th>
								<td width="35%">
									1.1
								</td>
							</tr>
							<tr>
								<th>版本日期:</th>
								<td>2020-07-17</td>
								<th>方案是否为联合用药</th>
								<td>否 </td>
							</tr>
						</tbody></table>
						<div class="searchDetailPartTit">二、申请人信息</div>
						<table class="searchDetailTable">
							<tbody><tr>
								<th>申请人名称</th>
								<td colspan="5">
									<div class="input-group">
										<span class="input-group-addon">1</span>
										<input type="text" style="width: 500px;" class="form-control" readonly="" placeholder="" value="湖南华纳大药厂股份有限公司" />
									</div>
								</td>
							</tr>
							<tr>
								<th width="15%">联系人姓名</th>
								<td width="18%">张静</td>
								<th width="15%">联系人座机</th>
								<td width="18%">0731-85910585</td>
								<th width="15%">联系人手机号</th>
								<td width="19%">18613997826</td>
							</tr>
							<tr>
								<th>联系人Email</th>
								<td>zhangjing@warrant.com.cn</td>
								<th>联系人邮政地址</th>
								<td>湖南省-长沙市-高新区麓天路28号五矿麓谷科技园C7栋3楼</td>
								<th>联系人邮编</th>
								<td>410205</td>
							</tr>
						</tbody></table>	
						<div class="searchDetailPartTit">三、临床试验信息</div>
						<div class="sDPTit2">1、试验目的</div>
						分别采用单中心、随机、开放、双周期、自身交叉、单剂量给药设计评价空腹给药条件下和单中心、随机、开放、三周期、半重复交叉、单剂量给药设计评价餐后给药条件下，湖南华纳大药厂股份有限公司生产的吗替麦考酚酯胶囊（250 mg/粒）与上海罗氏制药有限公司生产的吗替麦考酚酯胶囊（250 mg/粒），商品名：骁悉®）在中国健康人群吸收程度和吸收速度的差异，并评价湖南华纳大药厂股份有限公司生产的吗替麦考酚酯胶囊的安全性。
						<div class="sDPTit2">2、试验设计</div>
						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%">试验分类</th>
								<td width="17%">
									生物等效性试验/生物利用度试验
								</td>
						
								<th width="15%">试验分期</th>
								<td width="17%">
									其它
										BE试验
								</td>
						
								<th width="15%">设计类型</th>
								<td width="17%">
									交叉设计
								</td>
							</tr>		
							<tr>
								<th>随机化</th>
								<td>
									随机化
								</td>
						
								<th>盲法</th>
								<td>
									开放
								</td>
					
								<th>试验范围</th>
								<td>
									国内试验
								</td>
							</tr>
						</tbody></table>
						<div class="sDPTit2">3、受试者信息</div>
						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%">年龄</th>
								<td width="85%">
										18岁(最小年龄)至
										60岁(最大年龄)
								</td>
							</tr>
							<tr>
								<th width="15%">性别</th>
								<td width="35%">
										男
								</td>
							</tr>
							<tr>
								<th>健康受试者</th>
								<td colspan="3">
									有
								</td>
							</tr>
							<tr>
								<th>入选标准</th>
								<td colspan="3">
									<table class="subSearch">
										<tbody><tr>
											<td width="10%">
											1
											</td>
											<td width="90%" style="text-align: left;">
											年龄在18周岁至60周岁（含边界值）的中国健康志愿者，男性
											</td>
										</tr>
										<tr>
											<td width="10%">
											2
											</td>
											<td width="90%" style="text-align: left;">
											体重不小于50 kg；体重指数在19~26 kg/m2范围内（包括临界值）
											</td>
										</tr>
										<tr>
											<td width="10%">
											3
											</td>
											<td width="90%" style="text-align: left;">
											试验前签署知情同意书、并对试验内容、过程及可能出现的不良反应充分了解
											</td>
										</tr>
										<tr>
											<td width="10%">
											4
											</td>
											<td width="90%" style="text-align: left;">
											志愿者能够和研究者进行良好的沟通，并且理解和遵守本项研究的各项要求
											</td>
										</tr>
									</tbody></table>
								</td>
							</tr>
							<tr>
								<th>排除标准</th>
								<td colspan="3">
										<table class="subSearch">
										<tbody><tr>
										<td width="10%">
										1
										</td>
										<td width="90%" style="text-align: left;">
										试验前3个月内参加过其他任何临床试验者
										</td>
										</tr>
										<tr>
										<td width="10%">
										2
										</td>
										<td width="90%" style="text-align: left;">
										对吗替麦考酚酯、麦考酚酸或药物中的其他成分有超敏反应者
										</td>
										</tr>
										<tr>
										<td width="10%">
										3
										</td>
										<td width="90%" style="text-align: left;">
										三年内有慢性或活动性消化道疾病如食管疾病、胃炎、胃溃疡、憩室炎、肠炎，活动性胃肠道出血、胃肠道穿孔或消化道手术者
										</td>
										</tr>
										<tr>
										<td width="10%">
										4
										</td>
										<td width="90%" style="text-align: left;">
										有心血管系统、内分泌系统、神经系统、血液系统、免疫系统（包括个人或家族史遗传性免疫缺陷）、精神病、代谢异常、恶性肿瘤、淋巴组织增生性疾病等病史且研究者认为目前仍有临床意义者
										</td>
										</tr>
										<tr>
										<td width="10%">
										5
										</td>
										<td width="90%" style="text-align: left;">
										有体位性低血压、晕针或晕血病史或静脉穿刺采血不耐受者
										</td>
										</tr>
										<tr>
										<td width="10%">
										6
										</td>
										<td width="90%" style="text-align: left;">
										试验前3个月内接种过，或试验中、试验后3个月内计划接种疫苗者
										</td>
										</tr>
										<tr>
										<td width="10%">
										7
										</td>
										<td width="90%" style="text-align: left;">
										密切接触人群患有传播性的细菌、病毒感染（包括水痘病毒、流感病毒）者
										</td>
										</tr>
										<tr>
										<td width="10%">
										8
										</td>
										<td width="90%" style="text-align: left;">
										试验前6个月内接受过经研究者判断会影响药物吸收、分布、代谢、排泄的手术者；或试验前4周内接受过外科手术；或计划在研究期间进行外科手术者
										</td>
										</tr>
										<tr>
										<td width="10%">
										9
										</td>
										<td width="90%" style="text-align: left;">
										试验前14天内因各种原因使用过任何药物（包括中草药）者
										</td>
										</tr>
										<tr>
										<td width="10%">
										10
										</td>
										<td width="90%" style="text-align: left;">
										试验前30天内使用过任何抑制或诱导肝脏对药物代谢的药物者
										</td>
										</tr>
										<tr>
										<td width="10%">
										11
										</td>
										<td width="90%" style="text-align: left;">
										试验前3个月内献血者或大量失血（＞200 mL）或试验期间/试验结束后3个月内有献血计划者
										</td>
										</tr>
										<tr>
										<td width="10%">
										12
										</td>
										<td width="90%" style="text-align: left;">
										药物滥用者或试验前3个月使用过软毒品（如：大麻）或试验前1年服用硬毒品（如：甲基安非他明、苯环己哌啶等）者
										</td>
										</tr>
										<tr>
										<td width="10%">
										13
										</td>
										<td width="90%" style="text-align: left;">
										嗜烟者或试验3个月内每日吸烟量多于5支者，或试验期间不能停止使用任何烟草类产品
										</td>
										</tr>
										<tr>
										<td width="10%">
										14
										</td>
										<td width="90%" style="text-align: left;">
										酗酒者或试验前6个月内经常饮酒者，即每周饮酒超过14单位酒精（1单位=360 mL啤酒或45 mL酒精量为40%的烈酒或150 mL葡萄酒）；或试验期间不愿意停止饮酒或任何含酒精的制品
										</td>
										</tr>
										<tr>
										<td width="10%">
										15
										</td>
										<td width="90%" style="text-align: left;">
										每天饮用过量茶、咖啡和/或含咖啡因的饮料（8杯以上，1杯=250 mL）者，或不同意试验期间停止饮用茶、咖啡和/或含咖啡因的饮料者
										</td>
										</tr>
										<tr>
										<td width="10%">
										16
										</td>
										<td width="90%" style="text-align: left;">
										对饮食有特殊要求，不能遵守统一饮食者；或乳糖不耐受者
										</td>
										</tr>
										<tr>
										<td width="10%">
										17
										</td>
										<td width="90%" style="text-align: left;">
										试验期间或试验结束后3个月内有捐精计划，或试验期间不愿采取一种或一种以上的非药物避孕措施（如完全禁欲、伴侣结扎等）者
										</td>
										</tr>
										<tr>
										<td width="10%">
										18
										</td>
										<td width="90%" style="text-align: left;">
										在服用研究药物前3天内进食可能影响药物体内代谢的饮食（包括葡萄柚或葡萄柚产品、火龙果、芒果、柚子、橘子等），或研究者认为有其他影响药物吸收、分布、代谢、排泄的饮食者
										</td>
										</tr>
										<tr>
										<td width="10%">
										19
										</td>
										<td width="90%" style="text-align: left;">
										试验前生命体征检查异常且有临床意义者，由研究者参考正常范围后综合判定
										</td>
										</tr>
										<tr>
										<td width="10%">
										20
										</td>
										<td width="90%" style="text-align: left;">
										试验前体格检查异常且有临床意义者
										</td>
										</tr>
										<tr>
										<td width="10%">
										21
										</td>
										<td width="90%" style="text-align: left;">
										试验前实验室检查异常且有临床意义者
										</td>
										</tr>
										<tr>
										<td width="10%">
										22
										</td>
										<td width="90%" style="text-align: left;">
										试验前心电图异常且有临床意义者
										</td>
										</tr>
										<tr>
										<td width="10%">
										23
										</td>
										<td width="90%" style="text-align: left;">
										试验前胸部X线（正侧位）检查结果异常且有临床意义者
										</td>
										</tr>
										<tr>
										<td width="10%">
										24
										</td>
										<td width="90%" style="text-align: left;">
										受试者可能因为其他原因而不能完成本研究或经研究者判断具有其它不宜参加试验原因者
										</td>
										</tr>
										</tbody></table>
								</td>
							</tr>
							
						</tbody></table>
						<div class="sDPTit2">4、试验分组</div>
						
						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%">试验药</th>
								<td width="85%">
									<table class="subSearch">
										<tbody><tr>
											<th width="10%">序号</th>
											<th width="40%">名称</th>
											<th width="50%">用法</th>
										</tr>
										<tr>
											<td>
											1
											</td>
											<td>
													中文通用名:吗替麦考酚酯胶囊<br />
													英文通用名:Mycophenolate mofetil capsules<br />
													商品名称:浦津
											</td>
											<td>
													 剂型:胶囊<br />
													 规格:250mg<br />
													 用法用量:单次给药1粒<br />
													 用药时程:每周期（7天）单次给药
											</td>
										</tr>
									</tbody></table>
								</td>
							</tr>
							<tr>
								<th width="15%">对照药</th>
								<td width="35%">
									<table class="subSearch">
										<tbody><tr>
											<th width="10%">序号</th>
											<th width="40%">名称</th>
											<th width="50%">用法</th>
										</tr>
										<tr>
											<td>1</td>
											<td>
													中文通用名:吗替麦考酚酯胶囊<br />
													英文通用名:Mycophenolate mofetil capsules<br />
													商品名称:骁悉
											</td>
											<td>
													 剂型:胶囊<br />
													 规格:250mg<br />
													 用法用量:单次给药1粒 <br />
													 用药时程:每周期（7天）单次给药
											</td>
										</tr>
									</tbody></table>
								</td>
							</tr>
						</tbody></table>
						
						<div class="sDPTit2">5、终点指标</div>
						
						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%">主要终点指标及评价时间</th>
								<td width="85%">
									<table class="subSearch">
										<tbody><tr>
											<th width="10%">序号</th>
											<th width="35%">指标</th>
											<th width="35%">评价时间</th>
											<th width="20%">终点指标选择</th>
										</tr>
										<tr>
											<td>1</td>
											<td>血浆药物峰浓度（Cmax）、药物浓度-时间曲线下面积(AUC)</td>
											<td>给药后48h</td>
											<td>
											有效性指标
																						</td>
										</tr>
									</tbody></table>
								</td>
							</tr>
							<tr>
								<th>次要终点指标及评价时间</th>
								<td>
										<table class="subSearch">
											<tbody><tr>
												<th width="10%">序号</th>
												<th width="35%">指标</th>
												<th width="35%">评价时间</th>
												<th width="20%">终点指标选择</th>
											</tr>
											<tr>
											<td>1</td>
											<td>达峰时间(Tmax)；
安全性评价：生命体征（血压、脉搏、体温）、体格检查、实验室检查和不良事件
</td>
											<td>整个试验过程</td>
											<td>
												有效性指标+安全性指标
																							</td>
											</tr>
										</tbody></table>
								</td>
							</tr>
						</tbody></table>
						
						<div class="sDPTit2">
							6、数据安全监查委员会（DMC）
						</div>
								无
						<div class="sDPTit2">
							7、为受试者购买试验伤害保险
						</div>	
							
							有

						<div class="searchDetailPartTit">四、研究者信息</div>

						<div class="sDPTit2">1、主要研究者信息</div>
						<table class="searchDetailTable marginBtm10">
							
							<tbody><tr>
								<th width="5%" rowspan="3" style="text-align: center;">1</th>
								<th width="10%">姓名</th>
								<td width="18%">张毕奎</td>
								<th width="15%">学位</th>
								<td width="18%">药理学博士</td>
								<th width="15%">职称</th>
								<td width="19%">主任药师</td>
							</tr>
							<tr>
								<th>电话</th>
								<td>0731-85292098</td>
								<th>Email</th>
								<td>bikui_zh@vip.126.com</td>
								<th>邮政地址</th>
								<td>湖南省-长沙市-万家丽北路61号</td>
							</tr>
							<tr>
								<th>邮编</th>
								<td>410100</td>
								<th>单位名称</th>
								<td colspan="3">湘雅博爱康复医院</td>
							</tr>
							
						</tbody></table>
						
						<div class="sDPTit2">2、各参加机构信息</div>

						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%" class="text-center">序号</th>
								<th width="16%" class="text-center">机构名称</th>
								<th width="16%" class="text-center">主要研究者</th>
								<th width="16%" class="text-center">国家</th>
								<th width="16%" class="text-center">省（州）</th>
								<th width="20%" class="text-center">城市</th>
							</tr>
							<tr>
								<td class="text-center">1</td>
								<td class="text-center">湘雅博爱康复医院</td>
								<td class="text-center">张毕奎</td>
								<td class="text-center">中国</td>
								<td class="text-center">湖南省</td>
								<td class="text-center">长沙市</td>
							</tr>
						</tbody></table>
					
						<div class="searchDetailPartTit">五、伦理委员会信息</div>
						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%" style="text-align: center;">序号</th>
								<th width="30%" style="text-align: center;">名称</th>
								<th width="30%" style="text-align: center;">审查结论</th>
								<th width="25%" style="text-align: center;">批准日期/备案日期</th>
							</tr>
							<tr>
								<td style="text-align: center;">1</td>
								<td style="text-align: center;">湘雅博爱康复医院伦理委员会</td>
								<td style="text-align: center;">
										同意
										
										 
								</td>
								<td style="text-align: center;">2020-01-13</td>
							</tr>
						</tbody></table>
						<div class="searchDetailPartTit">六、试验状态信息</div>
						<div class="sDPTit2">1、试验状态</div>
						进行中
						（尚未招募）
			          							<div class="sDPTit2">2、试验人数</div>
						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%">目标入组人数</th>
								<td width="85%">
						        		
						        			国内: 48 人；
								</td>
							</tr>
							<tr>
								<th width="15%">已入组人数</th>
								<td width="85%">
										国内: 登记人暂未填写该信息；
								</td>
							</tr>
							<tr>
								<th>实际入组总人数</th>
								<td>
										国内: 登记人暂未填写该信息；
								</td>
							</tr>
						</tbody></table>
						<div class="sDPTit2">3、受试者招募及试验完成日期</div>
						<table class="searchDetailTable">
							<tbody><tr>
								<th width="15%">第一例受试者签署知情同意书日期</th>
								<td width="85%">
										国内：登记人暂未填写该信息；    
								</td>
							</tr>
							<tr>
								<th>第一例受试者入组日期</th>
								<td>
										国内：登记人暂未填写该信息；    
								</td>
							</tr>
							<tr>
								<th>
				       					试验完成日期
						        </th>
								<td>
										国内：登记人暂未填写该信息；    
								</td>
							</tr>
						</tbody></table>
						<div class="searchDetailPartTit">七、临床试验结果摘要</div>
						<table class="searchDetailTable">
						<tbody><tr>
							<th width="15%" class="text-center">序号</th>
							<th width="45%" class="text-center">版本号</th>
							<th width="40%" class="text-center">版本日期</th>
						</tr>
							<tr><td colspan="3" style="text-align: center">暂未填写此信息</td></tr>
					</tbody></table>
				</div>
			</div>
		</div>

		<div class="panel panel-default">
			<div class="panel-heading" role="tab" id="headingThree">
				<h4 class="panel-title">
					<a class="collapsed" role="button" data-toggle="collapse" href="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
						信息更新记录
					</a>
				</h4>
			</div>
			<div id="collapseThree" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingThree">
				<div class="panel-body">
					<table class="searchDetailTable">
						<tbody><tr>
							<th width="40%" style="text-align: center;">时间</th>
							<th width="60%" style="text-align: center;">更新记录</th>
						</tr>
						<tr>
							<td colspan="2" style="text-align: center;">暂无更新记录</td>
						</tr>
					</tbody></table>
				</div>
			</div>
		</div>

	</div>

</div>

<div class="padding15 text-right printHidden">
	<form action="/clinicaltrials.searchlistdetail.dhtml?_export=doc" method="post" style="display: inline;">
		<input type="hidden" name="id" value="3ebce5b6a4d84f2f9570906cdac4f7ff" />
		<button type="submit" class="btn btn-sm btn-info download"><span class="fa fa-download"></span> 下载</button>
	</form>
		<button type="button" class="btn btn-sm btn-info" onclick="window.location='/clinicaltrials.searchdetail.rss.dhtml?id=3ebce5b6a4d84f2f9570906cdac4f7ff'"><span class="fa fa-feed"></span> 订阅RSS</button>
		<button type="button" class="btn btn-sm btn-info" onclick="doPrint()"><span class="fa fa-print"></span> 打印</button>
</div>

<div class="goTop printHidden" style="display: none;">
	<div class="upIcon"><span class="fa fa-angle-up"></span></div>
	TOP
</div>
<div id="toolbar_bottom" class="paddingSide15">

<style>
.f00{
	color:#F00
}
.radius_100{
	border-radius: 100px;
}

</style>
<div class="row" style="border-top: 1px #dedede solid; text-align: center; padding: 40px 0; line-height: 32px; font-size: 16px;">



		   
		目前是第 
		<span class="f00">1</span> 个试验/共 
		<span class="f00">11341</span> 个试验
		   

			<a href="javascript:void(0)" class="btn btn-default radius_100" onclick="gotopage(2);">
				下一个试验
				 
				<span class="fa fa-angle-right"></span>
			</a>

	

</div>
</div>
</div></div></div>
            </div>
        </div></main>
    <footer class="" style=""> 
    <div class="row " style="margin-top:15px;"> 
        <div class="container" style="box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);"> 
          <div class="column col-md-12" style="">
<div class="skin_01 eapblock " id="block5" style=""><style>
/*内容样式片段*/
.wrap_427 .widget-body{
	
}
</style>

<div class="wrap_427">
	<div class="widget-wrap">
	    <style>
    html,body{height: auto;}
    ._main_content{padding:0!important}
    .copyRight{background-color: #3f69c4; position: relative;
    padding: 20px; line-height: 32px; text-align: center; color: #fff;}  
    .qrCode{
        position: absolute; right: 50px; top: 25px; line-height: 25px;
    }
</style>
<div class="copyRight">
Copyright © 国家药品监督管理局药品审评中心 All Right Reserved.
<br />
地址： 中国 北京市朝阳区建国路128号 邮编：100022
<br />
总机：8610-68585566 传真：8610-68584189 备案序号：京ICP备09013725号-2
<div class="qrCode">
    <img src="/website/img/qrCode.jpg" alt="" />
    <br />
    手机版
</div>

</div>
	</div>
</div></div>          </div> 
        </div> 
      </div></footer> 
<script type="text/javascript" src="/resource/js/jquery.ui.touch-punch.min.js"></script>
<script type="text/javascript" src="/resource/js/layer/layer.js"></script>
<script type="text/javascript" src="/resource/js/layer/extend/layer.ext.js"></script>
<!--[if lte IE 8]>
<script type="text/javascript" src="/resource/js/respond.min.js"></script>
<![endif]--><script type="text/javascript" src="/resource/js/bootstrap.min.js"></script>
</body></html>'''

# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options,
                          executable_path="D:\\PyCharm2019.3.1\\pystudy\\chromedriver.exe")

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})

url = "http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml"
url='http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml'
driver.get(url)
html=driver.page_source
html=my_html_tools.qu_kong_ge(html)

登记号=re.findall(r'''<th.*?>登记号</th><td.*?>(.*?)</td>''',html,re.S)
相关登记号=re.findall(r'''<th.*?>相关登记号</th><td.*?>(.*?)</td>''',html,re.S)
药物名称=re.findall(r'''<th.*?>药物名称</th><td.*?>(.*?)</td>''',html,re.S)
药物类型=re.findall(r'''<th.*?>药物类型</th><td.*?>(.*?)</td>''',html,re.S)
备案号=re.findall(r'''<th.*?>备案号</th><td.*?>(.*?)</td>''',html,re.S)
适应症=re.findall(r'''<th.*?>适应症</th><td.*?>(.*?)</td>''',html,re.S)
试验专业题目=re.findall(r'''<th.*?>试验专业题目</th><td.*?>(.*?)</td>''',html,re.S)
试验通俗题目=re.findall(r'''<th.*?>试验通俗题目</th><td.*?>(.*?)</td>''',html,re.S)
试验方案编号=re.findall(r'''<th.*?>试验方案编号.*?</th><td.*?>(.*?)</td>''',html,re.S)
方案最新版本号=re.findall(r'''<th.*?>方案最新版本号</th><td.*?>(.*?)</td>''',html,re.S)
版本日期=re.findall(r'''<th.*?>版本日期.*?</th><td.*?>(.*?)</td>''',html,re.S)#<th>版本日期:</th><td>2020-07-17</td>
方案是否为联合用药=re.findall(r'''<th.*?>方案是否为联合用药.*?</th><td.*?>(.*?)</td>''',html,re.S)


print(登记号,相关登记号,药物名称,药物类型,备案号,适应症,试验专业题目,试验通俗题目,试验方案编号,方案最新版本号,版本日期,方案是否为联合用药)









#
# id_value = driver.find_element_by_xpath('//a[@id="7e9a398a0e52469983e1c68daf937ace"]')
# print(id_value.text)
#
# list_value = driver.find_elements_by_xpath('//a[@onclick="getDetail(this.id)"]')
# for i in list_value:
#     print("序号：%s   值：%s" % (list_value.index(i) + 1, i.text))



