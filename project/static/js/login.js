window.onload = function() {

    // var regtel = /^1[|3|4|5|7|8]\d{9}$/;  //电话号码
    var name = /^([a-zA-Z]+)([a-zA-Z0-9]*)$/; //英文开头的用户名
    var regpwd = /^[a-zA-Z0-9_-]{6,16}/; //密码
    var regCode = /^[a-zA-Z0-9]+$/; //验证码
    // var tel = document.querySelector("#tel");
    var form = document.querySelector("#form");
    var submitBtn = document.querySelector("#submit");
    var userName = document.querySelector("#userName");
    var pwd = document.querySelector("#pwd");
    var verifyCode = document.querySelector("#verifyCode");
    // regxbp(tel, regtel);
    regxbp(userName, name, "您的用户名", 1);
    regxbp(pwd, regpwd, "请输入密码", 2);
    regxbp(verifyCode, regCode, "请输入验证码", 3);
    submitBtn.onclick = checkSubmit
    var checkItem = [true, false, false, false]
    var inputItem = [userName, userName, pwd, verifyCode]
    var msg = ["空或已存在的用户名", "用户名错误", "请输入密码", "验证码有误"]
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
        form.submit();
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
                        checkItem[3] = true;
                    } else if (data == 2) {
                        ele.nextElementSibling.className = 'error';
                        ele.nextElementSibling.innerHTML = '<i class="error_icon"></i>';
                        checkItem[3] = false;
                    } else {
                        ele.nextElementSibling.className = 'error';
                        ele.nextElementSibling.innerHTML = '<i class="error_icon"></i>' + data;
                        checkItem[3] = false;
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
                if (index == 3) {
                    checkVerifyCode(this);
                }
            } else {
                this.nextElementSibling.className = 'error';
                this.nextElementSibling.innerHTML = '<i class="error_icon"></i>' + msg;
                checkItem[index] = false;
            }
        }
    }

}