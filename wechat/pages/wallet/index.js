// pages/wallet/index.js
Page({
  data:{
    overage: 0,
    ticket: 0,
    username1:'',
    password1:''
  },
// 页面加载
  onLoad:function(options){
     wx.setNavigationBarTitle({
       title: '我的钱包'
     })
     
  },
// 页面加载完成，更新本地存储的overage
  onReady:function(){
     wx.getStorage({
      key: 'overage',
      success: (res) => {
        this.setData({
          overage: res.data.overage
        })
      }
    })
  },
// 页面显示完成，获取本地存储的overage
  onShow:function(){
    wx.getStorage({
      key: 'overage',
      success: (res) => {
        this.setData({
          overage: res.data.overage
        })
      }
    }) 
  },
// 余额说明
  overageDesc: function(){
    wx.showModal({
      title: "",
      content: "余额用于购物结束时的自动扣款服务",
      showCancel: false,
      confirmText: "我知道了",
    })
  },
  shiming:function(){
    wx.navigateTo({
      url: '../face/index'
    })
  },
// 跳转到充值页面
  movetoCharge: function(){
    // 关闭当前页面，跳转到指定页面，返回时将不会回到当前页面
    wx.redirectTo({
      url: '../charge/index'
    })

  },
// 用车券
  showTicket: function(){
    wx.showModal({
      title: "",
      content: "你没有用车券了",
      showCancel: false,
      confirmText: "好吧",
    })
  },
  showmingxi: function(){
    wx.showModal({
      title: "",
      content: "无使用记录",
      showCancel: false,
      confirmText: "确认",
    })
  },
// 押金退还
  showDeposit: function(){
    wx.showModal({
      title: "",
      content: "押金会立即退回，退款后，您将不能使用智U购购物车，确认要进行此退款吗？",
      cancelText: "继续使用",
      cancelColor: "#b9dd08",
      confirmText: "押金退款",
      confirmColor: "#ccc",
      success: (res) => {
        if(res.confirm){
          wx.showToast({
            title: "退款成功",
            icon: "success",
            duration: 2000
          })
        }
      }
    })
  },
// 关于ofo
  showInvcode: function(){
    wx.showModal({
      title: "智U购服务",
      content: "欢迎关注微信公众号：一岩",
      showCancel: false,
      confirmText: "感谢体验"
    })
  }
})