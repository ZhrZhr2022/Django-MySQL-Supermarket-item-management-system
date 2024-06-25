// pages/charge/index.js
let username2 = '';
let password2 = '';
let overage2 = 0.00;
Page({
  data: {
    inputValue: '0.00'
    //username2: '',
    //password2: ''
  },
  // 页面加载
  onLoad: function (options) {
    wx.setNavigationBarTitle({
      title: '充值'
    });
  },
  // 存储输入的充值金额
  bindInput: function (res) {
    let inputValue = parseFloat(res.detail.value); 
    inputValue = isNaN(inputValue) ? 0.00 : inputValue.toFixed(2); 
    this.setData({
      inputValue: inputValue
    });
  },
  // 充值
  charge: function () {
    // 必须输入大于0的数字
    if (parseFloat(this.data.inputValue) <= 0 || isNaN(parseFloat(this.data.inputValue))) {
      wx.showModal({
        title: "警告",
        content: "咱是不是还得给你钱？！！",
        showCancel: false,
        confirmText: "不不不不"
      });
    } else {
      let inputValue = parseFloat(this.data.inputValue);
      wx.getStorage({
        key: 'overage',
        success: (res) => {
          let currentOverage = parseFloat(res.data.overage) || 0;
          overage2 = (currentOverage + inputValue).toFixed(2);
          wx.getStorage({
            key: 'username1',
            success: (res) => {
              username2 = res.data.username1;
              wx.getStorage({
                key: 'password1',
                success: (res) => {
                  password2 = res.data.password1;
                  wx.request({
                    url: 'http://192.168.32.175:8000/wechat/login/',
                    data: {
                      flag: 2,
                      username: username2,
                      password: password2,
                      overage: overage2
                    },
                    method: 'POST',
                    header: {
                      "content-type": "application/json"
                    },
                    success: function () {
                      wx.showToast({
                        title: "充值成功",
                        icon: "success",
                        duration: 2000
                      });
                      console.log('成功添加余额，用户名', username2);
                      console.log('成功添加余额，密码', password2);
                      console.log('成功添加余额，余额', overage2);
                      wx.setStorage({
                        key: 'overage',
                        data: {
                          overage: overage2
                        },
                        success: function () {
                          wx.redirectTo({
                            url: '../wallet/index',
                          });
                        }
                      });
                    },
                    fail: function () {
                      console.log("请求失败");
                      console.log(res);
                    },
                  });
                },
                fail: function () {
                  console.log("获取密码失败");
                }
              });
            },
            fail: function () {
              console.log("获取用户名失败");
            }
          });
        },
        fail: (res) => {
          console.log("获取余额失败");
        }
      });
    }
  }
});
