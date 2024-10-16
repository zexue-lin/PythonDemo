import qrcode
from MyQR import myqr as mq

# 设置扫码二维码后跳转的链接
url = 'https://work.weixin.qq.com/ct/wcde31309ebc3ac4a7f684b97367a8c1fc1a'

# 设置图片路径
image_path = 'avatar.jpg'

# 生成二维码
mq.run(
    words=url,  # 二维码中包含的内容
    picture=image_path,  # 本地图片路径
    version=1,  # 生成二维码的版本号（1-40）
    colorized=True,  # 生成彩色二维码
    save_name='xhs_August.png'  # 保存的文件名
)
