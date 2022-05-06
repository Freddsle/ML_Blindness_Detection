import torchvision
import torch
from PIL import Image


def img_transform(dzn_photo, RESCALE_SIZE):
    image = Image.open(dzn_photo)
    image.load()

    transform = torchvision.transforms.Compose([
                torchvision.transforms.Resize(RESCALE_SIZE),
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize([0.485, 0.456, 0.406],
                                                 [0.229, 0.224, 0.225]),
                ])

    tensor_image = transform(image)
    tensor_image = tensor_image.unsqueeze(0)
    return tensor_image


def load_model(PATH):
    model = torchvision.models.vgg19_bn()
    N_CLASSES = 5
    num_features = 4096
    model.classifier[6] = torch.nn.Linear(num_features, N_CLASSES)
    model.load_state_dict(torch.load(PATH, map_location=torch.device('cpu')))
    model.eval()
    return model


def predict(inputs, model):
    out = model(inputs)
    out = torch.nn.functional.softmax(out, dim=-1)
    _, preds = torch.max(out.data, 1)

    return preds


def ml_for_eye_care(dzn_photo):    
    
    PATH = '../data/model/vgg19.txt'
    RESCALE_SIZE = 224, 224

    model = load_model(PATH)
    
    img = img_transform(dzn_photo, RESCALE_SIZE)

    pred = predict(img, model)

    return pred