//index.js
//获取应用实例
const app = getApp()
 let nickname=''
 let username=''
 let password=''

Page({
  data: {
    username: '',
    password: '',
    nickname: '',
    clientHeight:'',
    list:''
  },
  //链接本地数据库
  login:function(e){
    console.log(this.data.username, this.data.password)
    wx.request({
      url: 'http://192.168.32.175:8000/wechat/login/',
      
      data:{username:this.data.username,password:this.data.password},
      method:'POST',
      header:{
                "content-type": "application/json"    //使用POST方法要带上这个header
              },
      success:function(res){
        console.log(res.data)
        console.log("ok")
      },
      fail:function(res){
        console.log("false")
      },
      complete:function(res){} 
    })
  },
  onLoad(){
    var that=this
    wx.getSystemInfo({ 
      success: function (res) { 
        console.log(res.windowHeight)
          that.setData({ 
              clientHeight:res.windowHeight
        }); 
      } 
    }) 
  },
  //获取输入款内容
  content(e){
    username=e.detail.value
  },
  password(e){
    password=e.detail.value
  },
  nickname(e){
    nickname=e.detail.value
  },
  url(){
    wx.reLaunch({
      url: '../index/index',
    })
  },
  //注册事件
  bindGetPhoneNumber(){
    var that = this; // 保存页面对象的引用
    console.log(this.data.username, this.data.password)
    if (username == '') {
      wx.showToast({
        icon: 'none',
        title: '账号不能为空',
      })
    }else if(username.length != 11){
      wx.showToast({
        icon: 'none',
        title: '账号格式不正确',
      })
    }else if (password == '') {
      wx.showToast({
        icon: 'none',
        title: '密码不能为空',
      })
    }else if (this.data.username != '' && this.data.password != '') {
      wx.request({
        url: 'http://192.168.32.175:8000/wechat/login/',
        //url: 'https://61.132.231.210:43446/wechat/login/',
        data: {
          flag : 1,
          username: this.data.username,
          password: this.data.password
        },
        method: 'POST',
        header: {
          "content-type": "application/json" //使用POST方法要带上这个header
        },
        success: function (res) {
          console.log(res.data["message"])
          console.log("ok")
          /*if (res.data["message"] == 'no1') { //密码错误//
            wx.showToast({
              icon: 'error',
              title: '密码错误',
              duration: 2500
            })
            that.setData({username:''});
            that.setData({password:''});
            //username= '';
            //password= '';
          } else */
          if (res.data["message"] == 'no1') { //未注册//已注册
            wx.showToast({
              title: '该用户已注册',
              icon: 'error',
              duration: 2500
            })
            that.setData({username:''});
            that.setData({password:''});
            //Page.data.username= '';
            //Page.data.psssword= '';
          } else if (res.data["message"] == 'yes') {
            wx.showToast({ //显示登录成功信息
              title: '注册成功！！',
              icon: 'success',
              duration: 1000
            })
            setTimeout(function () {
              //要延时执行的代码
              wx.reLaunch({
                url: '../my2/index'
              })
            }, 1000) //延迟时间
          }
        },
        fail: function (res) {
          console.log("false")
        },
      })
    }

/* 
    {
      wx.cloud.database().collection('admin').add({
        data: {
          nickname: nickname,
          username: username,
          password: password
        },
        success(res) {
          console.log('注册成功', res)
          wx.showToast({
            title: '注册成功',
            duration: 1000
          })
          
          wx.setStorageSync('admin', username)
                setTimeout(function () {
                  //要延时执行的代码
                  wx.reLaunch({
                    url: '../my2/index',
                  })
                }, 1000) //延迟时间
        },
        fail(res) {
          console.log('注册失败', res)
        }
      })
        
      }*/
    
  },
})
 

