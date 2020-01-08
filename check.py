from architecture.deeplab import *

model = DeepLab(num_classes=23,
                backbone='resnet',
                output_stride=16,
                sync_bn=None,
                freeze_bn=False)

print (model)
