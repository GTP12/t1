$(function(){
    $('.cbt').inputbox();
    //查看详情
    $(".ordetail").click(function(){
        if($(this).hasClass("up")){
            $(".waitpay-bot").slideUp();
            $(this).removeClass("up");
        }else{
            $(".waitpay-bot").slideDown();
            $(this).addClass("up");
        }
    });
    //选择红包
    $(".chredpack").find("li").click(function(){
        $(this).addClass("on").siblings("li").removeClass("on");
    });
    //选择第三方平台充值平台 支付宝 微信 易宝
    $(".allplat").find("li").click(function(){

        needpay = sub(orderPrice,haspay);

        var payway = $(this).attr("data-value");
        var payname = $(this).attr("data-name");
        $("#payway").val(payway);
        $("#fptname").val(payname);

        var srcurl = $(this).find("img").attr("src");
        $(".onlinepay").find(".nopt").hide();
        $(".onlinepay").find(".haspt").show();
        $(".onlinepay").find(".haspt").find("img").attr("src",srcurl);
        $(".onlinepay").find(".haspt").find(".payname").text(payname);

        feemoney = getReduce(payway,needpay);

        $(".onlinepay").find(".haspt").find(".feemoney").text(feemoney);

        if(feemoney == 0){
            $(".onlinepay").find(".haspt").find(".serfee").hide();
        }else {
            $(".onlinepay").find(".haspt").find(".serfee").show();
        }

        $(".onlinepay").find(".needpay").text(cutXiaoNum(add(needpay,feemoney) ,2));

        allprice = cutXiaoNum(add(orderPrice,feemoney) ,2);
        $(".allprice").text(allprice);

        $(".allbank").find(".on").removeClass("on");
        $(this).addClass("on").siblings("li").removeClass("on");

    });
    //选择银行
    $(".allbank").find("li").click(function(){

        var payway = $(this).attr("data-value");
        var payname = $(this).attr("data-name");
        $("#payway").val(payway);
        $("#fptname").val(payname);

        var srcurl = $(this).find("img").attr("src");
        $(".onlinepay").find(".nopt").hide();
        $(".onlinepay").find(".haspt").show();
        $(".onlinepay").find(".haspt").find("img").attr("src",srcurl);
        $(".onlinepay").find(".haspt").find(".payname").text(payname);

        feemoney = getReduce(payway,needpay);
        $(".onlinepay").find(".haspt").find(".feemoney").text(feemoney);

        if(feemoney == 0){
            $(".onlinepay").find(".haspt").find(".serfee").hide();
        }else {
            $(".onlinepay").find(".haspt").find(".serfee").show();
        }

        $(".onlinepay").find(".needpay").text(cutXiaoNum(add(needpay,feemoney) ,2));

        allprice = cutXiaoNum(add(orderPrice,feemoney) ,2);
        $(".allprice").text(allprice);

        $(".allplat").find(".on").removeClass("on");
        $(".allbank").find(".on").removeClass("on");
        $(this).addClass("on").siblings("li").removeClass("on");
    });
    //选择余额
    $(".balance").find(".checkbox").click(function(){
        $(".allprice").text(orderPrice);

        if($(this).hasClass("checkbox_active")){

            $(this).parent().find(".maypay").show();
            if(balance >= orderPrice){
                $(".onlinepay").find(".checkbox").removeClass("checkbox_active");
                $(".onlinepay").find(".btline").hide();
                $(".onlinecon ").removeClass("boxshadow");
                $(".onlinepay").removeClass("noborder");
                $(".onlinepay").find(".needpay").text('0');
            }
            if(balance > orderPrice){
                $(this).parent().find(".balause").text(orderPrice);
            }else{
                $(this).parent().find(".balause").text(cutXiaoNum(balance,2));
            }
            $(this).parent().addClass("boxshadow");

            if($(".onlinepay").find(".checkbox").hasClass("checkbox_active")){
                haspay = cutXiaoNum(balance,2);
                needpay = sub(orderPrice,haspay);


                var payway = $(".thirdpart").find(".on").attr("data-value");
                var payname = $(".thirdpart").find(".on").attr("data-name");
                $("#payway").val(payway);
                $("#fptname").val(payname);

                var srcurl = $(".thirdpart").find(".on").find("img").attr("src");
                $(".onlinepay").find(".nopt").hide();
                $(".onlinepay").find(".haspt").show();
                $(".onlinepay").find(".haspt").find("img").attr("src",srcurl);
                $(".onlinepay").find(".haspt").find(".payname").text(payname);

                feemoney = getReduce(payway,needpay);
                $(".onlinepay").find(".haspt").find(".feemoney").text(feemoney);

                if(feemoney == 0){
                    $(".onlinepay").find(".haspt").find(".serfee").hide();
                }else {
                    $(".onlinepay").find(".haspt").find(".serfee").show();
                }

                $(".onlinepay").find(".needpay").text(cutXiaoNum(add(needpay,feemoney) ,2));

                allprice = cutXiaoNum(add(orderPrice,feemoney) ,2);
                $(".allprice").text(allprice);

            }else{
                $(".onlinepay").find(".nopt").show();
                $(".onlinepay").find(".haspt").hide();
            }
        }else{
            $(this).parent().find(".maypay").hide();
            $(this).parent().removeClass("boxshadow");
            if($(".onlinepay").find(".checkbox").hasClass("checkbox_active")){
                needpay = orderPrice;

                var payway = $(".thirdpart").find(".on").attr("data-value");
                var payname = $(".thirdpart").find(".on").attr("data-name");
                $("#payway").val(payway);
                $("#fptname").val(payname);

                var srcurl = $(".thirdpart").find(".on").find("img").attr("src");
                $(".onlinepay").find(".nopt").hide();
                $(".onlinepay").find(".haspt").show();
                $(".onlinepay").find(".haspt").find("img").attr("src",srcurl);
                $(".onlinepay").find(".haspt").find(".payname").text(payname);

                feemoney = getReduce(payway,needpay);
                $(".onlinepay").find(".haspt").find(".feemoney").text(feemoney);

                if(feemoney == 0){
                    $(".onlinepay").find(".haspt").find(".serfee").hide();
                }else {
                    $(".onlinepay").find(".haspt").find(".serfee").show();
                }

                $(".onlinepay").find(".needpay").text(cutXiaoNum(add(needpay,feemoney) ,2));

                allprice = cutXiaoNum(add(orderPrice,feemoney) ,2);
                $(".allprice").text(allprice);
            }
            $(this).parent().find(".balause").text('0');

        }
        haspay = parseFloat($(".balance").find(".balause").text());
    });
    //选择在线支付
    $(".onlinepay").find(".checkbox").click(function(){

        if($(this).hasClass("checkbox_active")){
            $(this).parent().find(".btline").show();
            $(this).parent().addClass("noborder");
            $(this).parents(".onlinecon").addClass("boxshadow");

            if($(".balance").find(".checkbox").hasClass("checkbox_active")){
                if(balance >= orderPrice){
                    haspay = 0;
                    needpay = orderPrice;

                    $(".balance").find(".maypay").hide();
                    $(".balance").find(".checkbox").removeClass("checkbox_active");
                    $(".balance").removeClass("boxshadow");
                    $(".balance").find(".balause").text('0');
                }else{
                    haspay = parseFloat($(".balance").find(".balause").text());
                    needpay = sub(orderPrice,haspay);

                }
            }else{
                needpay = orderPrice;

            }

            if(payTypeName != "" && $("li[data-name='"+payTypeName+"']").length == 1){
                $("li[data-name='"+payTypeName+"']").addClass("on").siblings("li").removeClass("on");
            }else{
                $(".allplat").find("li").first().addClass("on").siblings("li").removeClass("on");
            }

            var payway = $(".thirdpart").find(".on").attr("data-value");
            var payname = $(".thirdpart").find(".on").attr("data-name");
            $("#payway").val(payway);
            $("#fptname").val(payname);

            var srcurl = $(".thirdpart").find(".on").find("img").attr("src");
            $(".onlinepay").find(".nopt").hide();
            $(".onlinepay").find(".haspt").show();
            $(".onlinepay").find(".haspt").find("img").attr("src",srcurl);
            $(".onlinepay").find(".haspt").find(".payname").text(payname);

            feemoney = getReduce(payway,needpay);
            $(".onlinepay").find(".haspt").find(".feemoney").text(feemoney);

            if(feemoney == 0){
                $(".onlinepay").find(".haspt").find(".serfee").hide();
            }else {
                $(".onlinepay").find(".haspt").find(".serfee").show();
            }

            $(".onlinepay").find(".needpay").text(cutXiaoNum(add(needpay,feemoney) ,2));

            allprice = cutXiaoNum(add(orderPrice,feemoney) ,2);
            $(".allprice").text(allprice);
        }else{
            $(this).parent().find(".btline").hide();
            $(this).parents(".onlinecon").removeClass("boxshadow");
            $(this).parent().removeClass("noborder");
            $(this).parent().find(".needpay").text('0');
            $(".onlinepay").find(".nopt").show();
            $(".onlinepay").find(".haspt").hide();

            $(".allprice").text(orderPrice);
        }
        needpay = parseFloat($(".onlinecon").find(".needpay").text());
    });
});
//判断默认支付方式
function LoadPay(){
    if(balance <= 0){
        $(".balance").addClass("nochose");
        $(".onlinecon").addClass("boxshadow").find(".checkbox").addClass("checkbox_active");
        needpay = orderPrice;
        selectThirdPayShow();
    }else{
        $(".balance").addClass("boxshadow");
        $(".balance").find(".checkbox").addClass("checkbox_active");
        if(balance >= orderPrice){
            $(".balance").find(".balause").text(orderPrice);
            haspay = orderPrice;
        }else{
            needpay = sub(orderPrice,balance);
            $(".onlinecon").addClass("boxshadow");
            $(".onlinecon").find(".checkbox").addClass("checkbox_active");

            $(".balance").find(".balause").text(cutXiaoNum(balance,2));

            haspay = cutXiaoNum(balance,2);

            // $(".onlinepay").find(".needpay").text(cutXiaoNum(needpay,2));
            selectThirdPayShow();

        }
    }
}

