import pygame
from floor import Floor
from brick import Brick
from questionBlock import QuestionBlock
from mushroomBlock import MushroomBlock

class BuildMap():
    def __init__(self, screen, settings):
        self.screen, self.settings = screen, settings
        self.file = open("maps/level1.txt", "r")
        self.textNewLine = "/n"
        self.line = ""
        self.lines = []
        self.xShift = 0
        self.yShift = 35
        self.worldShift = 0

        if self.file.mode == "r":
            self.contents = self.file.read()
            print("Start of read")

        for chars in self.contents:
            if chars != "\n":
                self.line += chars
            else:
                self.lines.append(self.line)
                self.line = ""

    def makeMap(self, floors, bricks, questionBlocks, mushroomBlocks):
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
                    newBrick = Brick(self.screen, self.settings)
                    newBrick.rect.x, newBrick.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    bricks.add(newBrick)
                #  Blank space
                elif chars == "X":
                    self.xShift += size
                #  ? block
                elif chars == "?":
                    newQuestion = QuestionBlock(self.screen, self.settings)
                    newQuestion.rect.x, newQuestion.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    questionBlocks.add(newQuestion)
                    self.xShift += size
                #  Mushroom blocks (look like ? blocks):
                elif chars == "M":
                    newMushroom = MushroomBlock(self.screen, self.settings)
                    newMushroom.rect.x, newMushroom.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    mushroomBlocks.add(newMushroom)
                    self.xShift += size

            self.xShift = 0
            self.yShift += size
        print("Done.")

    def drawMap(self, floors, bricks, questionBlocks, mushroomBlocks):
        for floor in floors:
            floor.blit()
        for brick in bricks:
            brick.blit()
        for questionBlock in questionBlocks:
            questionBlock.blit()
        for mushroomBlock in mushroomBlocks:
            mushroomBlock.blit()


