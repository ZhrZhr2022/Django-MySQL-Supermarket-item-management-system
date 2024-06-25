let username = ''
let password = ''

Page({
  data: {
    username: '',
    password: '',
    flag: '',
    clientHeight: '',
    list: ''
  },

  content(e) {
    username = e.detail.value
  },

  password(e) {
    password = e.detail.value
  },

  login: function (e) {
    // Check if username and password are provided
    if (!username || !password) {
      wx.showToast({
        icon: 'none',
        title: '账号和密码不能为空',
      })
      return;
    }

    // Make request to login
    wx.request({
      url: 'http://192.168.32.175:8000/wechat/login/',
      data: {
        flag: 0,
        username: username,
        password: password
      },
      method: 'POST',
      header: {
        "content-type": "application/json"
      },
      success: function (res) {
        if (res.data["message"] === 'yes') { // 登录成功
          wx.showToast({
            title: '登陆成功！！',
            icon: 'success',
            duration: 1000
          })
          wx.setStorage({
            key: 'overage',
            data: {
              overage: res.data["overage"]
            },
            success: function () {
              console.log('overage 值已成功更新为:', res.data["overage"]);
            },
            fail: function (error) {
              console.error('更新 overage 值失败:', error);
            }
          });
          wx.setStorage({
            key: 'username1',
            data: {
              username1: res.data["username"]
            },
            success: function () {
              console.log('username 值已成功更新为:', res.data["username"]);
            },
            fail: function (error) {
              console.error('更新 username 值失败:', error);
            }
          });
          wx.setStorage({
            key: 'password1',
            data: {
              password1: res.data["password"]
            },
            success: function () {
              console.log('password 值已成功更新为:', res.data["password"]);
            },
            fail: function (error) {
              console.error('更新 password 值失败:', error);
            }
          });
          setTimeout(function () {
            wx.reLaunch({
              url: '../wallet/index'
            })
          }, 1000)
        } else if (res.data["message"] === 'no1') { // 密码错误
          wx.showToast({
            icon: 'error',
            title: '密码错误',
            duration: 2500
          })
        } else if (res.data["message"] === 'no2') { // 未注册
          wx.showToast({
            title: '该用户不存在',
            icon: 'error',
            duration: 2500
          })
        }
      },
      fail: function (res) {
        console.log("false")
      },
    })
  }
})