function selectThirdPayShow(){
    if(payTypeName != "" && $("li[data-name='"+payTypeName+"']").length == 1){
        $("li[data-name='"+payTypeName+"']").addClass("on").siblings("li").removeClass("on");
    }else{
        $(".allplat").find("li").first().addClass("on").siblings("li").removeClass("on");
    }

    var payway = $(".thirdpart").find(".on").attr("data-value");
    var payname = $(".thirdpart").find(".on").attr("data-name");
    $("#payway").val(payway);
    $("#fptname").val(payname);

    var srcurl = $(".thirdpart").find(".on").find("img").attr("src");
    $(".onlinepay").find(".nopt").hide();
    $(".onlinepay").find(".haspt").show();
    $(".onlinepay").find(".haspt").find("img").attr("src",srcurl);
    $(".onlinepay").find(".haspt").find(".payname").text(payname);

    feemoney = getReduce(payway,needpay);
    $(".onlinepay").find(".haspt").find(".feemoney").text(feemoney);

    if(feemoney == 0){
        $(".onlinepay").find(".haspt").find(".serfee").hide();
    }else {
        $(".onlinepay").find(".haspt").find(".serfee").show();
    }

    $(".onlinepay").find(".needpay").text(cutXiaoNum(add(needpay,feemoney) ,2));

    allprice = cutXiaoNum(add(orderPrice,feemoney) ,2);
    $(".allprice").text(allprice);
}

