from operator import itemgetter

import requests

url="https://hacker-news.firebaseio.com/v0/topstories.json"
r=requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:30]:
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"Status code: {r.status_code}")
    response_dict=r.json()
    
    submission_dict={
        'title':response_dict['title'],
        'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
        'comments':response_dict.get('descendants',0)
    }
    submission_dicts.append(submission_dict)
    
submission_dict={
    'title':itemgetter('title'),
    'hn_link':itemgetter('hn_link'),
    'comments':itemgetter('comments')
}

try:
     sorted_submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse=True)
except TypeError:
    print("Error: TypeError")
for sorted_submission_dict in sorted_submission_dicts:
    print(f"\nTitle:{sorted_submission_dict['title']}")
    print(f"Discussion link:{sorted_submission_dict['hn_link']}")
    print(f"Comments:{sorted_submission_dict['comments']}")