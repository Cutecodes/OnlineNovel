window.onload = function() {
    // var regtel = /^1[|3|4|5|7|8]\d{9}$/;  //电话号码
    var name = /^([a-zA-Z]+)([a-zA-Z0-9]*)$/; //英文开头的用户名
    var emailReg = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/; //邮箱
    var regpwd = /^[a-zA-Z0-9_-]{6,16}/; //密码
    var regCode = /^[a-zA-Z0-9]+$/; //验证码
    // var tel = document.querySelector("#tel");
    var form = document.querySelector("#form");
    var submitBtn = document.querySelector("#submit");
    var userName = document.querySelector("#userName");
    var email = document.querySelector("#email");
    var pwd = document.querySelector("#pwd");
    var repwd = document.querySelector("#repwd");
    var verifyCode = document.querySelector("#verifyCode");
    // regxbp(tel, regtel);
    regxbp(userName, name, "字母开头,可包含字母、数字", 1);
    regxbp(email, emailReg, "您的邮箱", 2);
    regxbp(pwd, regpwd, "请输入6-16位密码", 3);
    regxbp(verifyCode, regCode, "请输入验证码", 5);
    submitBtn.onclick = checkSubmit
    var checkItem = [false, false, false, false, false, false]
    var inputItem = [userName, userName, email, pwd, repwd, verifyCode]
    var msg = ["空或已存在的用户名", "字母开头,可包含字母、数字", "邮箱格式有误", "请输入6-16位密码", "两次密码不一致", "验证码有误"]
        //更新验证码


    function encodeMD5(str) {
        return CryptoJS.MD5(str).toString(); //Hash加密
    }

    function checkSubmit() {
        for (index in checkItem) {

            if (!checkItem[index]) {
                inputItem[index].nextElementSibling.className = 'error';
                inputItem[index].nextElementSibling.innerHTML = '<i class="error_icon"></i>' + msg[index];
                return;
            }
        }
        //提交时对密码加密
        pwd.value = encodeMD5(pwd.value);
        repwd.value = encodeMD5(repwd.value);

        form.submit();
    }

    function checkUserName(ele) {
        /* 实例化XMLHttpResquest*/
        var xhr = new XMLHttpRequest();

        /* 监控xhr对象的状态,只要xhr.readyState值改变就会触发事件由alert弹出框的值可以知道
            a.以下xhr.readyState值为4的时候表示请求响应结束，数据接收完毕并且可以使用
            b.xhr.status值为200表示请求成功
        */
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status == 200) {
                    var data = xhr.responseText;
                    if (data == 1) {
                        ele.nextElementSibling.className = 'success';
                        ele.nextElementSibling.innerHTML = '<i class="success_icon"></i>用户名可用';
                        checkItem[0] = true;
                    } else if (data == 2) {
                        ele.nextElementSibling.className = 'error';
                        ele.nextElementSibling.innerHTML = '<i class="error_icon"></i>用户名已存在';
                        checkItem[0] = false;
                    } else {
                        ele.nextElementSibling.className = 'error';
                        ele.nextElementSibling.innerHTML = '<i class="error_icon"></i>' + data;
                        checkItem[0] = true;
                    }

                }
            }
        }
        var testUrl = "http://localhost:8080/util/isExistUser?userName=" + ele.value;
        var url = '/util/isExistUser?userName=' + ele.value;
        xhr.open('get', testUrl, true);
        xhr.send(null);
    }
    //检查验证码
    function checkVerifyCode(ele) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status == 200) {
                    var data = xhr.responseText;
                    if (data == 1) {
                        ele.nextElementSibling.className = 'success';
                        ele.nextElementSibling.innerHTML = '<i class="success_icon"></i>';
                        checkItem[5] = true;
                    } else if (data == 2) {
                        ele.nextElementSibling.className = 'error';
                        ele.nextElementSibling.innerHTML = '<i class="error_icon"></i>';
                        checkItem[5] = false;
                    } else {
                        ele.nextElementSibling.className = 'error';
                        ele.nextElementSibling.innerHTML = '<i class="error_icon"></i>' + data;
                        checkItem[5] = false;
                    }

                }
            }
        }
        var testUrl = "http://localhost:8080/util/checkVerifyCode?verifyCode=" + ele.value;
        var url = '/util/isExistUser?userName=' + ele.value;
        xhr.open('get', testUrl, true);
        xhr.send(null);
    }

    function regxbp(ele, reg, msg = "", index = 1) {
        ele.onblur = function() {
            if (this.value == "") {
                this.nextElementSibling.className = "success";
                this.nextElementSibling.innerHTML = msg;
                checkItem[index] = false;
            } else if (reg.test(this.value)) {
                this.nextElementSibling.className = 'success';
                this.nextElementSibling.innerHTML = '<i class="success_icon"></i>';
                checkItem[index] = true;
                if (index == 1) {
                    checkUserName(this);
                }
                if (index == 5) {
                    checkVerifyCode(this);
                }
            } else {
                this.nextElementSibling.className = 'error';
                this.nextElementSibling.innerHTML = '<i class="error_icon"></i>' + msg;
                checkItem[index] = false;
            }
        }
    }

    repwd.onblur = function() {
        if (this.value == "") {
            this.nextElementSibling.className = "";
            this.nextElementSibling.innerHTML = "";
            checkItem[4] = false;
        } else if (this.value == pwd.value) {
            this.nextElementSibling.className = 'sucuess';
            this.nextElementSibling.innerHTML = '<i class="success_icon"></i>  两次输入的密码一致';
            checkItem[4] = true;
        } else {
            this.nextElementSibling.className = 'error';
            this.nextElementSibling.innerHTML = '<i class="error_icon"></i>  两次输入的密码不一致';
            checkItem[4] = false;
        }
    }

}