//余额支付
function payBlan(){
    var html = $(".yueopen").html();
    layer.open({
        type: 1,
        title:'',
        skin:'pay-blan',
        closeBtn: 0,
        anim: 2,
        area:['300px','380px'],
        content: html,
        success:function(){
            $(".pay-blan").find(".closebtn").click(function(){
                layer.closeAll();
            });
            $(".pay-blan").find(".paypass .iptpwd span").click(function(){
                $(this).hide();
                $(this).parent().find("input").focus();
            });
            $(".pay-blan").find(".paypass input").blur(function(){
                if($(this).val()==""){
                    $(this).removeClass("error");
                    $(this).parent().find("span").show();
                    $(this).parent().find("em").hide();
                }
            });
            $(".pay-blan").find(".paypass input").focus(function(){
                $(this).removeClass("error");
                $(this).parent().find("span").hide();
                $(this).parent().find("em").hide();
            });
            $(".pay-blan").find(".paypass input").bind('input propertychange',function() {
                var pswd = $(this).val();
                if(pswd.length>=6){
                    $(this).parent().find("a").addClass("on");
                }else{
                    $(this).parent().find("a").removeClass("on");
                }
            });
            $(".pay-blan").find(".password a").click(function(){
                var pswd = $(this).parent().find("input").val();
                if($(this).hasClass("on")){
                    VadPwd(pswd,$(this));
                }
            });
            $(".pay-blan").find(".fgetpwd").click(function(){
                tosetPhone();
                $(".pay-blan").find(".password").hide();
                $(".pay-blan").find(".yzphone").show();
            });
            $(".pay-blan").find(".yzphone a").click(function(){
                var yzcode = $(this).parent().find("input").val();
                if($(this).hasClass("on")){
                    VadYzm(yzcode,$(this));
                }
            });
            $(".pay-blan").find(".ret-sent").click(function(){

                $.ajax( {
                    type : 'post',
                    url : '/api/send_phone_code.action',
                    cache : false,
                    async: false,
                    dataType:'json',
                    data : {
                        "t" : 0,
                        "act" : "payoutUseBalance"
                    },
                    success : function(rst) {
                        if (rst && rst.errno == 0) {
                            $(".pay-blan").find(".ret-sent").hide();
                            $(".pay-blan").find(".ret-sent").parent().find("span").show();
                            djs();
                        }else{
                            var msg = "发送验证码出现错误";
                            if (rst && rst.msg) {
                                msg = rst.msg;
                            }
                            layer.msg(msg);
                        }
                    }
                });


            });
        }
    });
}
//微信支付
function payWchat(){
    var html = $(".weixinopen").html();
    layer.open({
        type: 1,
        title:'',
        skin:'pay-wchat',
        closeBtn: 0,
        anim: 2,
        area:['933px','380px'],
        content: html,
        success:function(){
            $(".pay-wchat").find(".closebtn").click(function(){
                layer.closeAll();
                clearInterval(cleanRequest);
            });
            $(".pay-wchat").find(".payMoney_span").html($(".onlinepay").find(".needpay").text());

            if(payoutResultData.success == 'T') {
                $(".pay-wchat").find(".scanpic iframe").show();
                $(".pay-wchat").find(".scanpic p").show();
                $(".pay-wchat").find(".scanpic h3").hide();

                oid = payoutResultData.oid;

                tosetWpic();
                clearInterval(cleanRequest);
                cleanRequest = window.setInterval(queryOrderStatus,qrCodeRefreshTime);
            }else{
                $(".pay-wchat").find(".scanpic iframe").hide();
                $(".pay-wchat").find(".scanpic p").hide();

                if(payoutResultData.msg == "getPayWayFail"){
                    $(".pay-wchat").find(".scanpic h3").html('获取支付二维码失败，请重试，如重试后仍无法支付，请<a href="#">联系客服</a>！');
                }else{
                    $(".pay-wchat").find(".scanpic h3").html(payoutResultData.msg);
                }

                $(".pay-wchat").find(".scanpic h3").show();
            }

        }
    });
}
var cleanRequest;
//支付宝支付
function payAlipay(){
    var html = $(".payalipay").html();
    layer.open({
        type: 1,
        title:'',
        skin:'pay-alipay',
        closeBtn: 0,
        anim: 2,
        area:['933px','380px'],
        content: html,
        success:function(){
            $(".pay-alipay").find(".closebtn").click(function(){
                layer.closeAll();
                clearInterval(cleanRequest);
            });
            $(".pay-alipay").find(".payMoney_span").html($(".onlinepay").find(".needpay").text());

            if(payoutResultData.success == 'T') {
                $(".pay-alipay").find(".scanpic iframe").show();
                $(".pay-alipay").find(".scanpic p").show();
                $(".pay-alipay").find(".scanpic h3").hide();

                 oid = payoutResultData.oid;

                tosetApic();
                clearInterval(cleanRequest);
                cleanRequest = window.setInterval(queryOrderStatus,qrCodeRefreshTime);
            }else{
                $(".pay-alipay").find(".scanpic iframe").hide();
                $(".pay-alipay").find(".scanpic p").hide();

                if(payoutResultData.msg == "getPayWayFail"){
                    $(".pay-alipay").find(".scanpic h3").html('获取支付二维码失败，请重试，如重试后仍无法支付，请<a href="#">联系客服</a>！');
                }else{
                    $(".pay-alipay").find(".scanpic h3").html(payoutResultData.msg);
                }

                $(".pay-alipay").find(".scanpic h3").show();
            }
        }
    });
}

