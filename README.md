## Example

#### Raw Skin

<img src='https://i.imgur.com/HqoJWhH.png' alt='Raw' /> 

### Render

#### Face
<img src='https://i.imgur.com/XpoN1vE.png' alt='front' /> <img src='https://i.imgur.com/HnBa2fR.png' alt='back' /> <img src='https://i.imgur.com/vIUDZ5j.png' alt='left' /> <img src='https://i.imgur.com/sSur3vQ.png' alt='right' /> 

#### Skin
<img src='https://i.imgur.com/TrzhqT8.png' alt='front' /> <img src='https://i.imgur.com/ZYmJrBz.png' alt='back' /> <img src='https://i.imgur.com/Q56WscN.png' alt='left' /> <img src='https://i.imgur.com/rYCNHU6.png' alt='right' /> 


## Usage

```bash
import Skinrender

Head = Skinrender.load('ImgExample/Steve.png').head(scale = 14)
Body = Skinrender.load('ImgExample/Steve.png').body()
Arm = Skinrender.load('ImgExample/Steve.png').arm()
Leg = Skinrender.load('ImgExample/Steve.png').leg()
Skin = Skinrender.load('ImgExample/Steve.png').skin()
```

## Args
| param| default | values | use in |
| ---- | ------- | ------ | ------ |
| scale | 16 | int | head, body, arm, leg and skin |
| color | transparent | tuple; RGB, example: (243,123,312) | skin |
| save | None | path of file | head, body, arm, leg and skin |
| position | front | front / left / right / back | head, body, arm, leg and skin |
| side | left | left / right | arm and leg |

## License
[MIT](https://choosealicense.com/licenses/mit/)
