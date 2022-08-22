import qrcode
import qrcode.image.svg

img = qrcode.make(
  'https://youtube.com/endre-synnes',
  image_factory=qrcode.image.svg.SvgImage
)

img.save('my-page.svg')
