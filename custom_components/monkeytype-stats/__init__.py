""" Monkeytype stats integration"""
import aiohttp
import asyncio

base_url = "https://api.monkeytype.com" 
ape_key = "cle_api"

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + '/public/typingStats') as resp:
          print(resp.status)
          print(await resp.text())
          print(await resp.json())
          testsCompleted = resp.json["data"]["testsCompleted"]
          testsStarted = resp.json["data"]["testsStarted"]
          timeTyping = resp.json["data"]["timeTyping"]
          print('Nombre de tests complétés : ' + testsCompleted)
          print('Nombre de tests commencés : ' + testsStarted)
          print('Temps de frape total : ' + timeTyping)


asyncio.run(main())



#public_stats = aiohttp.get(
#  base_url + '/public/typingStats')
#stats = public_stats.json()
#print(public_stats)


#public_leaderboard = aiohttp.get(
#  base_url + '/leaderboards',
#  params={'language': 'english', 'mode': 'time', 'mode2': '60'}
#  )
#public_leaderboard = public_leaderboard.json()
#print(public_leaderboard)

#currentTestActivity = aiohttp.get(
#  base_url + '/users/currentTestActivity',
#  params={'language': 'english', 'mode': 'time', 'mode2': '60'},
#  headers={'Authorization': f'ApeKey {ape_key}'}
#  )
#message_erreur = currentTestActivity
#currentTestActivity = currentTestActivity.json()
#print(currentTestActivity)
#print(message_erreur)
