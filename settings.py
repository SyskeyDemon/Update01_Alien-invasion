# -*- coding:GBK -*-

class Settings():
	# �洢�����������֡����������� ����
	def __init__(self):
		'''��ʼ����Ϸ�ľ�̬����'''
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		# �ɴ�����
		self.ship_limit = 3
		
		# �ӵ�����
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10
		
		# ����������
		self.fleet_drop_speed = 3
		
		# ��ʲô�����ٶȼӿ���Ϸ����
		self.speedup_scale = 1.1
		
		self.initialize_dynamic_settings()#��ʼ������Ϸ���ж��仯������
		
	def initialize_dynamic_settings(self):
		'''��ʼ������Ϸ���ж��仯������'''
		self.ship_speed_factor = 0.5
		self.bullet_speed_factor = 0.5
		self.alien_speed_factor = 0.5
		
		self.fleet_direction = 1	# 1��ʾ����, -1��ʾ����
	
	def increase_speed(self):
		'''����ٶ�����'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		
		
		
		
		
		'''
		# ��ʼ����Ϸ�������, ��Ļ����
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		# �ɴ�������
		self.ship_speed_factor = 0.5
		self.ship_limit = 3
		# �ӵ�����
		self.bullet_speed_factor = 0.5
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 255, 60, 60
		self.bullets_allowed = 10	# �洢������������ӵ���
		# ����������
		self.alien_speed_factor = 0.5	# ���������������ƶ�������
		self.fleet_drop_speed = 30	# ײ����Ļ��Եʱ�����ƶ����ٶ�
		self.fleet_direction = 1	# fleet_directionΪ1��ʾ�����ƶ���Ϊ-1��ʾ�����ƶ�
		'''
		