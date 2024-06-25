// pages/scanresult/index.js
Page({
  data:{
    time: 9
  },
// 页面加载
  onLoad:function(options){
    this.setData({
      password: options.password
    })
    // 设置初始计时秒数
    let time = 9;
    this.timer = setInterval(() => {
      this.setData({
        time: -- time
      });
      if(time < 0){
        clearInterval(this.timer)
        wx.redirectTo({
          url: '../billing/index?number=' + options.number
        })
      }
    },1000)
  },
// 点击去首页报障
  moveToWarn: function(){
    clearInterval(this.timer)
    wx.redirectTo({
      url: '../index/index'
    })
  }
})