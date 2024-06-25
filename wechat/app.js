//app.js
const AV = require('/utils/av-weapp-min.js'); 
AV.init({
  appId: 'pTf5kDMERjsFopcOt9mO4C3e-gzGzoHsz', 
  appKey: 'YRb4tW0mekPrVHpCHzokI3Bf'
})
App({
  onLaunch:function () {
    wx.cloud.init({
      env:"cloud1-2g639alh3d190371"
    })
  }
})