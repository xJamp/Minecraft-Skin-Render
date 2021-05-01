from PIL import Image
COORDSMINECRAFTAPI = {'head' : {'front' : (8, 8, 16, 16), 'left' : (0, 8, 8, 16), 'right' : (16, 8, 24, 16), 'back' : (24, 8, 32, 16)}, 'body' : {'front' : (20,  20,  28,  32), 'left' : (16,  20,  20,  32), 'right' : (28,  20,  32,  32), 'back' : (32,  20,  40,  32)}, 'arm' : {'front' : {'left' : (44,  20,  48,  32), 'right' : (36,  52,  40,  64)}, 'left' : {'left' : (40,  20,  44,  32), 'right' : (32,  52,  36,  64)}, 'right' : {'left' : (48,  20,  52,  32), 'right' : (40,  52,  44,  64)}, 'back' : {'left' : (52,  20,  56,  32), 'right' : (44,  52,  48,  64)}}, 'leg' : {'front' : {'left' : (4,  20,  8,  32), 'right' : (20,  52,  24,  64)}, 'left' : {'left' : (0,  20,  4,  32), 'right' : (16,  52,  20,  64)}, 'right' : {'left' : (8,  20,  12,  32), 'right' : (24,  52,  28,  64)}, 'back' : {'left' : (12,  20,  16,  32), 'right' : (28,  52,  32,  64)}}, 'skin' : {'front' : [16, 4], 'back' : [16, 4], 'left' : [8, 0], 'right' : [8, 0]}}

class load():
    def __init__(self, src):
        self.Raw_skin = Image.open(src)

    def CheckArgs(self, args):
        if args not in ('front', 'back', 'left', 'right'):
            raise Exception('position acepta como argumentos: front, back, left y right')

    def save(self, img, src):
        img.save(src)

    def head(self, scale = 16, position = 'front', save = None):
        self.CheckArgs(position)

        HeadCrop = self.Raw_skin.crop(COORDSMINECRAFTAPI['head'][position])
        HeadCrop = HeadCrop.resize((8 * scale, 8 * scale))

        if save:
            self.save(HeadCrop, save)
        return HeadCrop

    def body(self, scale = 16, position = 'front', save = None):
        self.CheckArgs(position)

        BodyCrop = self.Raw_skin.crop(COORDSMINECRAFTAPI['body'][position])
        BodyCrop = BodyCrop.resize((8 * scale, 12 * scale))

        if save:
            self.save(BodyCrop, save)
        return BodyCrop


    def arm(self, scale = 16, side = 'left', position = 'front', save = None):
        self.CheckArgs(position)

        ArmCrop = self.Raw_skin.crop(COORDSMINECRAFTAPI['arm'][position][side])
        ArmCrop = ArmCrop.resize((4 * scale, 12 * scale))

        if save:
            self.save(ArmCrop, save)
        return ArmCrop

    def leg(self, scale = 16, side = 'left', position = 'front', save = None):
        self.CheckArgs(position)

        LegCrop = self.Raw_skin.crop(COORDSMINECRAFTAPI['leg'][position][side])
        LegCrop = LegCrop.resize((4 * scale, 12 * scale))

        if save:
            self.save(LegCrop, save)
        return LegCrop

    def skin(self, scale = 16, position = 'front', save = None, color = 0):
        self.CheckArgs(position)

        if color == 0:
            mode = 'RGBA'
        else:
            mode = 'RGB'

        skin = Image.new( mode = mode, size = (COORDSMINECRAFTAPI['skin'][position][0] * scale, 32 * scale), color = color)

        HeadCrop = self.head(scale = scale, position = position)
        skin.paste(HeadCrop, (COORDSMINECRAFTAPI['skin'][position][1]* scale , 0))

        if position == 'front' or position == 'back':
            BodyCrop = self.body(scale = scale, position = position)
            skin.paste(BodyCrop, (4* scale , 8* scale))

            ArmLeftCrop = self.arm(scale = scale, side = 'left', position = position)
            skin.paste(ArmLeftCrop, (0 , 8* scale))

            ArmrightCrop = self.arm(scale = scale, side = 'right', position = position)
            skin.paste(ArmrightCrop, (12* scale , 8* scale))

            legLeftCrop = self.leg(scale = scale, side = 'left', position = position)
            skin.paste(legLeftCrop, (4* scale , 20* scale))

            legrightCrop = self.leg(scale = scale, side = 'right', position = position)
            skin.paste(legrightCrop, (8* scale , 20* scale))

        else:
            if position == 'left':
                ArmCrop = self.arm(scale = scale, side = 'left', position = 'left')
                legCrop = self.leg(scale = scale, side = 'left', position = 'left')
            else:
                ArmCrop = self.arm(scale = scale, side = 'right', position = 'right')
                legCrop = self.leg(scale = scale, side = 'right', position = 'right')

            skin.paste(ArmCrop, (2* scale , 8* scale))
            skin.paste(legCrop, (2* scale , 20* scale))

        if save:
            self.save(skin, save)
        return skin