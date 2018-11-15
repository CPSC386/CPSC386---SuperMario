import pygame
from floor import Floor
from brick import Brick
from block import Block # testing Diverse Block
from questionBlock import QuestionBlock
from mushroomBlock import MushroomBlock
from unbreakableBrick import UnbreakableBrick
from pipe import Pipe
from goomba import Goomba


class BuildMap():
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


    def makeMap(self, floors, blocks, pipes, goombas):
        size = self.settings.rectSize
        for row in self.lines:
            for chars in row:
                #  Floor
                if chars == "F":
                    newFloor = Floor(self.screen, self.settings)
                    newFloor.rect.x, newFloor.rect.y = self.xShift, self.yShift
                    self.xShift += size
                    floors.add(newFloor)
                #  Breakable brick
                elif chars == "B":
                    newBrick = Block(self.screen, self.settings, 4)
                    newBrick.rect.x, newBrick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(newBrick)
                #  Unbreakable brick
                elif chars == "U":
                    newBrick = Block(self.screen, self.settings, 0)
                    newBrick.rect.x, newBrick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(newBrick)
                #  Pipe
                elif chars == "P":
                    newPipe = Pipe(self.screen, self.settings)
                    newPipe.rect.x, newPipe.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    pipes.add(newPipe)
                #  Blank space
                elif chars == "X":
                    self.xShift += size
                #  ? block
                elif chars == "?":
                    newBrick = Block(self.screen, self.settings, 6)
                    newBrick.rect.x, newBrick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(newBrick)
                #  Mushroom blocks (look like ? blocks):
                elif chars == "M":
                    newBrick = Block(self.screen, self.settings, 6, 0, 1)
                    newBrick.rect.x, newBrick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    blocks.add(newBrick)

                #  Goombas
                elif chars == "G":
                    newGoomba = Goomba(self.screen, self.settings)
                    newGoomba.rect.x, newGoomba.rect.y = self.xShift + size / 4, self.yShift - size / 10
                    self.xShift += size
                    goombas.add(newGoomba)

            self.xShift = 0
            self.yShift += size
        print("Done.")

    def drawMap(self, floors, blocks, pipes, goombas):
        for floor in floors:
            floor.blit()
        for block in blocks:
            block.blit()
        for pipe in pipes:
            pipe.blit()
        for goomba in goombas:
            goomba.drawGoomba()

    def shiftMap(self, floors, blocks, pipes, settings, goombas):
        worldShift = 0
        if settings.moving_right == True:
            for floor in floors:
                floor.rect.x -= 1
            for block in blocks:
                block.rect.x -= 1
            for pipe in pipes:
                pipe.rect.x -= 1
            for goomba in goombas:
                goomba.rect.x -= 1