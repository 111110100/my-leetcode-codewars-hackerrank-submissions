'''
You have a group chat application, but who is online!?

You want to show your users which of their friends are online and available to chat!

Given an input of an array of objects containing usernames, status and time since last activity (in mins), create a function to work out who is online, offline and away.

If someone is online but their lastActivity was more than 10 minutes ago they are to be considered away.

The input data has the following structure:

[{
  username: 'David',
  status: 'online',
  lastActivity: 10
}, {
  username: 'Lucy', 
  status: 'offline',
  lastActivity: 22
}, {
  username: 'Bob', 
  status: 'online',
  lastActivity: 104
}]
The corresponding output should look as follows:

{
  online: ['David'],
  offline: ['Lucy'],
  away: ['Bob']
}
If for example, no users are online the output should look as follows:

{
  offline: ['Lucy'],
  away: ['Bob']
}
username will always be a string, status will always be either 'online' or 'offline' (UserStatus enum in C#) and lastActivity will always be number >= 0.

Finally, if you have no friends in your chat application, the input will be an empty array []. In this case you should return an empty object {} (empty Dictionary in C#).
'''

def who_is_online(friends):
    status = {}
    for f in friends:
        if f['status'] == 'online' and f['last_activity'] > 10:
            if status.get('away') == None:
                status['away'] = [f['username']]
            else:
                status['away'].append(f['username'])
        else:
            if status.get(f['status']) == None:
                status[f['status']] = [f['username']]
            else:
                status[f['status']].append(f['username'])
    return status

#friends = [{"username": "David", "status": "online", "last_activity": 10},
#           {"username": "Lucy", "status": "offline", "last_activity": 22},
#           {"username": "Bob", "status": "online", "last_activity": 104}]

friends = [{'username': 'David', 'status': 'online', 'last_activity': 10}, {'username': 'Lucy', 'status': 'online', 'last_activity': 0}, {'username': 'Bob', 'status': 'online', 'last_activity': 3}, {'username': 'Julie', 'status': 'offline', 'last_activity': 104}, {'username': 'Lenny', 'status': 'online', 'last_activity': 38}]

print(who_is_online(friends))

'''
def who_is_online(friends):
    res = {}
    online = [user['username'] for user in friends if (user['status'] == 'online' and user['last_activity'] <= 10)]
    offline = [user['username'] for user in friends if user['status'] == 'offline']
    away = [user['username'] for user in friends if (user['status'] == 'online' and user['last_activity'] > 10)]
    if online:
        res['online'] = online
    if offline:
        res['offline'] = offline
    if away:
        res['away'] = away
    return res

def who_is_online(friends):
    activities = {}
    for friend in friends:
        activities.setdefault('away' if friend['status'] == 'online' and friend['last_activity'] > 10 else friend['status'], []).append(friend['username'])
    
    return activities

def who_is_online(friends):
    res = {}
    for f in friends:
        status = 'offline' if f['status'] != 'online' else 'away' if f['last_activity'] > 10 else 'online'
        res.setdefault(status, []).append(f['username'])
   return res
'''