//获取手续费
function getReduce(payway,amount){
    var reduce = 0;
    $.ajax({
        type:'post',
        url:'/payment/getReduce.action?payway='+ payway+"&amount="+amount,
        cache:false,
        async:false,
        dataType:'json',
        success:function(data) {
            if(data.result == 'T'){
                reduce = data.reduce;
            }
        }
    });
    return reduce;
}

//倒计时
function djs(){
    var wait=59;
    function time(){
        if($(".pay-blan").length==1){
            if (wait == 0) {
                $(".pay-blan").find(".ret-djs").hide();
                $(".pay-blan").find(".ret-sent").show();
            }else{
                $(".pay-blan").find(".djs-s").text(wait+'s');
                wait--;
                setTimeout(function() {
                    time()
                },1000);
            }
        }
    };
    time();
};

//微信支付成功后执行
function payWsucc(){
    $(".pay-wchat").find(".scanpic").hide();
    $(".pay-wchat").find(".succpic").show();
    $(".pay-wchat").find(".succpic a").attr("href",payoutBackUrl);
    var t = setInterval(function(){
        var count = parseInt($(".pay-wchat").find(".todjs").text());
        count--;
        if(count >0) {
            $(".pay-wchat").find(".todjs").text(count)
        }else if(count==0){
            window.location = payoutBackUrl;
            clearInterval(t);
            return;
        }else{
            clearInterval(t);
        }
    }, 1000);
}
//支付宝支付成功后执行
function payAsucc(){
    $(".pay-alipay").find(".scanpic").hide();
    $(".pay-alipay").find(".succpic").show();
    $(".pay-alipay").find(".succpic a").attr("href",payoutBackUrl);

    var t = setInterval(function(){
        var count = parseInt($(".pay-alipay").find(".todjs").text());
        count--;
        if(count >0) {
            $(".pay-alipay").find(".todjs").text(count)
        }else if(count==0){
            window.location = payoutBackUrl;
            clearInterval(t);
            return;
        }else{
            clearInterval(t);
        }
    }, 1000);
}

