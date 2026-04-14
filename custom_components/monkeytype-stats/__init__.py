""" Monkeytype stats integration"""
import aiohttp
import asyncio

base_url = "https://api.monkeytype.com" 
ape_key = "cle_api"

async def public_datas_fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + '/public/typingStats') as resp:
          datas = await resp.json()
          print(datas)
          testsCompleted = datas["data"]["testsCompleted"]
          testsStarted = datas["data"]["testsStarted"]
          timeTyping = datas["data"]["timeTyping"]
          print('Nombre de tests complétés : ' + str(testsCompleted))
          print('Nombre de tests commencés : ' + str(testsStarted))
          print('Temps de frape total : ' + str(timeTyping))
asyncio.run(public_datas_fetch())



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
