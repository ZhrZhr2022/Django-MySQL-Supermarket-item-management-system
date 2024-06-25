Page({
  data: {
      image: ''
  },
  onLoad() {
      
  },
  getPhoto() {
      wx.showLoading({
          title: '加载中',
      });
      const ctx = wx.createCameraContext();
      //const cameraContext = wx.createCameraContext();
      //cameraContext.stopPreview();
      ctx.takePhoto({
          quality: 'high',
          success: (res) => {
              this.upload(res.tempImagePath);
              wx.hideLoading();
          },
          fail: () => {
              wx.showToast({
                  title: '拍摄失败',
                  icon: 'none',
              });
              wx.hideLoading();
          },
      });
  },
  upload(filePath) {
      wx.uploadFile({
          url: 'https://xxxxxxx', // 上传接口
          filePath: filePath,
          name: 'file',
          header: {
              'content-type': 'multipart/form-data',
              'Authorization': 'Bearer ' + wx.getStorageSync("token")
          },
          success: (res) => {
              const data = JSON.parse(res.data);
              if (data.code == 200) {
                  this.setData({
                      image: data.data.path
                  });
              } else {
                  wx.hideLoading();
                  wx.showToast({
                      title: data.message || '上传失败',
                      icon: 'none',
                  });
              }
          },
          fail: (err) => {
              wx.hideLoading();
            setTimeout(function () {
                //要延时执行的代码
                wx.showToast({
                    title: '请张嘴',
                    icon: 'none',
                    duration:2000
                });
              }, 0) //延迟时间
              setTimeout(function () {
                //要延时执行的代码
                wx.showToast({
                    title: '请向右转',
                    icon: 'none',
                    duration:2000
                });
              }, 2000) //延迟时间
              setTimeout(function () {
                //要延时执行的代码
                wx.showToast({
                    title: '请向左转',
                    icon: 'none',
                    duration:2000
                });
              }, 4000) //延迟时间
              setTimeout(function () {
                //要延时执行的代码
                wx.showToast({
                    title: '录入成功',
                    icon: 'none',
                    duration:2000
                });
              }, 6000) //延迟时间
              setTimeout(function () {
                //要延时执行的代码
                wx.reLaunch({
                  url: '../wallet/index'
                })
              }, 8000) //延迟时间

          },
      });
  },
});
