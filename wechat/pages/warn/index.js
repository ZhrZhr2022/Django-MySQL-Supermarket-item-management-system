// pages/wallet/index.js
const AV = require('../../utils/av-weapp-min.js'); 
Page({
  data:{
    // 故障购物车周围环境图路径数组
    picUrls: [],
    // 故障购物车编号和备注
    inputValue: {
      num: 0,
      desc: ""
    },
    checkboxValue: [],
    actionText: "拍照/相册",
    btnBgc: "",
    itemsValue: [
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      },
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      },
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      },
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      },
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      },
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      },
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      },
      {
        checked: false,
        value: "///",
        color: "#b9dd08"
      }
    ]
  },
// 页面加载
  onLoad:function(options){
    wx.setNavigationBarTitle({
      title: '报障维修'
    })
  },
// 勾选故障类型，获取类型值存入checkboxValue
  checkboxChange: function(e){
    let _values = e.detail.value;
    if(_values.length == 0){
      this.setData({
        btnBgc: ""
      })
    }else{
      this.setData({
        checkboxValue: _values,
        btnBgc: "#b9dd08"
      })
    }   
  },
// 输入购物车编号，存入inputValue
  numberChange: function(e){
    this.setData({
      inputValue: {
        num: e.detail.value,
        desc: this.data.inputValue.desc
      }
    })
  },
// 输入备注，存入inputValue
  descChange: function(e){
    this.setData({
      inputValue: {
        num: this.data.inputValue.num,
        desc: e.detail.value
      }
    })
  },
// 选择故障购物车周围环境图 拍照或选择相册
  bindCamera: function(){
    wx.chooseImage({
      count: 4, 
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'], 
      success: (res) => {
        let tfps = res.tempFilePaths;
        let _picUrls = this.data.picUrls;
        for(let item of tfps){
          _picUrls.push(item);
          this.setData({
            picUrls: _picUrls,
            actionText: "+"
          });
        };
        var tempFilePath = res.tempFilePaths[0];
        new AV.File('pictrue', {
          blob: {
            uri: tempFilePath,
          },
        }).save().then(
          file => console.log(file.url())
        ).catch(console.error);
      }
    })
  },
// 删除选择的故障购物车周围环境图
  delPic: function(e){
    let index = e.target.dataset.index;
    let _picUrls = this.data.picUrls;
    _picUrls.splice(index,1);
    this.setData({
      picUrls: _picUrls
    })
  }
})