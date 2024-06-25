//index.js
var app = getApp()
Page({
  data: {
    scale: 18,
    latitude: 0,
    longitude: 0
  },
// 页面加载
  onLoad: function (options) {
    // 1.获取定时器
    this.timer = options.timer;

    // 2.获取并设置当前位置经纬度
    wx.getLocation({
      type: "gcj02",
      success: (res) => {
        this.setData({
          longitude: res.longitude,
          latitude: res.latitude
        })
      }
    });

    // 3.设置地图控件的位置及大小
    wx.getSystemInfo({
      success: (res) => {
        this.setData({
          controls: [{
            id: 1,
            iconPath: '/images/location.png',
            position: {
              left: 20,
              top: res.windowHeight - 80,
              width: 50,
              height: 50
            },
            clickable: true
          },
          {
            id: 2,
            iconPath: '/images/use.png',
            position: {
              left: res.windowWidth/2 - 45,
              top: res.windowHeight - 100,
              width: 90,
              height: 90
            },
            clickable: true
          },
          {
            id: 3,
            iconPath: '/images/warn.png',
            position: {
              left: res.windowWidth - 70,
              top: res.windowHeight - 80,
              width: 50,
              height: 50
            },
            clickable: true
          },
          {
            id: 4,
            iconPath: '/images/marker.png',
            position: {
              left: res.windowWidth/2 - 11,
              top: res.windowHeight/2 - 45,
              width: 22,
              height: 45
            },
            clickable: true
          },
          {
            id: 5,
            iconPath: '/images/avatar.png',
            position: {
              left: res.windowWidth - 68,
              top: res.windowHeight - 155,
              width: 45,
              height: 45
            },
            clickable: true
          }]
        })
      }
    });

    // 4.请求服务器，显示附近的购物车
    
  },
// 页面显示
  onShow: function(){
    // 1.移动当前位置到地图中心
    this.mapCtx = wx.createMapContext("ofoMap");
    this.movetoPosition()
  },
// 地图控件
  bindcontroltap: function(e){
    // 判断点击的是哪个控件
    switch(e.controlId){
      // 点击定位控件
      case 1: this.movetoPosition();
        break;
      case 2: if(this.timer === "" || this.timer === undefined){
          wx.scanCode({
            success: (res) => {
              wx.showLoading({
                title: '正在获取密码',
                mask: true
              })
              
            }
          })
        }else{
          wx.navigateBack({
            delta: 1
          })
        }  
        break;
      // 点击保障控件
      case 3: wx.navigateTo({
          url: '../warn/index'
        });
        break;
      // 点击头像控件
      case 5: wx.navigateTo({
          url: '../my2/index'
        });
        break; 
      default: break;
    }
  },

  bindmarkertap: function(e){
    console.log(e);
    let _markers = this.data.markers;
    let markerId = e.markerId;
    let currMaker = _markers[markerId];
    this.setData({
      polyline: [{
        points: [{
          longitude: this.data.longitude,
          latitude: this.data.latitude
        }, {
          longitude: currMaker.longitude,
          latitude: currMaker.latitude
        }],
        color:"#FF0000DD",
        width: 1,
        dottedLine: true
      }],
      scale: 18
    })
  },
// 定位函数，移动位置到地图中心
  movetoPosition: function(){
    this.mapCtx.moveToLocation();
  }
})
