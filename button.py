# -*- coding:utf-8 -*-

import pygame.font

class Button():
	def __init__(self, ai_settings, screen, msg):
		# 初始化按钮的属性
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# 设置按钮的尺寸和其他属性
		self.width, self.height = 200, 50
		self.button_color = (12, 24, 26)		# 按钮颜色为黑
		self.text_color = (255, 255, 255)	# 文本颜色为白
		self.font = pygame.font.SysFont(None, 48)	# 使用默认字体，字体号为48
		
		# 创建按钮rect对象, 并使其居中
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center	# 让按钮的center属性设置为屏幕的center属性
		
		# 按钮的标签只需创建一次
		self.prep_msg(msg)	# 通过将字符串渲染为图像来处理文本
		
	def prep_msg(self, msg):
		# 将msg渲染为图像,并使其在按钮上居中
		self.msg_image = self.font.render(msg, True, self.text_color,
							self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center	# 文本图像的center属性设置为按钮的center属性
		
	def draw_button(self):
		# 绘制一个用颜色填充的按钮，再绘制文本
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
