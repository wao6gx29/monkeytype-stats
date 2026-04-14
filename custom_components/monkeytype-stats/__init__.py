""" Monkeytype stats integration"""
import aiohttp

base_url = "https://api.monkeytype.com" 
ape_key = "cle_api"


public_stats = aiohttp.get(
  base_url + '/public/typingStats')
stats = public_stats.json()
print(public_stats)


public_leaderboard = aiohttp.get(
  base_url + '/leaderboards',
  params={'language': 'english', 'mode': 'time', 'mode2': '60'}
  )
public_leaderboard = public_leaderboard.json()
print(public_leaderboard)

currentTestActivity = aiohttp.get(
  base_url + '/users/currentTestActivity',
  params={'language': 'english', 'mode': 'time', 'mode2': '60'},
  headers={'Authorization': f'ApeKey {ape_key}'}
  )
message_erreur = currentTestActivity
currentTestActivity = currentTestActivity.json()
print(currentTestActivity)
print(message_erreur)
