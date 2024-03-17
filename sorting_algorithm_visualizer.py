import pygame
import random

class Sorting_Algorithm_Visualizer:

    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Algorithm Visualizer")
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        self.total_bars = 30
        self.bars = []
        self.colors = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
        self.x, self.y, self.width, self.height = 250, 350, 10, 350

        self.bars.append([pygame.Rect(self.x, self.y, self.width, self.height), self.colors[random.randint(0, len(self.colors) - 1)]])

        for i in range(self.total_bars):
            random_number = random.randint(-300, 300)
            random_color = self.colors[random.randint(0, len(self.colors) - 1)]
            r = pygame.Rect(self.x + (i + 1) * self.width, self.y + random_number, self.width, self.height - random_number)
            self.bars.append([r, random_color])

    def write_text(self):

        WHITE = (255, 255, 255)

        insertion_sort_text = self.font.render(f"I - INSERTION SORT", True, WHITE)
        bubble_sort_text = self.font.render(f"B - BUBBLE SORT", True, WHITE)
        quick_sort_text = self.font.render(f"Q - QUICK SORT", True, WHITE)
        selection_sort_text = self.font.render(f"S - SELECTION SORT", True, WHITE)
        self.screen.blit(insertion_sort_text, (25, 50))
        self.screen.blit(bubble_sort_text, (225, 50))
        self.screen.blit(quick_sort_text, (425, 50))
        self.screen.blit(selection_sort_text, (650, 50))

    def bubble_sort_algoritm(self):

        GREEN = (0, 255, 0)

        sorted = True

        while sorted:

            sorted = False

            for i in range(len(self.bars) - 1):

                if self.bars[i][0].height > self.bars[i + 1][0].height:

                    # Swap rectangles
                    self.bars[i][0].y, self.bars[i + 1][0].y = self.bars[i + 1][0].y, self.bars[i][0].y
                    self.bars[i][0].height, self.bars[i + 1][0].height = self.bars[i + 1][0].height, self.bars[i][0].height
                    self.bars[i][1], self.bars[i + 1][1] = self.bars[i + 1][1], self.bars[i][1]

                    # Draw rectangles and update display after each swap
                    self.screen.fill(GREEN)  # Clear the screen
                    for bar in self.bars:
                        pygame.draw.rect(self.screen, bar[1], bar[0])

                    self.write_text()
                    pygame.display.update()
                    sorted = True

                    pygame.time.delay(200)

    def insertion_sort_algorithm(self):

        GREEN = (0, 255, 0)

        for i in range(len(self.bars) - 1):

            j = i

            while j >= 0 and self.bars[j+1][0].height < self.bars[j][0].height:
                self.bars[j][0].y, self.bars[j + 1][0].y = self.bars[j + 1][0].y, self.bars[j][0].y
                self.bars[j][0].height, self.bars[j + 1][0].height = self.bars[j + 1][0].height, self.bars[j][0].height
                self.bars[j][1], self.bars[j + 1][1] = self.bars[j + 1][1], self.bars[j][1]

                j = j - 1

                self.screen.fill(GREEN)
                # Draw rectangles and update display after each swap
                for bar in self.bars:
                    pygame.draw.rect(self.screen, bar[1], bar[0])

                self.write_text()
                pygame.display.update()
                pygame.time.delay(200)

    def selection_sort_algorithm(self):

        GREEN = (0, 255, 0)

        for i in range(len(self.bars)):

            min = self.bars[i][0].height

            for j in range(i, len(self.bars)):
                if self.bars[j][0].height <= min:
                    min = self.bars[j][0].height
                    k = j

            self.bars[i][0].y, self.bars[k][0].y = self.bars[k][0].y, self.bars[i][0].y
            self.bars[i][0].height, self.bars[k][0].height = self.bars[k][0].height, self.bars[i][0].height
            self.bars[i][1], self.bars[k][1] = self.bars[k][1], self.bars[i][1]

            self.screen.fill(GREEN)
            # Draw rectangles and update display after each swap
            for bar in self.bars:
                pygame.draw.rect(self.screen, bar[1], bar[0])

            self.write_text()
            pygame.display.update()
            pygame.time.delay(200)

    def quicksort_algorithm(self, left, right):

        if left < right:
            partition_pos = self.partition(left, right)
            self.quicksort_algorithm(left, partition_pos - 1)
            self.quicksort_algorithm(partition_pos + 1, right)
            pygame.time.delay(200)
    def partition(self, left, right):

        GREEN = (0, 255, 0)

        i = left
        j = right - 1

        pivot = self.bars[right][0].height

        while i < j:
            while i < right and self.bars[i][0].height < pivot:
                i = i + 1
            while j > left and self.bars[j][0].height >= pivot:
                j = j - 1
            if i < j:
                self.bars[i][0].y, self.bars[j][0].y = self.bars[j][0].y, self.bars[i][0].y
                self.bars[i][0].height, self.bars[j][0].height = self.bars[j][0].height, self.bars[i][0].height
                self.bars[i][1], self.bars[j][1] = self.bars[j][1], self.bars[i][1]

                self.screen.fill(GREEN)
                # Draw rectangles and update display after each swap
                for bar in self.bars:
                    pygame.draw.rect(self.screen, bar[1], bar[0])

                self.write_text()
                pygame.display.update()
                pygame.time.delay(200)

        if self.bars[i][0].height > pivot:

            self.bars[i][0].y, self.bars[right][0].y = self.bars[right][0].y, self.bars[i][0].y
            self.bars[i][0].height, self.bars[right][0].height = self.bars[right][0].height, self.bars[i][0].height
            self.bars[i][1], self.bars[right][1] = self.bars[right][1], self.bars[i][1]

            self.screen.fill(GREEN)

            # Draw rectangles and update display after each swap
            for bar in self.bars:
                pygame.draw.rect(self.screen, bar[1], bar[0])

            pygame.display.update()
            pygame.time.delay(200)

        return i

    def running_main_loop(self):

        running = True

        GREEN = (0, 255, 0)

        while running:

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(GREEN)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_b]:
                self.bubble_sort_algoritm()
                pygame.time.delay(1000)
                pygame.display.update()
                break

            elif keys[pygame.K_i]:
                self.insertion_sort_algorithm()
                pygame.time.delay(1000)
                pygame.display.update()
                break

            elif keys[pygame.K_s]:
                self.selection_sort_algorithm()
                pygame.time.delay(1000)
                pygame.display.update()
                break

            elif keys[pygame.K_q]:
                self.quicksort_algorithm(0, len(self.bars)-1)
                pygame.time.delay(1000)
                pygame.display.update()
                break

        pygame.quit()

