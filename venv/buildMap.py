import pygame
from floor import Floor
from brick import Brick
from block import Block  # testing Diverse Block
from questionBlock import QuestionBlock
from mushroomBlock import MushroomBlock
from unbreakableBrick import UnbreakableBrick
from pipe import Pipe
from goomba import Goomba
from koopa import Koopa


class BuildMap:
    def __init__(self, screen, settings):
        self.screen, self.settings = screen, settings
        self.file = open("maps/level1.txt", "r")
        self.textNewLine = "/n"
        self.line = ""
        self.lines = []
        self.xShift = 0
        self.yShift = 35

        if self.file.mode == "r":
            self.contents = self.file.read()
            print("Start of read")

        for chars in self.contents:
            if chars != "\n":
                self.line += chars
            else:
                self.lines.append(self.line)
                self.line = ""

    # def makeMap(self, floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes):
    #     size = self.settings.rectSize
    #     for row in self.lines:
    #         for chars in row:
    #             #  Floor
    #             if chars == "F":
    #                 newFloor = Floor(self.screen, self.settings)
    #                 newFloor.rect.x, newFloor.rect.y = self.xShift, self.yShift
    #                 self.xShift += size
    #                 floors.add(newFloor)
    #             #  Breakable brick
    #             elif chars == "B":
    #                 newBrick = Brick(self.screen, self.settings)
    #                 newBrick.rect.x, newBrick.rect.y = self.xShift + size / 4, self.yShift + size / 4
    #                 self.xShift += size
    #                 bricks.add(newBrick)
    #             #  Unbreakable brick
    #             elif chars == "U":
    #                 newUB = UnbreakableBrick(self.screen, self.settings)
    #                 newUB.rect.x, newUB.rect.y = self.xShift + size / 4, self.yShift + size / 4
    #                 self.xShift += size
    #                 unbreakableBricks.add(newUB)
    #             #  Pipe
    #             elif chars == "P":
    #                 newPipe = Pipe(self.screen, self.settings)
    #                 newPipe.rect.x, newPipe.rect.y = self.xShift + size / 4, self.yShift + size / 4
    #                 self.xShift += size
    #                 pipes.add(newPipe)
    #             #  Blank space
    #             elif chars == "X":
    #                 self.xShift += size
    #             #  ? block
    #             elif chars == "?":
    #                 newQuestion = QuestionBlock(self.screen, self.settings)
    #                 newQuestion.rect.x, newQuestion.rect.y = self.xShift + size / 4, self.yShift + size / 4
    #                 questionBlocks.add(newQuestion)
    #                 self.xShift += size
    #             #  Mushroom blocks (look like ? blocks):
    #             elif chars == "M":
    #                 newMushroom = MushroomBlock(self.screen, self.settings)
    #                 newMushroom.rect.x, newMushroom.rect.y = self.xShift + size / 4, self.yShift + size / 4
    #                 mushroomBlocks.add(newMushroom)
    #                 self.xShift += size
    # 
    #         self.xShift = 0
    #         self.yShift += size
    #     print("Done.")
    # 
    # def drawMap(self, floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes):
    #     for floor in floors:
    #         floor.blit()
    #     for brick in bricks:
    #         brick.blit()
    #     for questionBlock in questionBlocks:
    #         questionBlock.blit()
    #     for mushroomBlock in mushroomBlocks:
    #         mushroomBlock.blit()
    #     for unbreakableBrick in unbreakableBricks:
    #        unbreakableBrick.blit()
    #     for pipe in pipes:
    #         pipe.blit()
    # 
    # def shiftMap(self, floors, bricks, questionBlocks, mushroomBlocks, unbreakableBricks, pipes, settings):
    #     worldShift = 0
    #     if settings.moving_right == True:
    #         for floor in floors:
    #             floor.rect.x -= 1
    #         for brick in bricks:
    #             brick.rect.x -= 1
    #         for questionBlock in questionBlocks:
    #             questionBlock.rect.x -= 1
    #         for mushroomBlock in mushroomBlocks:
    #             mushroomBlock.rect.x -= 1
    #         for unbreakableBrick in unbreakableBricks:
    #             unbreakableBrick.rect.x -= 1
    #         for pipe in pipes:
    #             pipe.rect.x -= 1


# TESTING DIVERSE BLOCK -----------------------------------------------------------------------------------------

    def make_map(self, floors, blocks, pipes, goombas, invis, koopa):
        size = self.settings.rectSize
        for row in self.lines:
            for chars in row:
                #  Floor
                if chars == "F":
                    new_floor = Floor(self.screen, self.settings)
                    new_floor.rect.x, new_floor.rect.y = self.xShift, self.yShift
                    self.xShift += size
                    floors.add(new_floor)
                #  Breakable brick
                elif chars == "B":
                    new_brick = Block(self.screen, self.settings, 4)
                    new_brick.rect.x, new_brick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(new_brick)
                #  Unbreakable brick
                elif chars == "U":
                    new_brick = Block(self.screen, self.settings, 0)
                    new_brick.rect.x, new_brick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(new_brick)
                #  Pipe
                elif chars == "P":
                    new_pipe = Pipe(self.screen, self.settings)
                    new_pipe.rect.x, new_pipe.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    pipes.add(new_pipe)
                #  Blank space
                elif chars == "X":
                    self.xShift += size
                #  ? block
                elif chars == "?":
                    new_brick = Block(self.screen, self.settings, 6)
                    new_brick.rect.x, new_brick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(new_brick)
                #  Mushroom blocks (look like ? blocks):
                elif chars == "M":
                    new_brick = Block(self.screen, self.settings, 6, 0, 1)
                    new_brick.rect.x, new_brick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(new_brick)
                #  Invisible walls
                elif chars == "I":
                    new_invis = Block(self.screen, self.settings, 8, 0, 1)
                    new_invis.rect.x, new_invis.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    invis.add(new_invis)

                #  Goombas
                elif chars == "G":
                    new_goomba = Goomba(self.screen, self.settings)
                    new_goomba.rect.x, new_goomba.rect.y = self.xShift + size / 4, self.yShift - size / 10
                    self.xShift += size
                    goombas.add(new_goomba)
                elif chars == "K":
                    new_koopa = Koopa(self.screen, self.settings)
                    new_koopa.rect.x, new_koopa.rect.y = self.xShift + size / 4, self.yShift - size / 10
                    self.xShift += size
                    koopa.add(new_koopa)

            self.xShift = 0
            self.yShift += size
        print("Done.")

    @staticmethod
    def draw_map(floors, blocks, pipes, goombas, invis_g, koopas):
        for floor in floors:
            floor.blit()
        for block in blocks:
            block.blit()
        for pipe in pipes:
            pipe.blit()
        for goomba in goombas:
            goomba.draw_goomba()
        for koopa in koopas:
            koopa.draw_koopa()
        for invis in invis_g:
            invis.blit()

    @staticmethod
    def shift_map(floors, blocks, pipes, settings, goombas, invis_g, koopas):
        # world_shift = 0
        if settings.moving_right:
            for floor in floors:
                floor.rect.x -= 1
            for block in blocks:
                block.rect.x -= 1
            for pipe in pipes:
                pipe.rect.x -= 1
            for goomba in goombas:
                goomba.rect.x -= 1
            for koopa in koopas:
                koopa.rect.x -= 1
            for invis in invis_g:
                invis.rect.x -= 1