//微信支付二维码
function tosetWpic(){
    $(".pay-wchat").find(".scanpic iframe").attr("src", payUrl + "/pay/send.action?oid=" + oid +"&rand=" + new Date().getTime());
}
//支付宝支付二维码
function tosetApic(){
    $(".pay-alipay").find(".scanpic iframe").attr("src", payUrl + "/pay/send.action?oid=" + oid +"&rand=" + new Date().getTime());
}
//余额输入密码提交
function VadPwd(pswd,obj){
    if(pswd == ""){
        obj.parent().find("input").addClass("error");
        obj.parent().find("em").show();
        return;
    }
    var marketflag = $("#marketflag").val();
    var marketflag_ = $("#marketflag_").val();
    var mobilechecked = $("#mobilechecked").val();

    if(marketflag != ""){
        if(marketflag == marketflag_){
            layer.msg("资金安全体系升级，检测到您的支付密码和登录密码相同，资金存在安全风险，请 <a href='/commerical/toChangetransactionPass.action' class='blue'>重新设置支付密码</a>");
            return;
        }
    }else{
        layer.msg("未设置支付密码，请选择其他验证方式");
        return;
    }

    $("#validway").val("transactionpass");


    isOk("transactionpass",pswd,"");
    if(yzinfoFlag != "1"){
        obj.parent().find("input").addClass("error");
        obj.parent().find("em").show();
        return;
    }else{
        if($(".allpayway").find(".checkbox_active").length == 2){
            thirdPay();
        }else{
            $("#transactionpass").val(pswd);
            $('#payForm').attr('action', payoutUseBalanceUrl);
            $('#payForm').submit();
        }
    }
}
//忘记密码输入验证码提交
function VadYzm(yzcode,obj){
    $("#validway").val("mobilenum");

    isOk("mobilenum",yzcode,"payoutUseBalance");

    if(yzinfoFlag != "1"){
        obj.parent().find("input").addClass("error");
        if("over" == yzinfoFlag){
            layer.msg('超过验证码验证次数，请稍后再试');
        }else{
            obj.parent().find("em").show();
        }
        return;
    }else{
        if($(".allpayway").find(".checkbox_active").length == 2){
            thirdPay();
        }else{
            $("#verificationcode").val(yzcode);
            $('#payForm').attr('action', payoutUseBalanceUrl);
            $('#payForm').submit();
        }

    }
}

