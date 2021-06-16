from mcpi.minecraft import Minecraft  # quarry? https://quarry.readthedocs.io/en/latest/index.html
# import quarry
import minecraftstuff
import time
from math import *
import sys
import os


# import random
# mc.postToChat('Hello, World!')  # write in chat


class MinecraftTest:
    init_pos = 0

    def __init__(self):  # ??? Uses mc instance.
        # create minecraft object
        print("\nFUNCTION: MinecraftGenerator __init__")
        print("Opening connection to Minecraft Pi")
        try:
            self.mc = Minecraft.create()  # minecraft world connection
            self.init_pos = self.mc.player.getTilePos()
        except:
            # print("There was an error connecting to Minecraft.")
            sys.exit("There was an error connecting to Minecraft.")
        pos = self.mc.player.getTilePos()
        direction = self.mc.player.getRotation()
        print(f'Current position: x = {pos.x}, y = {pos.y}, z = {pos.z}')
        print(f'Current direction: {direction}')

    def immutable_blocks(self):
        self.mc.setting('world_immutable', True)
        time.sleep(20)
        self.mc.setting('world_immutable', False)
        self.mc.postToChat('world_immutable = false')

    def write_coord_in_chat(self):  # write current coordinates to chat every 5 seconds
        while True:
            self.mc.postToChat(str(self.mc.player.getTilePos()))
            time.sleep(5)

    def build_house(self):
        target = self.init_pos.clone()
        target.x -= 3
        block = 1  # 162 wood
        build_x = 10
        build_y = 6
        build_z = 10
        for i in range(build_x):  # x
            for j in range(build_z):  # z
                for k in range(build_y):  # y
                    self.mc.setBlock(target.x - i, target.y, target.z - j, block)  # floor
                    self.mc.setBlock(target.x - i, target.y + k, target.z, block)  # left wall
                    self.mc.setBlock(target.x - i, target.y + k, target.z - 9, block)  # right wall
                    self.mc.setBlock(target.x, target.y + k, target.z - j, block)  # front wall
                    self.mc.setBlock(target.x - 9, target.y + k, target.z - j, block)  # back wall
                    # self.mc.setBlock(target.x - i, target.y + 5, target.z - j, block)  # top
                for m in range(5):  # roof
                    self.mc.setBlock(target.x - m, target.y + 6 + m, target.z - j, 53, 1)  # stairs roof
                    self.mc.setBlock(target.x - 9 + m, target.y + 6 + m, target.z - j, 53, 0)  # stairs roof
                    if m == 4:
                        delta = 1
                    else:
                        delta = 0
                    self.mc.setBlocks(target.x - 1 - m, target.y + 6 + m - delta, target.z,
                                      target.x - 8 + m, target.y + 6 + m - delta, target.z, block)
                    self.mc.setBlocks(target.x - 1 - m, target.y + 6 + m - delta, target.z - 9,
                                      target.x - 8 + m, target.y + 6 + m - delta, target.z - 9, block)

        self.mc.setBlock(target.x, target.y + 2, target.z - build_z // 2 + 1, 0)  # doorway
        self.mc.setBlock(target.x, target.y + 1, target.z - build_z // 2 + 1, 0)  # doorway
        self.mc.setBlock(target.x, target.y + 2, target.z - build_z // 2 + 1, 64, 8)  # door
        self.mc.setBlock(target.x, target.y + 1, target.z - build_z // 2 + 1, 64, 0)  # door
        self.mc.setBlock(target.x - 7, target.y + 1, target.z - 1, 26, 8)  # bed
        self.mc.setBlock(target.x - 7, target.y + 1, target.z - 2, 26, 0)  # bed
        self.mc.setBlock(target.x - 8, target.y + 4, target.z - 2, 50, 1)  # torch
        self.mc.setBlock(target.x - 1, target.y + 4, target.z - 2, 50, 2)  # torch
        self.mc.setBlock(target.x - 8, target.y + 4, target.z - 7, 50, 1)  # torch
        self.mc.setBlock(target.x - 1, target.y + 4, target.z - 7, 50, 2)  # torch
        self.mc.setBlock(target.x - 4, target.y + 8, target.z - 1, 50, 4)  # torch
        self.mc.setBlock(target.x - 5, target.y + 8, target.z - 1, 50, 4)  # torch
        self.mc.setBlock(target.x - 4, target.y + 8, target.z - 8, 50, 3)  # torch
        self.mc.setBlock(target.x - 5, target.y + 8, target.z - 8, 50, 3)  # torch
        self.mc.setBlock(target.x + 1, target.y, target.z - build_z // 2 + 1, 53, 1)  # stairs
        self.mc.setBlock(target.x - 1, target.y + 1, target.z - build_z // 2 + 1, 72, 0)  # pressure plate
        self.mc.setBlock(target.x - 7, target.y + 1, target.z - 8, 54, 3)  # chest
        self.mc.setBlock(target.x - 6, target.y + 1, target.z - 8, 54, 3)  # chest
        self.mc.setBlock(target.x - 8, target.y + 2, target.z - 8, 61, 3)  # iron
        self.mc.setBlock(target.x - 8, target.y + 1, target.z - 8, 61, 3)  # iron
        self.mc.setBlock(target.x - 5, target.y + 1, target.z - 8, 116, 0)  # Enchanting Table
        self.mc.setBlock(target.x - 4, target.y + 1, target.z - 8, 145, 0)  # anvil
        self.mc.setBlock(target.x - 3, target.y + 1, target.z - 8, 58, 1)  # crafting table
        self.mc.setBlock(target.x - 2, target.y + 1, target.z - 8, 117, 3)  # brewing stand
        self.mc.setBlocks(target.x - 9, target.y + 2, target.z - build_z // 2 + 2, target.x - 9, target.y + 4,
                          target.z - build_z // 2 - 1, 20)  # window

    def rainbow(self):
        """_mcpd
        create a rainbow.
        The code is from:
        http://dev.bukkit.org/bukkit-plugins/raspberryjuice/
        """
        pos = self.mc.player.getTilePos()
        colors = [14, 1, 4, 5, 3, 11, 10]
        height = 60
        self.mc.setBlocks(pos.x - 64, 0, 0, pos.x + 64, height + len(colors), 0, 0)
        for x in range(0, 128):
            for colour_index in range(0, len(colors)):
                y = sin((x / 128.0) * pi) * height + colour_index
                self.mc.setBlock(pos.x + x - 64, pos.y + y, pos.z,
                                 35, colors[len(colors) - 1 - colour_index])

    def del_or_fill(self, mod=1, block=1, start_x=0, start_y=0, start_z=0, end_x=30, end_y=30, end_z=30):
        pos = self.init_pos
        if mod == 1:
            block = 0
            print('eraser start')
        elif mod == 2:
            block = block
            print('filler start')
        self.mc.setBlocks(pos.x - start_x - 1, pos.y + start_y, pos.z - start_z, pos.x - 1 - end_x, pos.y + end_y,
                          pos.z - end_z, block)

    def follower(self):
        draw = minecraftstuff.MinecraftDrawing(self.mc)  # use command minecraftstuff.MinecraftDrawing(mc)

        r2d2 = self.mc.player.getTilePos()  # current position
        block1 = 57  # Block ID (57 - diamond)
        block2 = 11
        self.mc.setBlock(r2d2.x, r2d2.y, r2d2.z + 3, block1)  # set the block to defined place

        r2d2.z += 3

        while True:  # make block follow player
            pos = self.mc.player.getTilePos()
            target = pos.clone()

            if r2d2 != target:
                blocks = draw.getLine(r2d2.x, r2d2.y, r2d2.z, target.x, target.y,
                                      target.z)  # find line between positions

            for step in blocks[:-2]:  # go to line blocks except 2 in the end
                self.mc.setBlock(r2d2.x, r2d2.y, r2d2.z, 0)  # del old blocks (exchange to air block)
                r2d2 = step.clone()  # copy to the new place
                r2d2.y = self.mc.getHeight(r2d2.x, r2d2.z) + 1  # set r2d2 to the ground

                self.mc.setBlock(r2d2.x, r2d2.y, r2d2.z, block1)
                self.mc.setBlock(r2d2.x, r2d2.y, r2d2.z - 1, block2)
                time.sleep(0.2)

    def teleport(self, x=0, y=91, z=0):  # teleports player to x, y, z coords and add block of stone under player
        if self.mc.getBlock(x, y, z) == 0 and self.mc.getBlock(x, y + 1, z) == 0:
            self.mc.setBlock(x, y - 1, z, 1)
            self.mc.player.setTilePos(x, y, z)
        else:
            self.mc.postToChat(
                f'Teleport location is filled by blocks, you can teleport to ({x},{self.mc.getHeight(x, z) + 1},{z})')

    def set_stone_when_not_on_the_ground(self):
        while True:
            pos = self.mc.player.getTilePos()
            if self.mc.getBlock(pos.x, pos.y - 1, pos.z) != 1:
                self.mc.setBlock(pos.x, pos.y - 1, pos.z, 1)

    def diamond_find(self, x, y, z):
        diamond_list = []
        pos = self.mc.player.getTilePos()
        count = 0
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    print(f'Current position: x = {i}, y = {j}, z = {k}')
                    if self.mc.getBlock(pos.x - i, pos.y - 50 - j, pos.z - k) == 56:
                        diamond_list.append([pos.x - i, pos.y - 50 - j, pos.z - k])
                        count += 1
        if count == 0:
            self.mc.postToChat('There is on diamonds in this area.')
        else:
            with open('diamond_file.txt', 'w') as f:
                os.system(r'nul>diamond_file.txt')
                i = 0
                for item in diamond_list:
                    f.write(f'{i}. ' + str(item) + '\n')
                    i += 1

    def make_garden_bed(self, seed=141):  # 141: carrots, 142: potatoes, 59: wheat,
        pos = self.mc.player.getTilePos()
        pos.x = pos.x - 1
        mt.del_or_fill(1, 0, 1, 0, -1, 10, 3, 11)
        self.mc.setBlocks(pos.x + 1, pos.y + 1, pos.z, pos.x, pos.y + 2, pos.z, 0)
        self.mc.setBlock(pos.x, pos.y, pos.z, 126, [1, 10])
        for j in range(1, 12, 2):
            # pass
            self.mc.setBlocks(pos.x - 1, pos.y, pos.z - j + 1, pos.x - 10, pos.y, pos.z - j + 1, 9)
            self.mc.setBlocks(pos.x - 1, pos.y + 3, pos.z - j + 1, pos.x - 10, pos.y + 3, pos.z - j + 1, 50, 3)
        time.sleep(2)
        for i in range(0, 13, 2):
            self.mc.setBlocks(pos.x - 1, pos.y, pos.z - i + 1, pos.x - 10, pos.y, pos.z - i + 1, 60)
            self.mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - i + 1, pos.x - 10, pos.y + 1, pos.z - i + 1, seed, [1, 0])
            self.mc.setBlocks(pos.x - 1, pos.y + 3, pos.z - i + 1, pos.x - 10, pos.y + 3, pos.z - i + 1, 20)

    def chest_test(self):  # not finished
        pos = self.mc.player.getTilePos()

        self.mc.setBlocks(pos.x - 1, pos.y, pos.z, pos.x, pos.y, pos.z - 1, 5)  # сундук
        # self.mc.setBlock(pos.x - 1, pos.y, pos.z, 54, [1, 0, 364])
        # self.mc.postToChat(self.mc.getBlockWithData(pos.x - 2, pos.y, pos.z))
        # self.mc.spawnEntity(pos.x - 1, pos.y, pos.z, 100) #  mobs spawn!!!

    def animal_farm(self):
        pos = self.mc.player.getTilePos()
        mt.del_or_fill(1, 0, 0, 0, 0, 10, 3, 10)
        mt.del_or_fill(1, 0, 8, 0, 8, 11, 27, 11)
        self.mc.setBlocks(pos.x - 2, pos.y, pos.z, pos.x - 2, pos.y + 1, pos.z - 10, 85, 0)
        self.mc.setBlock(pos.x - 2, pos.y, pos.z - 5, 107, 1)
        self.mc.setBlocks(pos.x - 10, pos.y, pos.z, pos.x - 10, pos.y + 1, pos.z - 10, 85, 0)
        self.mc.setBlocks(pos.x - 2, pos.y, pos.z, pos.x - 10, pos.y + 3, pos.z, 20)
        self.mc.setBlocks(pos.x - 2, pos.y + 4, pos.z, pos.x - 10, pos.y + 4, pos.z, 50, 5)
        self.mc.setBlocks(pos.x - 2, pos.y, pos.z - 10, pos.x - 10, pos.y + 3, pos.z - 10, 20)
        self.mc.setBlocks(pos.x - 2, pos.y + 4, pos.z - 10, pos.x - 10, pos.y + 4, pos.z - 10, 50, 5)

    def torches_on_the_way(self):
        while True:
            pos = self.mc.player.getTilePos()
            self.mc.setBlock(pos.x + 1, pos.y, pos.z, 50, 5)
            time.sleep(3)

    def enemy_mob_farm(self):
        pos = self.mc.player.getTilePos()
        self.mc.setBlocks(pos.x, pos.y + 28, pos.z, pos.x - 30, pos.y + 35, pos.z - 30, 0)  # коробка
        self.mc.setBlocks(pos.x, pos.y + 28, pos.z, pos.x - 19, pos.y + 33, pos.z - 19, 1)  # коробка
        self.mc.setBlocks(pos.x - 1, pos.y + 31, pos.z - 1, pos.x - 18, pos.y + 32, pos.z - 18,
                          0)  # пространство для спавна
        self.mc.setBlocks(pos.x - 9, pos.y + 29, pos.z - 1, pos.x - 10, pos.y + 30, pos.z - 18, 0)  # желоб по z
        self.mc.setBlocks(pos.x - 1, pos.y + 29, pos.z - 9, pos.x - 18, pos.y + 30, pos.z - 10, 0)  # желоб по x

        self.mc.setBlocks(pos.x - 9, pos.y + 29, pos.z - 1, pos.x - 10, pos.y + 29, pos.z - 1, 8)  # вода
        self.mc.setBlocks(pos.x - 1, pos.y + 29, pos.z - 9, pos.x - 1, pos.y + 29, pos.z - 10, 8)  # вода
        self.mc.setBlocks(pos.x - 9, pos.y + 29, pos.z - 18, pos.x - 10, pos.y + 29, pos.z - 18, 8)  # вода
        self.mc.setBlocks(pos.x - 18, pos.y + 29, pos.z - 9, pos.x - 18, pos.y + 29, pos.z - 10, 8)  # вода
        self.mc.setBlocks(pos.x - 1, pos.y + 30, pos.z - 9, pos.x - 18, pos.y + 30, pos.z - 9, 68, 0)  # таблички
        self.mc.setBlocks(pos.x - 1, pos.y + 30, pos.z - 10, pos.x - 18, pos.y + 30, pos.z - 10, 68, 3)  # таблички
        self.mc.setBlocks(pos.x - 9, pos.y + 30, pos.z - 1, pos.x - 9, pos.y + 30, pos.z - 18, 68, 4)  # таблички
        self.mc.setBlocks(pos.x - 10, pos.y + 30, pos.z - 1, pos.x - 10, pos.y + 30, pos.z - 18, 68, 5)  # таблички
        self.mc.setBlocks(pos.x - 9, pos.y + 28, pos.z - 9, pos.x - 10, pos.y + 31, pos.z - 10,
                          0)  # отверстие посередине
        self.mc.setBlocks(pos.x - 8, pos.y + 5, pos.z - 8, pos.x - 11, pos.y + 27, pos.z - 11, 1)  # блок для падения
        self.mc.setBlocks(pos.x - 8, pos.y + 3, pos.z - 8, pos.x - 11, pos.y + 4, pos.z - 11,
                          20)  # блок для падения стекло
        self.mc.setBlocks(pos.x - 9, pos.y + 3, pos.z - 9, pos.x - 10, pos.y + 27, pos.z - 10,
                          0)  # отверстие посередине блока для падения
        self.mc.setBlocks(pos.x - 9, pos.y + 2, pos.z - 9, pos.x - 10, pos.y + 2, pos.z - 10, 154)  # воронки
        self.mc.setBlocks(pos.x - 10, pos.y, pos.z - 9, pos.x - 10, pos.y, pos.z - 10, 2)  # сундук

    def hell_portal(self):
        pos = self.init_pos
        self.mc.setBlocks(pos.x - 2, pos.y - 1, pos.z, pos.x - 2, pos.y + 3, pos.z - 3, 49)
        self.mc.setBlocks(pos.x - 2, pos.y, pos.z - 1, pos.x - 2, pos.y + 2, pos.z - 2, 90, 2)

    def letter_scan(self):
        pos = self.init_pos
        with open('Letters/0.txt', 'w') as file:  # change 0 to required letter
            for i in range(1, 11):
                for j in range(11):
                    block_id = self.mc.getBlock(pos.x - 2, pos.y + 10 - i, pos.z - j)
                    file.write(f'{-2} {10 - i} {-j} {block_id}\n')
        print('File closed')

    def letter_print(self, string='hi'):
        string = string.upper()
        pos = self.init_pos
        self.del_or_fill(1, 0, -50, 0, 0, 30, 20, len(string) * 12 + 20)
        for item in string:
            if item == ' ':
                pos.z -= 12
            else:
                with open(f'Letters\{item}.txt', 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        line = line.rstrip('\n')
                        block_position_list = line.split(' ')
                        if block_position_list[3] == '1':
                            block_position_list[3] = 89
                            print('hello')
                        self.mc.setBlock(pos.x + int(block_position_list[0]),
                                         pos.y + int(block_position_list[1]),
                                         pos.z + int(block_position_list[2]),
                                         int(block_position_list[3]))
                pos.z -= 12

    def find_ore(self, x, y, z, ore=15):
        # 14: gold, 15: iron, 16: coal, 73: redstone, 21: lapis
        ore_list = []
        pos = self.init_pos
        count = 0
        N = x * y * z
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    print(N)
                    N -= 1
                    if self.mc.getBlock(pos.x - i, pos.y + j, pos.z - k) == ore:
                        ore_list.append([pos.x - i, pos.y + j, pos.z - k])
                        count += 1
                        print(count)
        if count == 0:
            print('There is on ore in this area.')
        else:
            with open(f'd.txt', 'w') as f:
                i = 0
                for item in ore_list:
                    f.write(f'{i}. ' + str(item) + '\n')
                    i += 1

    def remove_except_ore(self):
        pos = self.init_pos
        remove_list = [1, 2, 3, 4, 8, 9, 10, 11, 12, 13]
        for i in range(20):
            for j in range(3):
                for k in range(20):
                    span = self.mc.getBlock(pos.x - i, pos.y + j, pos.z - k)
                    if span in remove_list:
                        self.mc.setBlock(pos.x - i, pos.y + j, pos.z - k, 0)
    def test_func(self):
        pos = self.init_pos
        for i in range(128):
            self.mc.setBlock(pos.x, pos.y, pos.z - 1, 50, 1)
            time.sleep(2)
            self.mc.setBlock(pos.x, pos.y, pos.z - 1, 0)



# -247,66,237
mt = MinecraftTest()
# mt.make_garden_bed(0)
# mt.del_or_fill(2, 50, 0, 0, 1, 0, 0, 11)
#mt.build_house()
# mt.write_coord_in_chat()
# mt.del_or_fill(1, 0, 0, 0, 0, 3, 10, 11)
# mt.animal_farm()
# mt.chest_test()
# mt.torches_on_the_way()
#mt.teleport(-247, 66, 237)
# mt.enemy_mob_farm()
# mt.hell_portal()
# mt.letter_scan()
# mt.letter_print('home is here')
# mt.find_ore(50, 5, 10, 73)
#mt.test_func()