// pages/billing/index.js
Page({
  data:{
    hours: 0,
    minuters: 0,
    seconds: 0,
    billing: "正在计费"
  },
// 页面加载
  onLoad:function(options){
    this.setData({
      number: options.number,
      timer: this.timer
    })
    let s = 0;
    let m = 0;
    let h = 0;
    this.timer = setInterval(() => {
      this.setData({
        seconds: s++
      })
      if(s == 60){
        s = 0;
        m++;
        setTimeout(() => {         
          this.setData({
            minuters: m
          });
        },1000)      
        if(m == 60){
          m = 0;
          h++
          setTimeout(() => {         
            this.setData({
              hours: h
            });
          },1000)
        }
      };
    },1000)  
  },
  endRide: function(){
    clearInterval(this.timer);
    this.timer = "";
    this.setData({
      billing: "本次使用耗时",
      disabled: true
    })
  },
  moveToIndex: function(){
    if(this.timer == ""){
      wx.redirectTo({
        url: '../index/index'
      })
    }else{
      wx.navigateTo({
        url: '../index/index?timer=' + this.timer
      })
    }
  }
})