from architecture import resnet101

def build_backbone(backbone, output_stride, BatchNorm):
    if backbone == 'resnet':
        return resnet101.ResNet101(output_stride, BatchNorm)
    else:
        raise NotImplementedError

