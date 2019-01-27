# -*- coding:GBK -*-

class Settings():
	# 存储《外星人入侵》的所有设置 的类
	def __init__(self):
		'''初始化游戏的静态设置'''
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		# 飞船设置
		self.ship_limit = 3
		
		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10
		
		# 外星人设置
		self.fleet_drop_speed = 3
		
		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1
		
		self.initialize_dynamic_settings()#初始化随游戏进行而变化的属性
		
	def initialize_dynamic_settings(self):
		'''初始化随游戏进行而变化的属性'''
		self.ship_speed_factor = 0.5
		self.bullet_speed_factor = 0.5
		self.alien_speed_factor = 0.5
		
		self.fleet_direction = 1	# 1表示向右, -1表示向左
	
	def increase_speed(self):
		'''提高速度设置'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		
		
		
		
		
		'''
		# 初始化游戏外观设置, 屏幕设置
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		# 飞船的设置
		self.ship_speed_factor = 0.5
		self.ship_limit = 3
		# 子弹设置
		self.bullet_speed_factor = 0.5
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10	# 存储所允许的最大子弹数
		# 外星人设置
		self.alien_speed_factor = 0.5	# 设置外星人向右移动的速速
		self.fleet_drop_speed = 30	# 撞到屏幕边缘时向下移动的速度
		self.fleet_direction = 1	# fleet_direction为1表示向右移动，为-1表示向左移动
		'''
		