//忘记密码手机号码
function tosetPhone(){
    $(".pay-blan").find(".phone").text(phone);
}

$(function(){
    //判断默认支付方式
    LoadPay();
    //确认提交时间
    $(".submita").click(function(){
        if($(".allpayway").find(".checkbox_active").length==0){
            layer.msg('请先选择付款方式');
        }else{
            if($(".allpayway").find(".checkbox_active").length==2){
                $("#yefalg").val(1);
                $("#hdn_useBalance").val(haspay);
                payBlan();
            }else{
                if($(".allpayway").find(".checkbox_active").attr("val")=="2"){
                    if(balance < orderPrice){
                        layer.msg('请选择正确的付款方式');
                        return;
                    }else{
                        payBlan();
                    }
                }else{
                    thirdPay();
                }
            }

        }
    });

});

function thirdPay(){
    $("#validway").val("nobalance");

    var payway = $("#payway").val();
    var params = $("#payForm").serialize();

    if(payway == "3002" || payway == "9110" || payway == "9003"){

        $.ajax({
            type:'post',
            url:payoutAjaxUrl,
            async:false,
            data : params,
            dataType:'json',
            success:function(data) {
                payoutResultData = data;
                if(payway == "3002" || payway == "9110"){
                    payAlipay(); //支付宝支付弹窗
                }else if(payway == "9003"){
                    payWchat(); //微信支付弹窗
                }
            }
        });
    }else{
        $('#payForm').attr('action', payoutUrl);
        $('#payForm').submit();
    }
}

function queryOrderStatus(){
    $.ajax({
        url :  payUrl + "/pay/queryOrderStatus.action",
        type : "POST",
        data : {"oid":oid},
        dataType: "jsonp",
        success : function(data) {
            var payway = $("#payway").val();
            if(data != ""){
                if(data.status == "1"){
                    if(cleanRequest != ""){
                        clearInterval(cleanRequest);
                    }
                    if(payoutBackUrl == "" && data.backurl != ""){
                        payoutBackUrl = data.backurl;
                    }
                    //支付成功 页面跳转
                    if(payway == "9110"){
                        payAsucc();
                    }else if(payway == "9003"){
                        payWsucc();
                    }
                }else{
                    //获取支付二维码
                    if(payway == "9110"){
                        tosetApic();
                    }else if(payway == "9003"){
                        if("9106" != payoutResultData.payway && "9111" != payoutResultData.payway){
                            tosetWpic();
                        }
                    }
                }
            }
        }
    });
}
var yzinfoFlag="1";
function  isOk(validway,yztxt,mobilenumType){
    $.ajax( {
        type : 'post',
        url : '/payment/payIsFlag.action',
        cache : false,
        async: false,
        data : {
            "validway" : validway,
            "yztxt" : yztxt,
            "mobilenumType" : mobilenumType
        },
        success : function(data) {
            if(data=="true"){
                yzinfoFlag="1";
            }else{
                yzinfoFlag=data;
            }
        }
    });
}