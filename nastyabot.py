#! /usr/bin/env python
# -*- coding: utf-8 -*-
import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import preview

NASTYA = ["photo-140929_13730091", "photo559433773_457247408", "photo22505982_457239732"] #Можете добавлять свои фото - ["photo123_123", "photo123_123", "photo123_123", "photo123_123", "photo123_123"] - вот так


vk_session = vk_api.VkApi(token='ТОКЕН') #Замените ТОКЕН на token от группы 
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,123) #Замените 123 на ID от группы 
def main():

	keyboard = VkKeyboard(one_time=False) 
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()	
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.NEGATIVE)
	keyboard.add_line()
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.POSITIVE)
	keyboard.add_line()
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.NEGATIVE)
	keyboard.add_line()	
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.POSITIVE)
	keyboard.add_line()
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.POSITIVE)
	keyboard.add_line()
	keyboard.add_button("NASTYA Shturm TaksiMironTM vto.pe", color=VkKeyboardColor.NEGATIVE)
	
	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("Настюху добавили в чат!!!")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, attachment=random.choice(NASTYA), keyboard=keyboard.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('Настюха отработала!!!') 

if __name__ == '__main__':
	main()
