import pygame

# INIT
pygame.init() # menjalankan/meng-inisialisasi pygame

# membuat display
window_panjang = 1000
window_lebar = 700
window = pygame.display.set_mode((window_panjang, window_lebar))

# OBJECT GAME
x = 500
y = 350

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

isRun = True
while isRun:
    pygame.time.delay(10)
    # USER INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # ambil ke kanan
    if keys[pygame.K_RIGHT] and x < window_panjang-panjang:
        x += speed

    # ambil ke bawah
    if keys[pygame.K_DOWN] and y < window_lebar-lebar:
        y += speed

    # ambil ke atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # UPDATE ASSET
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar, panjang))
    # RENDER KE DISPLAY
    pygame.display.update()

pygame.quit()

